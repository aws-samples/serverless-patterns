'''
# Cloud Executable API

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## V2 Feature Flags

* `@aws-cdk/aws-s3:createDefaultLoggingPolicy`

Enable this feature flag to create an S3 bucket policy by default in cases where
an AWS service would automatically create the Policy if one does not exist.

For example, in order to send VPC flow logs to an S3 bucket, there is a specific Bucket Policy
that needs to be attached to the bucket. If you create the bucket without a policy and then add the
bucket as the flow log destination, the service will automatically create the bucket policy with the
necessary permissions. If you were to then try and add your own bucket policy CloudFormation will throw
and error indicating that a bucket policy already exists.

In cases where we know what the required policy is we can go ahead and create the policy so we can
remain in control of it.

https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-S3

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-s3:createDefaultLoggingPolicy": true
  }
}
```

* `@aws-cdk/aws-sns-subscriptions:restrictSqsDescryption`

Enable this feature flag to restrict the decryption of a SQS queue, which is subscribed to a SNS topic, to
only the topic which it is subscribed to and not the whole SNS service of an account.

Previously the decryption was only restricted to the SNS service principal. To make the SQS subscription more
secure, it is a good practice to restrict the decryption further and only allow the connected SNS topic to decryption
the subscribed queue.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-sns-subscriptions:restrictSqsDescryption": true
  }
}
```

* @aws-cdk/aws-apigateway:disableCloudWatchRole

Enable this feature flag to change the default behavior for aws-apigateway.RestApi and aws-apigateway.SpecRestApi
to *not* create a CloudWatch role and Account. There is only a single ApiGateway account per AWS
environment which means that each time you create a RestApi in your account the ApiGateway account
is overwritten. If at some point the newest RestApi is deleted, the ApiGateway Account and CloudWatch
role will also be deleted, breaking any existing ApiGateways that were depending on them.

When this flag is enabled you should either create the ApiGateway account and CloudWatch role
separately *or* only enable the cloudWatchRole on a single RestApi.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-apigateway:disableCloudWatchRole": true
  }
}
```

* `@aws-cdk/core:enablePartitionLiterals`

Enable this feature flag to have `Stack.partition` return a literal string for a stack's partition
when the stack has a known region configured.  If the region is undefined, or set to an unknown value, the
`Stack.partition` will be the CloudFormation intrinsic value `AWS::Partition`.  Without this feature flag,
`Stack.partition` always returns the CloudFormation intrinsic value `AWS::Partition`.

This feature will often simplify ARN strings in CDK generated templates, for example:

```yaml
 Principal:
   AWS:
     Fn::Join:
       - ""
       - - "arn:"
         - Ref: AWS::Partition
         - :iam::123456789876:root
```

becomes:

```yaml
 Principal:
   AWS: "arn:aws:iam::123456789876:root"
```

* `@aws-cdk/aws-ecs:disableExplicitDeploymentControllerForCircuitBreaker`

Enable this feature flag to avoid setting the "ECS" deployment controller when adding a circuit breaker to an
ECS Service, as this will trigger a full replacement which fails to deploy when using set service names.
This does not change any behaviour as the default deployment controller when it is not defined is ECS.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-ecs:disableExplicitDeploymentControllerForCircuitBreaker": true
  }
}
```

* `@aws-cdk/aws-s3:serverAccessLogsUseBucketPolicy`

Enable this feature flag to use S3 Bucket Policy for granting permission fo Server Access Logging
rather than using the canned `LogDeliveryWrite` ACL. ACLs do not work when Object Ownership is
enabled on the bucket.

This flag uses a Bucket Policy statement to allow Server Access Log delivery, following best
practices for S3.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html

```json
{
  "context": {
    "@aws-cdk/aws-s3:serverAccessLogsUseBucketPolicy": true
  }
}
```

* `@aws-cdk/aws-rds:databaseProxyUniqueResourceName`

Enable this feature flag to use unique resource names for each `DatabaseProxy`.

Previously, the default behavior for `DatabaseProxy` was to use `id` of the constructor for `dbProxyName`.
In this case, users couldn't deploy `DatabaseProxy`s that have the same `id` in the same region.

This is a feature flag as the old behavior was technically incorrect, but users may have come to depend on it.

```json
{
  "context": {
    "@aws-cdk/aws-rds:databaseProxyUniqueResourceName": true
  }
}
```

* `@aws-cdk/aws-redshift:columnId`

Enable this feature flag to allow the CDK to track changes in Redshift columns through their `id` attribute. This is a breaking change, as the `name` attribute was currently being used to track changes to Redshift columns.

Enabling this feature flag comes at a risk for existing Redshift columns, as the `name` attribute of a redshift column was currently being used. Therefore, to change a Redshift columns' `name` will essentially create a new column and delete the old one. This will cause data loss. If you choose to enable this flag, ensure that upon intial deployment (the first deployment after setting this feature flag), the `name` attribute of every column is not changed. After the intial deployment, you can freely change the `name` attribute of a column.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-redshift:columnId": true
  }
}
```

* `@aws-cdk/aws-stepfunctions-tasks:enableEmrServicePolicyV2`

Enable this feature flag to use the `AmazonEMRServicePolicy_v2` managed policies for the EMR service role.

This is a feature flag as the old behavior will be deprecated, but some resources may require manual
intervention since they might not have the appropriate tags propagated automatically.

https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-iam-policies.html

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-stepfunctions-tasks:enableEmrServicePolicyV2": true
  }
}
```

* `@aws-cdk/core:includePrefixInUniqueNameGeneration`

Enable this feature flag to include the stack's prefixes to the name generation process.

Not doing so can cause the name of stack to exceed 128 characters:

* The name generation ensures it doesn't exceed 128 characters
* Without this feature flag, the prefix is prepended to the generated name, which result can exceed 128 characters

This is a feature flag as it changes the name generated for stacks. Any CDK application deployed prior this fix will
most likely be generated with a new name, causing the stack to be recreated with the new name, and then deleting the old one.
For applications running on production environments this can be unmanageable.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/core:includePrefixInUniqueNameGeneration": true
  }
}
```

* `@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion`

Enable this feature flag to automatically use the latest available NodeJS version in the aws-lambda-nodejse.Function construct.

This allows creation of new functions using a version that will automatically stay up to date without breaking bundling of existing functions that externalize packages included in their environemnt such as `aws-sdk`.

Functions defined previously will continue to function correctly as long as they pass an explicit runtime version, or do not exclude packages during bundling.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion": true
  }
}
```

* `@aws-cdk/aws-codepipeline-actions:useNewDefaultBranchForCodeCommitSource`

Enable this feature flag to update the default branch for CodeCommit source actions to `main`.

Previously, the default branch for CodeCommit source actions was set to `master`.
However, this convention is no longer supported, and repositories created after March 2021 now have `main` as
their default branch.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-codepipeline-actions:useNewDefaultBranchForCodeCommitSource": true
  }
}
```

* `@aws-cdk/aws-cloudwatch-actions:changeLambdaPermissionLogicalIdForLambdaAction`

Enable this feature flag to change the logical ID of the `LambdaPermission` for the `LambdaAction` to include an alarm ID.

Previously, only one alarm with the `LambdaAction` could be created per Lambda.
This flag allows multiple alarms with the `LambdaAction` for the same Lambda to be created.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-cloudwatch-actions:changeLambdaPermissionLogicalIdForLambdaAction": true
  }
}
```

* `@aws-cdk/aws-codepipeline:crossAccountKeysDefaultValueToFalse`

Enables Pipeline to set the default value for `crossAccountKeys` to false.

When this feature flag is enabled, and the `crossAccountKeys` property is not provided in a `Pipeline`
construct, the construct automatically defaults the value of this property to false.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-codepipeline:crossAccountKeysDefaultValueToFalse": true
  }
}
```

* `@aws-cdk/aws-codepipeline:defaultPipelineTypeToV2`

Enables Pipeline to set the default pipeline type to V2.

When this feature flag is enabled, and the `pipelineType` property is not provided in a `Pipeline`
construct, the construct automatically defaults the value of this property to `PipelineType.V2`.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-codepipeline:defaultPipelineTypeToV2": true
  }
}
```

* `@aws-cdk/aws-kms:reduceCrossAccountRegionPolicyScope`

Reduce resource scope of the IAM Policy created from KMS key grant to granting key only.

When this feature flag is enabled and calling KMS key grant method, the created IAM policy will reduce the resource scope from
'*' to this specific granting KMS key.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-kms:reduceCrossAccountRegionPolicyScope": true
  }
}
```

* `@aws-cdk/aws-eks:nodegroupNameAttribute`

When enabled, nodegroupName attribute of the provisioned EKS NodeGroup will not have the cluster name prefix.

When this feature flag is enabled, the nodegroupName attribute will be exactly the name of the nodegroup
without any prefix.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-eks:nodegroupNameAttribute": true
  }
}
```

* `@aws-cdk/aws-ec2:ebsDefaultGp3Volume`

When enabled, the default volume type of the EBS volume will be GP3.

When this featuer flag is enabled, the default volume type of the EBS volume will be `EbsDeviceVolumeType.GENERAL_PURPOSE_SSD_GP3`

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-ec2:ebsDefaultGp3Volume": true
  }
}
```

* `@aws-cdk/aws-ecs:removeDefaultDeploymentAlarm`

When enabled, remove default deployment alarm settings.

When this featuer flag is enabled, remove the default deployment alarm settings when creating a AWS ECS service.

*cdk.json*

```json
{
  "context": {
    "@aws-cdk/aws-ec2:ebsDefaultGp3Volume": true
  }
}
```
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

from ..cloud_assembly_schema import (
    AmiContextQuery as _AmiContextQuery_74bf4b1b,
    ArtifactManifest as _ArtifactManifest_f79eef21,
    ArtifactType as _ArtifactType_1d870526,
    AssemblyManifest as _AssemblyManifest_413b9f23,
    AssetManifest as _AssetManifest_6cc3f0bc,
    AssetManifestProperties as _AssetManifestProperties_9084879a,
    AvailabilityZonesContextQuery as _AvailabilityZonesContextQuery_715a9fea,
    AwsCloudFormationStackProperties as _AwsCloudFormationStackProperties_50fb16af,
    BootstrapRole as _BootstrapRole_9b326056,
    ContainerImageAssetMetadataEntry as _ContainerImageAssetMetadataEntry_0a212d1d,
    ContextProvider as _ContextProvider_fa789bb5,
    EndpointServiceAvailabilityZonesContextQuery as _EndpointServiceAvailabilityZonesContextQuery_ea3ca0d1,
    FileAssetMetadataEntry as _FileAssetMetadataEntry_50173f8f,
    HostedZoneContextQuery as _HostedZoneContextQuery_8e6ca28f,
    KeyContextQuery as _KeyContextQuery_3ac6128d,
    LoadBalancerContextQuery as _LoadBalancerContextQuery_cb08d67c,
    LoadBalancerListenerContextQuery as _LoadBalancerListenerContextQuery_0eaf3c16,
    LoadManifestOptions as _LoadManifestOptions_56009fbd,
    MetadataEntry as _MetadataEntry_13e1bf79,
    MissingContext as _MissingContext_0ff9e334,
    NestedCloudAssemblyProperties as _NestedCloudAssemblyProperties_c2fa342d,
    PluginContextQuery as _PluginContextQuery_31a9d073,
    RuntimeInfo as _RuntimeInfo_3e9d9574,
    SSMParameterContextQuery as _SSMParameterContextQuery_675de122,
    SecurityGroupContextQuery as _SecurityGroupContextQuery_e772f3e6,
    Tag as _Tag_554dd7f9,
    TreeArtifactProperties as _TreeArtifactProperties_4092757e,
    VpcContextQuery as _VpcContextQuery_a193c650,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.AssemblyBuildOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class AssemblyBuildOptions:
    def __init__(self) -> None:
        '''
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            assembly_build_options = cx_api.AssemblyBuildOptions()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssemblyBuildOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.AwsCloudFormationStackProperties",
    jsii_struct_bases=[],
    name_mapping={
        "template_file": "templateFile",
        "parameters": "parameters",
        "stack_name": "stackName",
        "termination_protection": "terminationProtection",
    },
)
class AwsCloudFormationStackProperties:
    def __init__(
        self,
        *,
        template_file: builtins.str,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        stack_name: typing.Optional[builtins.str] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Artifact properties for CloudFormation stacks.

        :param template_file: A file relative to the assembly root which contains the CloudFormation template for this stack.
        :param parameters: Values for CloudFormation stack parameters that should be passed when the stack is deployed.
        :param stack_name: The name to use for the CloudFormation stack. Default: - name derived from artifact ID
        :param termination_protection: Whether to enable termination protection for this stack. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            aws_cloud_formation_stack_properties = cx_api.AwsCloudFormationStackProperties(
                template_file="templateFile",
            
                # the properties below are optional
                parameters={
                    "parameters_key": "parameters"
                },
                stack_name="stackName",
                termination_protection=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5c34615f91cec20ab023825c3decd0924a1d39d649c98c600cea970833ced2)
            check_type(argname="argument template_file", value=template_file, expected_type=type_hints["template_file"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_file": template_file,
        }
        if parameters is not None:
            self._values["parameters"] = parameters
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection

    @builtins.property
    def template_file(self) -> builtins.str:
        '''A file relative to the assembly root which contains the CloudFormation template for this stack.'''
        result = self._values.get("template_file")
        assert result is not None, "Required property 'template_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Values for CloudFormation stack parameters that should be passed when the stack is deployed.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the CloudFormation stack.

        :default: - name derived from artifact ID
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsCloudFormationStackProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudArtifact(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.CloudArtifact",
):
    '''Represents an artifact within a cloud assembly.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cloud_assembly_schema
        from aws_cdk import cx_api
        
        # cloud_assembly: cx_api.CloudAssembly
        
        cloud_artifact = cx_api.CloudArtifact.from_manifest(cloud_assembly, "MyCloudArtifact",
            type=cloud_assembly_schema.ArtifactType.NONE,
        
            # the properties below are optional
            dependencies=["dependencies"],
            display_name="displayName",
            environment="environment",
            metadata={
                "metadata_key": [cloud_assembly_schema.MetadataEntry(
                    type="type",
        
                    # the properties below are optional
                    data="data",
                    trace=["trace"]
                )]
            },
            properties=cloud_assembly_schema.AwsCloudFormationStackProperties(
                template_file="templateFile",
        
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                cloud_formation_execution_role_arn="cloudFormationExecutionRoleArn",
                lookup_role=cloud_assembly_schema.BootstrapRole(
                    arn="arn",
        
                    # the properties below are optional
                    assume_role_external_id="assumeRoleExternalId",
                    bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                    requires_bootstrap_stack_version=123
                ),
                parameters={
                    "parameters_key": "parameters"
                },
                requires_bootstrap_stack_version=123,
                stack_name="stackName",
                stack_template_asset_object_url="stackTemplateAssetObjectUrl",
                tags={
                    "tags_key": "tags"
                },
                termination_protection=False,
                validate_on_synth=False
            )
        )
    '''

    def __init__(
        self,
        assembly: "CloudAssembly",
        id: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param assembly: -
        :param id: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d9df0767e898e3c7d2743835aa9ce65467ceb2a717a448ad988e9d722408a1)
            check_type(argname="argument assembly", value=assembly, expected_type=type_hints["assembly"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        manifest = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        jsii.create(self.__class__, self, [assembly, id, manifest])

    @jsii.member(jsii_name="fromManifest")
    @builtins.classmethod
    def from_manifest(
        cls,
        assembly: "CloudAssembly",
        id: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> typing.Optional["CloudArtifact"]:
        '''Returns a subclass of ``CloudArtifact`` based on the artifact type defined in the artifact manifest.

        :param assembly: The cloud assembly from which to load the artifact.
        :param id: The artifact ID.
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        :return: the ``CloudArtifact`` that matches the artifact type or ``undefined`` if it's an artifact type that is unrecognized by this module.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a43b33c096c23def76559e7ae04cbbfebe9400c25a9d7ec0ac79410d9352d1ae)
            check_type(argname="argument assembly", value=assembly, expected_type=type_hints["assembly"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        artifact = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        return typing.cast(typing.Optional["CloudArtifact"], jsii.sinvoke(cls, "fromManifest", [assembly, id, artifact]))

    @jsii.member(jsii_name="findMetadataByType")
    def find_metadata_by_type(
        self,
        type: builtins.str,
    ) -> typing.List["MetadataEntryResult"]:
        '''
        :param type: -

        :return: all the metadata entries of a specific type in this artifact.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd3800ffb245fcadd6ec9780f43d13dc9f50e017d0c1cf6773cb5aa63830bca1)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        return typing.cast(typing.List["MetadataEntryResult"], jsii.invoke(self, "findMetadataByType", [type]))

    @builtins.property
    @jsii.member(jsii_name="assembly")
    def assembly(self) -> "CloudAssembly":
        return typing.cast("CloudAssembly", jsii.get(self, "assembly"))

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["CloudArtifact"]:
        '''Returns all the artifacts that this artifact depends on.'''
        return typing.cast(typing.List["CloudArtifact"], jsii.get(self, "dependencies"))

    @builtins.property
    @jsii.member(jsii_name="hierarchicalId")
    def hierarchical_id(self) -> builtins.str:
        '''An identifier that shows where this artifact is located in the tree of nested assemblies, based on their manifests.

        Defaults to the normal
        id. Should only be used in user interfaces.
        '''
        return typing.cast(builtins.str, jsii.get(self, "hierarchicalId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> _ArtifactManifest_f79eef21:
        '''The artifact's manifest.'''
        return typing.cast(_ArtifactManifest_f79eef21, jsii.get(self, "manifest"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(self) -> typing.List["SynthesisMessage"]:
        '''The set of messages extracted from the artifact's metadata.'''
        return typing.cast(typing.List["SynthesisMessage"], jsii.get(self, "messages"))


class CloudAssembly(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.CloudAssembly",
):
    '''Represents a deployable cloud application.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cx_api
        
        cloud_assembly = cx_api.CloudAssembly("directory",
            skip_enum_check=False,
            skip_version_check=False,
            topo_sort=False
        )
    '''

    def __init__(
        self,
        directory: builtins.str,
        *,
        skip_enum_check: typing.Optional[builtins.bool] = None,
        skip_version_check: typing.Optional[builtins.bool] = None,
        topo_sort: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Reads a cloud assembly from the specified directory.

        :param directory: The root directory of the assembly.
        :param skip_enum_check: Skip enum checks. This means you may read enum values you don't know about yet. Make sure to always check the values of enums you encounter in the manifest. Default: false
        :param skip_version_check: Skip the version check. This means you may read a newer cloud assembly than the CX API is designed to support, and your application may not be aware of all features that in use in the Cloud Assembly. Default: false
        :param topo_sort: Topologically sort all artifacts. This parameter is only respected by the constructor of ``CloudAssembly``. The property lives here for backwards compatibility reasons. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fddddcb2935767018d09ab9bba771c647da4dca6bcf2951acca71837d23ce0f2)
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
        load_options = _LoadManifestOptions_56009fbd(
            skip_enum_check=skip_enum_check,
            skip_version_check=skip_version_check,
            topo_sort=topo_sort,
        )

        jsii.create(self.__class__, self, [directory, load_options])

    @jsii.member(jsii_name="getNestedAssembly")
    def get_nested_assembly(self, artifact_id: builtins.str) -> "CloudAssembly":
        '''Returns a nested assembly.

        :param artifact_id: The artifact ID of the nested assembly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f303b13d87775fd1d362c0be6661fb685434df6fe5e86613a878ccc458c13c4a)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        return typing.cast("CloudAssembly", jsii.invoke(self, "getNestedAssembly", [artifact_id]))

    @jsii.member(jsii_name="getNestedAssemblyArtifact")
    def get_nested_assembly_artifact(
        self,
        artifact_id: builtins.str,
    ) -> "NestedCloudAssemblyArtifact":
        '''Returns a nested assembly artifact.

        :param artifact_id: The artifact ID of the nested assembly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca1be00ea6d5a6a3181e15cd3a7f56176d04c8f133fb678d50aac534642ef410)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        return typing.cast("NestedCloudAssemblyArtifact", jsii.invoke(self, "getNestedAssemblyArtifact", [artifact_id]))

    @jsii.member(jsii_name="getStackArtifact")
    def get_stack_artifact(
        self,
        artifact_id: builtins.str,
    ) -> "CloudFormationStackArtifact":
        '''Returns a CloudFormation stack artifact from this assembly.

        :param artifact_id: the artifact id of the stack (can be obtained through ``stack.artifactId``).

        :return: a ``CloudFormationStackArtifact`` object.

        :throws: if there is no stack artifact with that id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8fde0b2ca8fe6d68a7cd056ccfad10bf4236a83c0ac2d68ceff5eb735a15a1)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        return typing.cast("CloudFormationStackArtifact", jsii.invoke(self, "getStackArtifact", [artifact_id]))

    @jsii.member(jsii_name="getStackByName")
    def get_stack_by_name(
        self,
        stack_name: builtins.str,
    ) -> "CloudFormationStackArtifact":
        '''Returns a CloudFormation stack artifact from this assembly.

        Will only search the current assembly.

        :param stack_name: the name of the CloudFormation stack.

        :return: a ``CloudFormationStackArtifact`` object.

        :throws:

        if there is more than one stack with the same stack name. You can
        use ``getStackArtifact(stack.artifactId)`` instead.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b840a228aed1fef6a09c8ac443f560499b8b76163fcfca5f4fcdae412e7ce2ec)
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
        return typing.cast("CloudFormationStackArtifact", jsii.invoke(self, "getStackByName", [stack_name]))

    @jsii.member(jsii_name="tree")
    def tree(self) -> typing.Optional["TreeCloudArtifact"]:
        '''Returns the tree metadata artifact from this assembly.

        :return: a ``TreeCloudArtifact`` object if there is one defined in the manifest, ``undefined`` otherwise.

        :throws: if there is no metadata artifact by that name
        '''
        return typing.cast(typing.Optional["TreeCloudArtifact"], jsii.invoke(self, "tree", []))

    @jsii.member(jsii_name="tryGetArtifact")
    def try_get_artifact(self, id: builtins.str) -> typing.Optional[CloudArtifact]:
        '''Attempts to find an artifact with a specific identity.

        :param id: The artifact ID.

        :return: A ``CloudArtifact`` object or ``undefined`` if the artifact does not exist in this assembly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7c8acc8076027cc90b668ac3309172b04bcab88dfe6087bd99e1947e5f5824)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(typing.Optional[CloudArtifact], jsii.invoke(self, "tryGetArtifact", [id]))

    @builtins.property
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> typing.List[CloudArtifact]:
        '''All artifacts included in this assembly.'''
        return typing.cast(typing.List[CloudArtifact], jsii.get(self, "artifacts"))

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        '''The root directory of the cloud assembly.'''
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @builtins.property
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> _AssemblyManifest_413b9f23:
        '''The raw assembly manifest.'''
        return typing.cast(_AssemblyManifest_413b9f23, jsii.get(self, "manifest"))

    @builtins.property
    @jsii.member(jsii_name="nestedAssemblies")
    def nested_assemblies(self) -> typing.List["NestedCloudAssemblyArtifact"]:
        '''The nested assembly artifacts in this assembly.'''
        return typing.cast(typing.List["NestedCloudAssemblyArtifact"], jsii.get(self, "nestedAssemblies"))

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> _RuntimeInfo_3e9d9574:
        '''Runtime information such as module versions used to synthesize this assembly.'''
        return typing.cast(_RuntimeInfo_3e9d9574, jsii.get(self, "runtime"))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List["CloudFormationStackArtifact"]:
        '''
        :return: all the CloudFormation stack artifacts that are included in this assembly.
        '''
        return typing.cast(typing.List["CloudFormationStackArtifact"], jsii.get(self, "stacks"))

    @builtins.property
    @jsii.member(jsii_name="stacksRecursively")
    def stacks_recursively(self) -> typing.List["CloudFormationStackArtifact"]:
        '''Returns all the stacks, including the ones in nested assemblies.'''
        return typing.cast(typing.List["CloudFormationStackArtifact"], jsii.get(self, "stacksRecursively"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The schema version of the assembly manifest.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))


class CloudAssemblyBuilder(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.CloudAssemblyBuilder",
):
    '''Can be used to build a cloud assembly.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cx_api
        
        # cloud_assembly_builder_: cx_api.CloudAssemblyBuilder
        
        cloud_assembly_builder = cx_api.CloudAssemblyBuilder("outdir",
            asset_outdir="assetOutdir",
            parent_builder=cloud_assembly_builder_
        )
    '''

    def __init__(
        self,
        outdir: typing.Optional[builtins.str] = None,
        *,
        asset_outdir: typing.Optional[builtins.str] = None,
        parent_builder: typing.Optional["CloudAssemblyBuilder"] = None,
    ) -> None:
        '''Initializes a cloud assembly builder.

        :param outdir: The output directory, uses temporary directory if undefined.
        :param asset_outdir: Use the given asset output directory. Default: - Same as the manifest outdir
        :param parent_builder: If this builder is for a nested assembly, the parent assembly builder. Default: - This is a root assembly
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6a1363879dd2a5bcc5f520c0f431ae7555bcd85bdb9c732ec6bb62af4c7f5b)
            check_type(argname="argument outdir", value=outdir, expected_type=type_hints["outdir"])
        props = CloudAssemblyBuilderProps(
            asset_outdir=asset_outdir, parent_builder=parent_builder
        )

        jsii.create(self.__class__, self, [outdir, props])

    @jsii.member(jsii_name="addArtifact")
    def add_artifact(
        self,
        id: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Adds an artifact into the cloud assembly.

        :param id: The ID of the artifact.
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__261d018bdb1dc9a71bf2eedbb2cef096556840e4a312cda97d52542715b7bddc)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        manifest = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "addArtifact", [id, manifest]))

    @jsii.member(jsii_name="addMissing")
    def add_missing(
        self,
        *,
        key: builtins.str,
        props: typing.Union[typing.Union[_AmiContextQuery_74bf4b1b, typing.Dict[builtins.str, typing.Any]], typing.Union[_AvailabilityZonesContextQuery_715a9fea, typing.Dict[builtins.str, typing.Any]], typing.Union[_HostedZoneContextQuery_8e6ca28f, typing.Dict[builtins.str, typing.Any]], typing.Union[_SSMParameterContextQuery_675de122, typing.Dict[builtins.str, typing.Any]], typing.Union[_VpcContextQuery_a193c650, typing.Dict[builtins.str, typing.Any]], typing.Union[_EndpointServiceAvailabilityZonesContextQuery_ea3ca0d1, typing.Dict[builtins.str, typing.Any]], typing.Union[_LoadBalancerContextQuery_cb08d67c, typing.Dict[builtins.str, typing.Any]], typing.Union[_LoadBalancerListenerContextQuery_0eaf3c16, typing.Dict[builtins.str, typing.Any]], typing.Union[_SecurityGroupContextQuery_e772f3e6, typing.Dict[builtins.str, typing.Any]], typing.Union[_KeyContextQuery_3ac6128d, typing.Dict[builtins.str, typing.Any]], typing.Union[_PluginContextQuery_31a9d073, typing.Dict[builtins.str, typing.Any]]],
        provider: _ContextProvider_fa789bb5,
    ) -> None:
        '''Reports that some context is missing in order for this cloud assembly to be fully synthesized.

        :param key: The missing context key.
        :param props: A set of provider-specific options.
        :param provider: The provider from which we expect this context key to be obtained.
        '''
        missing = _MissingContext_0ff9e334(key=key, props=props, provider=provider)

        return typing.cast(None, jsii.invoke(self, "addMissing", [missing]))

    @jsii.member(jsii_name="buildAssembly")
    def build_assembly(self) -> CloudAssembly:
        '''Finalizes the cloud assembly into the output directory returns a ``CloudAssembly`` object that can be used to inspect the assembly.'''
        options = AssemblyBuildOptions()

        return typing.cast(CloudAssembly, jsii.invoke(self, "buildAssembly", [options]))

    @jsii.member(jsii_name="createNestedAssembly")
    def create_nested_assembly(
        self,
        artifact_id: builtins.str,
        display_name: builtins.str,
    ) -> "CloudAssemblyBuilder":
        '''Creates a nested cloud assembly.

        :param artifact_id: -
        :param display_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e63712a9b3643ce667b29b1f646c53fbff128df67c060f5e9a1f8cd350a0354)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
        return typing.cast("CloudAssemblyBuilder", jsii.invoke(self, "createNestedAssembly", [artifact_id, display_name]))

    @jsii.member(jsii_name="delete")
    def delete(self) -> None:
        '''Delete the cloud assembly directory.'''
        return typing.cast(None, jsii.invoke(self, "delete", []))

    @builtins.property
    @jsii.member(jsii_name="assetOutdir")
    def asset_outdir(self) -> builtins.str:
        '''The directory where assets of this Cloud Assembly should be stored.'''
        return typing.cast(builtins.str, jsii.get(self, "assetOutdir"))

    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''The root directory of the resulting cloud assembly.'''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.CloudAssemblyBuilderProps",
    jsii_struct_bases=[],
    name_mapping={"asset_outdir": "assetOutdir", "parent_builder": "parentBuilder"},
)
class CloudAssemblyBuilderProps:
    def __init__(
        self,
        *,
        asset_outdir: typing.Optional[builtins.str] = None,
        parent_builder: typing.Optional[CloudAssemblyBuilder] = None,
    ) -> None:
        '''Construction properties for CloudAssemblyBuilder.

        :param asset_outdir: Use the given asset output directory. Default: - Same as the manifest outdir
        :param parent_builder: If this builder is for a nested assembly, the parent assembly builder. Default: - This is a root assembly

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            # cloud_assembly_builder: cx_api.CloudAssemblyBuilder
            
            cloud_assembly_builder_props = cx_api.CloudAssemblyBuilderProps(
                asset_outdir="assetOutdir",
                parent_builder=cloud_assembly_builder
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cf08d1d4732cadcfbad0197fedaa9b4ea676984caad92dcdf90c09904e0faa5)
            check_type(argname="argument asset_outdir", value=asset_outdir, expected_type=type_hints["asset_outdir"])
            check_type(argname="argument parent_builder", value=parent_builder, expected_type=type_hints["parent_builder"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if asset_outdir is not None:
            self._values["asset_outdir"] = asset_outdir
        if parent_builder is not None:
            self._values["parent_builder"] = parent_builder

    @builtins.property
    def asset_outdir(self) -> typing.Optional[builtins.str]:
        '''Use the given asset output directory.

        :default: - Same as the manifest outdir
        '''
        result = self._values.get("asset_outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_builder(self) -> typing.Optional[CloudAssemblyBuilder]:
        '''If this builder is for a nested assembly, the parent assembly builder.

        :default: - This is a root assembly
        '''
        result = self._values.get("parent_builder")
        return typing.cast(typing.Optional[CloudAssemblyBuilder], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAssemblyBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationStackArtifact(
    CloudArtifact,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.CloudFormationStackArtifact",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cloud_assembly_schema
        from aws_cdk import cx_api
        
        # cloud_assembly: cx_api.CloudAssembly
        
        cloud_formation_stack_artifact = cx_api.CloudFormationStackArtifact(cloud_assembly, "artifactId",
            type=cloud_assembly_schema.ArtifactType.NONE,
        
            # the properties below are optional
            dependencies=["dependencies"],
            display_name="displayName",
            environment="environment",
            metadata={
                "metadata_key": [cloud_assembly_schema.MetadataEntry(
                    type="type",
        
                    # the properties below are optional
                    data="data",
                    trace=["trace"]
                )]
            },
            properties=cloud_assembly_schema.AwsCloudFormationStackProperties(
                template_file="templateFile",
        
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                cloud_formation_execution_role_arn="cloudFormationExecutionRoleArn",
                lookup_role=cloud_assembly_schema.BootstrapRole(
                    arn="arn",
        
                    # the properties below are optional
                    assume_role_external_id="assumeRoleExternalId",
                    bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                    requires_bootstrap_stack_version=123
                ),
                parameters={
                    "parameters_key": "parameters"
                },
                requires_bootstrap_stack_version=123,
                stack_name="stackName",
                stack_template_asset_object_url="stackTemplateAssetObjectUrl",
                tags={
                    "tags_key": "tags"
                },
                termination_protection=False,
                validate_on_synth=False
            )
        )
    '''

    def __init__(
        self,
        assembly: CloudAssembly,
        artifact_id: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param assembly: -
        :param artifact_id: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efbcfecbcc773b1f90d568df2c82e4e67168ad418a9cd97880b975d214994119)
            check_type(argname="argument assembly", value=assembly, expected_type=type_hints["assembly"])
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        artifact = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        jsii.create(self.__class__, self, [assembly, artifact_id, artifact])

    @jsii.member(jsii_name="isCloudFormationStackArtifact")
    @builtins.classmethod
    def is_cloud_formation_stack_artifact(cls, art: typing.Any) -> builtins.bool:
        '''Checks if ``art`` is an instance of this class.

        Use this method instead of ``instanceof`` to properly detect ``CloudFormationStackArtifact``
        instances, even when the construct library is symlinked.

        Explanation: in JavaScript, multiple copies of the ``cx-api`` library on
        disk are seen as independent, completely different libraries. As a
        consequence, the class ``CloudFormationStackArtifact`` in each copy of the ``cx-api`` library
        is seen as a different class, and an instance of one class will not test as
        ``instanceof`` the other class. ``npm install`` will not create installations
        like this, but users may manually symlink construct libraries together or
        use a monorepo tool: in those cases, multiple copies of the ``cx-api``
        library can be accidentally installed, and ``instanceof`` will behave
        unpredictably. It is safest to avoid using ``instanceof``, and using
        this type-testing method instead.

        :param art: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b66444028144603e6b05b0b8247226ffeb9078622ddf73bd9d540b8ce722630)
            check_type(argname="argument art", value=art, expected_type=type_hints["art"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCloudFormationStackArtifact", [art]))

    @builtins.property
    @jsii.member(jsii_name="assets")
    def assets(
        self,
    ) -> typing.List[typing.Union[_FileAssetMetadataEntry_50173f8f, _ContainerImageAssetMetadataEntry_0a212d1d]]:
        '''Any assets associated with this stack.'''
        return typing.cast(typing.List[typing.Union[_FileAssetMetadataEntry_50173f8f, _ContainerImageAssetMetadataEntry_0a212d1d]], jsii.get(self, "assets"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''A string that represents this stack.

        Should only be used in user
        interfaces. If the stackName has not been set explicitly, or has been set
        to artifactId, it will return the hierarchicalId of the stack. Otherwise,
        it will return something like " ()"
        '''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> "Environment":
        '''The environment into which to deploy this artifact.'''
        return typing.cast("Environment", jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="originalName")
    def original_name(self) -> builtins.str:
        '''The original name as defined in the CDK app.'''
        return typing.cast(builtins.str, jsii.get(self, "originalName"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''CloudFormation parameters to pass to the stack.'''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''The physical name of this stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''CloudFormation tags to pass to the stack.'''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> typing.Any:
        '''The CloudFormation template for this stack.'''
        return typing.cast(typing.Any, jsii.get(self, "template"))

    @builtins.property
    @jsii.member(jsii_name="templateFile")
    def template_file(self) -> builtins.str:
        '''The file name of the template.'''
        return typing.cast(builtins.str, jsii.get(self, "templateFile"))

    @builtins.property
    @jsii.member(jsii_name="templateFullPath")
    def template_full_path(self) -> builtins.str:
        '''Full path to the template file.'''
        return typing.cast(builtins.str, jsii.get(self, "templateFullPath"))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleArn")
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that needs to be assumed to deploy the stack.

        :default: - No role is assumed (current credentials are used)
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assumeRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleExternalId")
    def assume_role_external_id(self) -> typing.Optional[builtins.str]:
        '''External ID to use when assuming role for cloudformation deployments.

        :default: - No external ID
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assumeRoleExternalId"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapStackVersionSsmParameter")
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''Name of SSM parameter with bootstrap stack version.

        :default: - Discover SSM parameter by reading stack
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootstrapStackVersionSsmParameter"))

    @builtins.property
    @jsii.member(jsii_name="cloudFormationExecutionRoleArn")
    def cloud_formation_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that is passed to CloudFormation to execute the change set.

        :default: - No role is passed (currently assumed role/credentials are used)
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudFormationExecutionRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="lookupRole")
    def lookup_role(self) -> typing.Optional[_BootstrapRole_9b326056]:
        '''The role to use to look up values from the target AWS account.

        :default: - No role is assumed (current credentials are used)
        '''
        return typing.cast(typing.Optional[_BootstrapRole_9b326056], jsii.get(self, "lookupRole"))

    @builtins.property
    @jsii.member(jsii_name="requiresBootstrapStackVersion")
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to deploy this stack.

        :default: - No bootstrap stack required
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requiresBootstrapStackVersion"))

    @builtins.property
    @jsii.member(jsii_name="stackTemplateAssetObjectUrl")
    def stack_template_asset_object_url(self) -> typing.Optional[builtins.str]:
        '''If the stack template has already been included in the asset manifest, its asset URL.

        :default: - Not uploaded yet, upload just before deploying
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stackTemplateAssetObjectUrl"))

    @builtins.property
    @jsii.member(jsii_name="terminationProtection")
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether termination protection is enabled for this stack.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "terminationProtection"))

    @builtins.property
    @jsii.member(jsii_name="validateOnSynth")
    def validate_on_synth(self) -> typing.Optional[builtins.bool]:
        '''Whether this stack should be validated by the CLI after synthesis.

        :default: - false
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "validateOnSynth"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.EndpointServiceAvailabilityZonesContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "region": "region",
        "service_name": "serviceName",
    },
)
class EndpointServiceAvailabilityZonesContextQuery:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query to hosted zone context provider.

        :param account: Query account.
        :param region: Query region.
        :param service_name: Query service name.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            endpoint_service_availability_zones_context_query = cx_api.EndpointServiceAvailabilityZonesContextQuery(
                account="account",
                region="region",
                service_name="serviceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18b8b66b1c10428da0ac775df90fa02d4536a3abf32809fd4aa5613c7b749708)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if region is not None:
            self._values["region"] = region
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Query account.'''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Query region.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Query service name.'''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointServiceAvailabilityZonesContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.Environment",
    jsii_struct_bases=[],
    name_mapping={"account": "account", "name": "name", "region": "region"},
)
class Environment:
    def __init__(
        self,
        *,
        account: builtins.str,
        name: builtins.str,
        region: builtins.str,
    ) -> None:
        '''Models an AWS execution environment, for use within the CDK toolkit.

        :param account: The AWS account this environment deploys into.
        :param name: The arbitrary name of this environment (user-set, or at least user-meaningful).
        :param region: The AWS region name where this environment deploys into.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            environment = cx_api.Environment(
                account="account",
                name="name",
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b89ece71f0626cb86a981885eb005d80d37b76239395b1fb770f98af0feb287)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "name": name,
            "region": region,
        }

    @builtins.property
    def account(self) -> builtins.str:
        '''The AWS account this environment deploys into.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The arbitrary name of this environment (user-set, or at least user-meaningful).'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The AWS region name where this environment deploys into.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Environment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.EnvironmentPlaceholderValues",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "partition": "partition",
        "region": "region",
    },
)
class EnvironmentPlaceholderValues:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        partition: builtins.str,
        region: builtins.str,
    ) -> None:
        '''Return the appropriate values for the environment placeholders.

        :param account_id: Return the account.
        :param partition: Return the partition.
        :param region: Return the region.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            environment_placeholder_values = cx_api.EnvironmentPlaceholderValues(
                account_id="accountId",
                partition="partition",
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed6e19535466d26cdb82f05ca1d5f232f037fa0049d12f75cf29ad817a5d7f32)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "partition": partition,
            "region": region,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Return the account.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition(self) -> builtins.str:
        '''Return the partition.'''
        result = self._values.get("partition")
        assert result is not None, "Required property 'partition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Return the region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentPlaceholderValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvironmentPlaceholders(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.EnvironmentPlaceholders",
):
    '''Placeholders which can be used manifests.

    These can occur both in the Asset Manifest as well as the general
    Cloud Assembly manifest.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cx_api
        
        environment_placeholders = cx_api.EnvironmentPlaceholders()
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="replace")
    @builtins.classmethod
    def replace(
        cls,
        object: typing.Any,
        *,
        account_id: builtins.str,
        partition: builtins.str,
        region: builtins.str,
    ) -> typing.Any:
        '''Replace the environment placeholders in all strings found in a complex object.

        Duplicated between cdk-assets and aws-cdk CLI because we don't have a good single place to put it
        (they're nominally independent tools).

        :param object: -
        :param account_id: Return the account.
        :param partition: Return the partition.
        :param region: Return the region.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c501acc043bc39a8bac96f39d791a6247df0ff4b85022293cf10a9e35c2cbf)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        values = EnvironmentPlaceholderValues(
            account_id=account_id, partition=partition, region=region
        )

        return typing.cast(typing.Any, jsii.sinvoke(cls, "replace", [object, values]))

    @jsii.member(jsii_name="replaceAsync")
    @builtins.classmethod
    def replace_async(
        cls,
        object: typing.Any,
        provider: "IEnvironmentPlaceholderProvider",
    ) -> typing.Any:
        '''Like 'replace', but asynchronous.

        :param object: -
        :param provider: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1afabc7b5a7558dae687aa1b5d2443a52cc7b5f0e6aab01ccd7c06217f2346d)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "replaceAsync", [object, provider]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CURRENT_ACCOUNT")
    def CURRENT_ACCOUNT(cls) -> builtins.str:
        '''Insert this into the destination fields to be replaced with the current account.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CURRENT_ACCOUNT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CURRENT_PARTITION")
    def CURRENT_PARTITION(cls) -> builtins.str:
        '''Insert this into the destination fields to be replaced with the current partition.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CURRENT_PARTITION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CURRENT_REGION")
    def CURRENT_REGION(cls) -> builtins.str:
        '''Insert this into the destination fields to be replaced with the current region.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CURRENT_REGION"))


class EnvironmentUtils(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.EnvironmentUtils",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cx_api
        
        environment_utils = cx_api.EnvironmentUtils()
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="format")
    @builtins.classmethod
    def format(cls, account: builtins.str, region: builtins.str) -> builtins.str:
        '''Format an environment string from an account and region.

        :param account: -
        :param region: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0ab540cd47ccd18967a60dbc22dd525d173430ed5fd87a09975a27c1b4a1e40)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "format", [account, region]))

    @jsii.member(jsii_name="make")
    @builtins.classmethod
    def make(cls, account: builtins.str, region: builtins.str) -> Environment:
        '''Build an environment object from an account and region.

        :param account: -
        :param region: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc28e540849733b49f0e7ba0129dc101535f53a2636a768cad3fa3ebe9ee5dbf)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        return typing.cast(Environment, jsii.sinvoke(cls, "make", [account, region]))

    @jsii.member(jsii_name="parse")
    @builtins.classmethod
    def parse(cls, environment: builtins.str) -> Environment:
        '''
        :param environment: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b352e789835b9c9e77225861068bcffa327be4b34b87310b0ac375b17023fb)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
        return typing.cast(Environment, jsii.sinvoke(cls, "parse", [environment]))


@jsii.interface(jsii_type="aws-cdk-lib.cx_api.IEnvironmentPlaceholderProvider")
class IEnvironmentPlaceholderProvider(typing_extensions.Protocol):
    '''Return the appropriate values for the environment placeholders.'''

    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''Return the account.'''
        ...

    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        '''Return the partition.'''
        ...

    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        '''Return the region.'''
        ...


class _IEnvironmentPlaceholderProviderProxy:
    '''Return the appropriate values for the environment placeholders.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.cx_api.IEnvironmentPlaceholderProvider"

    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''Return the account.'''
        return typing.cast(builtins.str, jsii.invoke(self, "accountId", []))

    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        '''Return the partition.'''
        return typing.cast(builtins.str, jsii.invoke(self, "partition", []))

    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        '''Return the region.'''
        return typing.cast(builtins.str, jsii.invoke(self, "region", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentPlaceholderProvider).__jsii_proxy_class__ = lambda : _IEnvironmentPlaceholderProviderProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.KeyContextResponse",
    jsii_struct_bases=[],
    name_mapping={"key_id": "keyId"},
)
class KeyContextResponse:
    def __init__(self, *, key_id: builtins.str) -> None:
        '''Properties of a discovered key.

        :param key_id: Id of the key.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            key_context_response = cx_api.KeyContextResponse(
                key_id="keyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f13cf02baa9a996348503c81bdcb5503ad573a31d58b8846bc221099cffd660)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_id": key_id,
        }

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Id of the key.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyContextResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.LoadBalancerContextResponse",
    jsii_struct_bases=[],
    name_mapping={
        "ip_address_type": "ipAddressType",
        "load_balancer_arn": "loadBalancerArn",
        "load_balancer_canonical_hosted_zone_id": "loadBalancerCanonicalHostedZoneId",
        "load_balancer_dns_name": "loadBalancerDnsName",
        "security_group_ids": "securityGroupIds",
        "vpc_id": "vpcId",
    },
)
class LoadBalancerContextResponse:
    def __init__(
        self,
        *,
        ip_address_type: "LoadBalancerIpAddressType",
        load_balancer_arn: builtins.str,
        load_balancer_canonical_hosted_zone_id: builtins.str,
        load_balancer_dns_name: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''Properties of a discovered load balancer.

        :param ip_address_type: Type of IP address.
        :param load_balancer_arn: The ARN of the load balancer.
        :param load_balancer_canonical_hosted_zone_id: The hosted zone ID of the load balancer's name.
        :param load_balancer_dns_name: Load balancer's DNS name.
        :param security_group_ids: Load balancer's security groups.
        :param vpc_id: Load balancer's VPC.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            load_balancer_context_response = cx_api.LoadBalancerContextResponse(
                ip_address_type=cx_api.LoadBalancerIpAddressType.IPV4,
                load_balancer_arn="loadBalancerArn",
                load_balancer_canonical_hosted_zone_id="loadBalancerCanonicalHostedZoneId",
                load_balancer_dns_name="loadBalancerDnsName",
                security_group_ids=["securityGroupIds"],
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac79c3d47933ad7a274fcd1507b7e94ece2bc4338505867e28ea64343cdbe0d)
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument load_balancer_arn", value=load_balancer_arn, expected_type=type_hints["load_balancer_arn"])
            check_type(argname="argument load_balancer_canonical_hosted_zone_id", value=load_balancer_canonical_hosted_zone_id, expected_type=type_hints["load_balancer_canonical_hosted_zone_id"])
            check_type(argname="argument load_balancer_dns_name", value=load_balancer_dns_name, expected_type=type_hints["load_balancer_dns_name"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_address_type": ip_address_type,
            "load_balancer_arn": load_balancer_arn,
            "load_balancer_canonical_hosted_zone_id": load_balancer_canonical_hosted_zone_id,
            "load_balancer_dns_name": load_balancer_dns_name,
            "security_group_ids": security_group_ids,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def ip_address_type(self) -> "LoadBalancerIpAddressType":
        '''Type of IP address.'''
        result = self._values.get("ip_address_type")
        assert result is not None, "Required property 'ip_address_type' is missing"
        return typing.cast("LoadBalancerIpAddressType", result)

    @builtins.property
    def load_balancer_arn(self) -> builtins.str:
        '''The ARN of the load balancer.'''
        result = self._values.get("load_balancer_arn")
        assert result is not None, "Required property 'load_balancer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_canonical_hosted_zone_id(self) -> builtins.str:
        '''The hosted zone ID of the load balancer's name.'''
        result = self._values.get("load_balancer_canonical_hosted_zone_id")
        assert result is not None, "Required property 'load_balancer_canonical_hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_dns_name(self) -> builtins.str:
        '''Load balancer's DNS name.'''
        result = self._values.get("load_balancer_dns_name")
        assert result is not None, "Required property 'load_balancer_dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Load balancer's security groups.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Load balancer's VPC.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerContextResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cx_api.LoadBalancerIpAddressType")
class LoadBalancerIpAddressType(enum.Enum):
    '''Load balancer ip address type.'''

    IPV4 = "IPV4"
    '''IPV4 ip address.'''
    DUAL_STACK = "DUAL_STACK"
    '''Dual stack address.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.LoadBalancerListenerContextResponse",
    jsii_struct_bases=[],
    name_mapping={
        "listener_arn": "listenerArn",
        "listener_port": "listenerPort",
        "security_group_ids": "securityGroupIds",
    },
)
class LoadBalancerListenerContextResponse:
    def __init__(
        self,
        *,
        listener_arn: builtins.str,
        listener_port: jsii.Number,
        security_group_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''Properties of a discovered load balancer listener.

        :param listener_arn: The ARN of the listener.
        :param listener_port: The port the listener is listening on.
        :param security_group_ids: The security groups of the load balancer.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            load_balancer_listener_context_response = cx_api.LoadBalancerListenerContextResponse(
                listener_arn="listenerArn",
                listener_port=123,
                security_group_ids=["securityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a91c0cb0c6c1935935039ee08853827eb62ce0b9747a7e1792fe0e444a64bd1)
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
            check_type(argname="argument listener_port", value=listener_port, expected_type=type_hints["listener_port"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_arn": listener_arn,
            "listener_port": listener_port,
            "security_group_ids": security_group_ids,
        }

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''The ARN of the listener.'''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_port(self) -> jsii.Number:
        '''The port the listener is listening on.'''
        result = self._values.get("listener_port")
        assert result is not None, "Required property 'listener_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The security groups of the load balancer.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerListenerContextResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.MetadataEntryResult",
    jsii_struct_bases=[_MetadataEntry_13e1bf79],
    name_mapping={"type": "type", "data": "data", "trace": "trace", "path": "path"},
)
class MetadataEntryResult(_MetadataEntry_13e1bf79):
    def __init__(
        self,
        *,
        type: builtins.str,
        data: typing.Optional[typing.Union[builtins.str, typing.Union[_FileAssetMetadataEntry_50173f8f, typing.Dict[builtins.str, typing.Any]], typing.Union[_ContainerImageAssetMetadataEntry_0a212d1d, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[_Tag_554dd7f9, typing.Dict[builtins.str, typing.Any]]]]] = None,
        trace: typing.Optional[typing.Sequence[builtins.str]] = None,
        path: builtins.str,
    ) -> None:
        '''
        :param type: The type of the metadata entry.
        :param data: The data. Default: - no data.
        :param trace: A stack trace for when the entry was created. Default: - no trace.
        :param path: The path in which this entry was defined.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            metadata_entry_result = cx_api.MetadataEntryResult(
                path="path",
                type="type",
            
                # the properties below are optional
                data="data",
                trace=["trace"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb7cda500898c592440fb240140921316008dc94a4ac6385c5fe171bac93252)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "path": path,
        }
        if data is not None:
            self._values["data"] = data
        if trace is not None:
            self._values["trace"] = trace

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the metadata entry.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _FileAssetMetadataEntry_50173f8f, _ContainerImageAssetMetadataEntry_0a212d1d, typing.List[_Tag_554dd7f9]]]:
        '''The data.

        :default: - no data.
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _FileAssetMetadataEntry_50173f8f, _ContainerImageAssetMetadataEntry_0a212d1d, typing.List[_Tag_554dd7f9]]], result)

    @builtins.property
    def trace(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A stack trace for when the entry was created.

        :default: - no trace.
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The path in which this entry was defined.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetadataEntryResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NestedCloudAssemblyArtifact(
    CloudArtifact,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.NestedCloudAssemblyArtifact",
):
    '''Asset manifest is a description of a set of assets which need to be built and published.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cloud_assembly_schema
        from aws_cdk import cx_api
        
        # cloud_assembly: cx_api.CloudAssembly
        
        nested_cloud_assembly_artifact = cx_api.NestedCloudAssemblyArtifact(cloud_assembly, "name",
            type=cloud_assembly_schema.ArtifactType.NONE,
        
            # the properties below are optional
            dependencies=["dependencies"],
            display_name="displayName",
            environment="environment",
            metadata={
                "metadata_key": [cloud_assembly_schema.MetadataEntry(
                    type="type",
        
                    # the properties below are optional
                    data="data",
                    trace=["trace"]
                )]
            },
            properties=cloud_assembly_schema.AwsCloudFormationStackProperties(
                template_file="templateFile",
        
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                cloud_formation_execution_role_arn="cloudFormationExecutionRoleArn",
                lookup_role=cloud_assembly_schema.BootstrapRole(
                    arn="arn",
        
                    # the properties below are optional
                    assume_role_external_id="assumeRoleExternalId",
                    bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                    requires_bootstrap_stack_version=123
                ),
                parameters={
                    "parameters_key": "parameters"
                },
                requires_bootstrap_stack_version=123,
                stack_name="stackName",
                stack_template_asset_object_url="stackTemplateAssetObjectUrl",
                tags={
                    "tags_key": "tags"
                },
                termination_protection=False,
                validate_on_synth=False
            )
        )
    '''

    def __init__(
        self,
        assembly: CloudAssembly,
        name: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param assembly: -
        :param name: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58cd751fc0676bdece56072cebc370619182e12e08433ef6415db29d47ea7fb4)
            check_type(argname="argument assembly", value=assembly, expected_type=type_hints["assembly"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        artifact = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        jsii.create(self.__class__, self, [assembly, name, artifact])

    @jsii.member(jsii_name="isNestedCloudAssemblyArtifact")
    @builtins.classmethod
    def is_nested_cloud_assembly_artifact(cls, art: typing.Any) -> builtins.bool:
        '''Checks if ``art`` is an instance of this class.

        Use this method instead of ``instanceof`` to properly detect ``NestedCloudAssemblyArtifact``
        instances, even when the construct library is symlinked.

        Explanation: in JavaScript, multiple copies of the ``cx-api`` library on
        disk are seen as independent, completely different libraries. As a
        consequence, the class ``NestedCloudAssemblyArtifact`` in each copy of the ``cx-api`` library
        is seen as a different class, and an instance of one class will not test as
        ``instanceof`` the other class. ``npm install`` will not create installations
        like this, but users may manually symlink construct libraries together or
        use a monorepo tool: in those cases, multiple copies of the ``cx-api``
        library can be accidentally installed, and ``instanceof`` will behave
        unpredictably. It is safest to avoid using ``instanceof``, and using
        this type-testing method instead.

        :param art: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a2e95d592babe551ba1095814395519ee8ddb44b75386590a67acad58e21be)
            check_type(argname="argument art", value=art, expected_type=type_hints["art"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isNestedCloudAssemblyArtifact", [art]))

    @builtins.property
    @jsii.member(jsii_name="directoryName")
    def directory_name(self) -> builtins.str:
        '''The relative directory name of the asset manifest.'''
        return typing.cast(builtins.str, jsii.get(self, "directoryName"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''Display name.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="fullPath")
    def full_path(self) -> builtins.str:
        '''Full path to the nested assembly directory.'''
        return typing.cast(builtins.str, jsii.get(self, "fullPath"))

    @builtins.property
    @jsii.member(jsii_name="nestedAssembly")
    def nested_assembly(self) -> CloudAssembly:
        '''The nested Assembly.'''
        return typing.cast(CloudAssembly, jsii.get(self, "nestedAssembly"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.SecurityGroupContextResponse",
    jsii_struct_bases=[],
    name_mapping={
        "allow_all_outbound": "allowAllOutbound",
        "security_group_id": "securityGroupId",
    },
)
class SecurityGroupContextResponse:
    def __init__(
        self,
        *,
        allow_all_outbound: builtins.bool,
        security_group_id: builtins.str,
    ) -> None:
        '''Properties of a discovered SecurityGroup.

        :param allow_all_outbound: Whether the security group allows all outbound traffic. This will be true when the security group has all-protocol egress permissions to access both ``0.0.0.0/0`` and ``::/0``.
        :param security_group_id: The security group's id.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            security_group_context_response = cx_api.SecurityGroupContextResponse(
                allow_all_outbound=False,
                security_group_id="securityGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f30736a8fbf7f3faa6b49be9a48d529ff37ecf26b24a4bae9cb6821dbe8bdc)
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allow_all_outbound": allow_all_outbound,
            "security_group_id": security_group_id,
        }

    @builtins.property
    def allow_all_outbound(self) -> builtins.bool:
        '''Whether the security group allows all outbound traffic.

        This will be true
        when the security group has all-protocol egress permissions to access both
        ``0.0.0.0/0`` and ``::/0``.
        '''
        result = self._values.get("allow_all_outbound")
        assert result is not None, "Required property 'allow_all_outbound' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''The security group's id.'''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupContextResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.SynthesisMessage",
    jsii_struct_bases=[],
    name_mapping={"entry": "entry", "id": "id", "level": "level"},
)
class SynthesisMessage:
    def __init__(
        self,
        *,
        entry: typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]],
        id: builtins.str,
        level: "SynthesisMessageLevel",
    ) -> None:
        '''
        :param entry: 
        :param id: 
        :param level: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            synthesis_message = cx_api.SynthesisMessage(
                entry=MetadataEntry(
                    type="type",
            
                    # the properties below are optional
                    data="data",
                    trace=["trace"]
                ),
                id="id",
                level=cx_api.SynthesisMessageLevel.INFO
            )
        '''
        if isinstance(entry, dict):
            entry = _MetadataEntry_13e1bf79(**entry)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29937f9afd429e77cb3104d8535016507a83d9824ac8c4c46469e321925a6d3e)
            check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entry": entry,
            "id": id,
            "level": level,
        }

    @builtins.property
    def entry(self) -> _MetadataEntry_13e1bf79:
        result = self._values.get("entry")
        assert result is not None, "Required property 'entry' is missing"
        return typing.cast(_MetadataEntry_13e1bf79, result)

    @builtins.property
    def id(self) -> builtins.str:
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def level(self) -> "SynthesisMessageLevel":
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast("SynthesisMessageLevel", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynthesisMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cx_api.SynthesisMessageLevel")
class SynthesisMessageLevel(enum.Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class TreeCloudArtifact(
    CloudArtifact,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.TreeCloudArtifact",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cloud_assembly_schema
        from aws_cdk import cx_api
        
        # cloud_assembly: cx_api.CloudAssembly
        
        tree_cloud_artifact = cx_api.TreeCloudArtifact(cloud_assembly, "name",
            type=cloud_assembly_schema.ArtifactType.NONE,
        
            # the properties below are optional
            dependencies=["dependencies"],
            display_name="displayName",
            environment="environment",
            metadata={
                "metadata_key": [cloud_assembly_schema.MetadataEntry(
                    type="type",
        
                    # the properties below are optional
                    data="data",
                    trace=["trace"]
                )]
            },
            properties=cloud_assembly_schema.AwsCloudFormationStackProperties(
                template_file="templateFile",
        
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                cloud_formation_execution_role_arn="cloudFormationExecutionRoleArn",
                lookup_role=cloud_assembly_schema.BootstrapRole(
                    arn="arn",
        
                    # the properties below are optional
                    assume_role_external_id="assumeRoleExternalId",
                    bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                    requires_bootstrap_stack_version=123
                ),
                parameters={
                    "parameters_key": "parameters"
                },
                requires_bootstrap_stack_version=123,
                stack_name="stackName",
                stack_template_asset_object_url="stackTemplateAssetObjectUrl",
                tags={
                    "tags_key": "tags"
                },
                termination_protection=False,
                validate_on_synth=False
            )
        )
    '''

    def __init__(
        self,
        assembly: CloudAssembly,
        name: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param assembly: -
        :param name: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ac926e1ee09e8dfca43023911e9514e33e19b8a91828eab4d450a48d0bea631)
            check_type(argname="argument assembly", value=assembly, expected_type=type_hints["assembly"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        artifact = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        jsii.create(self.__class__, self, [assembly, name, artifact])

    @jsii.member(jsii_name="isTreeCloudArtifact")
    @builtins.classmethod
    def is_tree_cloud_artifact(cls, art: typing.Any) -> builtins.bool:
        '''Checks if ``art`` is an instance of this class.

        Use this method instead of ``instanceof`` to properly detect ``TreeCloudArtifact``
        instances, even when the construct library is symlinked.

        Explanation: in JavaScript, multiple copies of the ``cx-api`` library on
        disk are seen as independent, completely different libraries. As a
        consequence, the class ``TreeCloudArtifact`` in each copy of the ``cx-api`` library
        is seen as a different class, and an instance of one class will not test as
        ``instanceof`` the other class. ``npm install`` will not create installations
        like this, but users may manually symlink construct libraries together or
        use a monorepo tool: in those cases, multiple copies of the ``cx-api``
        library can be accidentally installed, and ``instanceof`` will behave
        unpredictably. It is safest to avoid using ``instanceof``, and using
        this type-testing method instead.

        :param art: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__719623729bff1c3a8f1e1bd1a4f6a3f18b01238945d9e3de639d5e629e4b449c)
            check_type(argname="argument art", value=art, expected_type=type_hints["art"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isTreeCloudArtifact", [art]))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.VpcContextResponse",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "vpc_id": "vpcId",
        "isolated_subnet_ids": "isolatedSubnetIds",
        "isolated_subnet_names": "isolatedSubnetNames",
        "isolated_subnet_route_table_ids": "isolatedSubnetRouteTableIds",
        "owner_account_id": "ownerAccountId",
        "private_subnet_ids": "privateSubnetIds",
        "private_subnet_names": "privateSubnetNames",
        "private_subnet_route_table_ids": "privateSubnetRouteTableIds",
        "public_subnet_ids": "publicSubnetIds",
        "public_subnet_names": "publicSubnetNames",
        "public_subnet_route_table_ids": "publicSubnetRouteTableIds",
        "region": "region",
        "subnet_groups": "subnetGroups",
        "vpc_cidr_block": "vpcCidrBlock",
        "vpn_gateway_id": "vpnGatewayId",
    },
)
class VpcContextResponse:
    def __init__(
        self,
        *,
        availability_zones: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        isolated_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        isolated_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        isolated_subnet_route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        owner_account_id: typing.Optional[builtins.str] = None,
        private_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        region: typing.Optional[builtins.str] = None,
        subnet_groups: typing.Optional[typing.Sequence[typing.Union["VpcSubnetGroup", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_cidr_block: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties of a discovered VPC.

        :param availability_zones: AZs.
        :param vpc_id: VPC id.
        :param isolated_subnet_ids: IDs of all isolated subnets. Element count: #(availabilityZones) · #(isolatedGroups)
        :param isolated_subnet_names: Name of isolated subnet groups. Element count: #(isolatedGroups)
        :param isolated_subnet_route_table_ids: Route Table IDs of isolated subnet groups. Element count: #(availabilityZones) · #(isolatedGroups)
        :param owner_account_id: The ID of the AWS account that owns the VPC. Default: the account id of the parent stack
        :param private_subnet_ids: IDs of all private subnets. Element count: #(availabilityZones) · #(privateGroups)
        :param private_subnet_names: Name of private subnet groups. Element count: #(privateGroups)
        :param private_subnet_route_table_ids: Route Table IDs of private subnet groups. Element count: #(availabilityZones) · #(privateGroups)
        :param public_subnet_ids: IDs of all public subnets. Element count: #(availabilityZones) · #(publicGroups)
        :param public_subnet_names: Name of public subnet groups. Element count: #(publicGroups)
        :param public_subnet_route_table_ids: Route Table IDs of public subnet groups. Element count: #(availabilityZones) · #(publicGroups)
        :param region: The region in which the VPC is in. Default: - Region of the parent stack
        :param subnet_groups: The subnet groups discovered for the given VPC. Unlike the above properties, this will include asymmetric subnets, if the VPC has any. This property will only be populated if ``VpcContextQuery.returnAsymmetricSubnets`` is true. Default: - no subnet groups will be returned unless ``VpcContextQuery.returnAsymmetricSubnets`` is true
        :param vpc_cidr_block: VPC cidr. Default: - CIDR information not available
        :param vpn_gateway_id: The VPN gateway ID.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            vpc_context_response = cx_api.VpcContextResponse(
                availability_zones=["availabilityZones"],
                vpc_id="vpcId",
            
                # the properties below are optional
                isolated_subnet_ids=["isolatedSubnetIds"],
                isolated_subnet_names=["isolatedSubnetNames"],
                isolated_subnet_route_table_ids=["isolatedSubnetRouteTableIds"],
                owner_account_id="ownerAccountId",
                private_subnet_ids=["privateSubnetIds"],
                private_subnet_names=["privateSubnetNames"],
                private_subnet_route_table_ids=["privateSubnetRouteTableIds"],
                public_subnet_ids=["publicSubnetIds"],
                public_subnet_names=["publicSubnetNames"],
                public_subnet_route_table_ids=["publicSubnetRouteTableIds"],
                region="region",
                subnet_groups=[cx_api.VpcSubnetGroup(
                    name="name",
                    subnets=[cx_api.VpcSubnet(
                        availability_zone="availabilityZone",
                        route_table_id="routeTableId",
                        subnet_id="subnetId",
            
                        # the properties below are optional
                        cidr="cidr"
                    )],
                    type=cx_api.VpcSubnetGroupType.PUBLIC
                )],
                vpc_cidr_block="vpcCidrBlock",
                vpn_gateway_id="vpnGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b99c21e77b73d3bb2ec2b5e4d552fdc6d32ae642513f2ea084181982c50129)
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument isolated_subnet_ids", value=isolated_subnet_ids, expected_type=type_hints["isolated_subnet_ids"])
            check_type(argname="argument isolated_subnet_names", value=isolated_subnet_names, expected_type=type_hints["isolated_subnet_names"])
            check_type(argname="argument isolated_subnet_route_table_ids", value=isolated_subnet_route_table_ids, expected_type=type_hints["isolated_subnet_route_table_ids"])
            check_type(argname="argument owner_account_id", value=owner_account_id, expected_type=type_hints["owner_account_id"])
            check_type(argname="argument private_subnet_ids", value=private_subnet_ids, expected_type=type_hints["private_subnet_ids"])
            check_type(argname="argument private_subnet_names", value=private_subnet_names, expected_type=type_hints["private_subnet_names"])
            check_type(argname="argument private_subnet_route_table_ids", value=private_subnet_route_table_ids, expected_type=type_hints["private_subnet_route_table_ids"])
            check_type(argname="argument public_subnet_ids", value=public_subnet_ids, expected_type=type_hints["public_subnet_ids"])
            check_type(argname="argument public_subnet_names", value=public_subnet_names, expected_type=type_hints["public_subnet_names"])
            check_type(argname="argument public_subnet_route_table_ids", value=public_subnet_route_table_ids, expected_type=type_hints["public_subnet_route_table_ids"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subnet_groups", value=subnet_groups, expected_type=type_hints["subnet_groups"])
            check_type(argname="argument vpc_cidr_block", value=vpc_cidr_block, expected_type=type_hints["vpc_cidr_block"])
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_zones": availability_zones,
            "vpc_id": vpc_id,
        }
        if isolated_subnet_ids is not None:
            self._values["isolated_subnet_ids"] = isolated_subnet_ids
        if isolated_subnet_names is not None:
            self._values["isolated_subnet_names"] = isolated_subnet_names
        if isolated_subnet_route_table_ids is not None:
            self._values["isolated_subnet_route_table_ids"] = isolated_subnet_route_table_ids
        if owner_account_id is not None:
            self._values["owner_account_id"] = owner_account_id
        if private_subnet_ids is not None:
            self._values["private_subnet_ids"] = private_subnet_ids
        if private_subnet_names is not None:
            self._values["private_subnet_names"] = private_subnet_names
        if private_subnet_route_table_ids is not None:
            self._values["private_subnet_route_table_ids"] = private_subnet_route_table_ids
        if public_subnet_ids is not None:
            self._values["public_subnet_ids"] = public_subnet_ids
        if public_subnet_names is not None:
            self._values["public_subnet_names"] = public_subnet_names
        if public_subnet_route_table_ids is not None:
            self._values["public_subnet_route_table_ids"] = public_subnet_route_table_ids
        if region is not None:
            self._values["region"] = region
        if subnet_groups is not None:
            self._values["subnet_groups"] = subnet_groups
        if vpc_cidr_block is not None:
            self._values["vpc_cidr_block"] = vpc_cidr_block
        if vpn_gateway_id is not None:
            self._values["vpn_gateway_id"] = vpn_gateway_id

    @builtins.property
    def availability_zones(self) -> typing.List[builtins.str]:
        '''AZs.'''
        result = self._values.get("availability_zones")
        assert result is not None, "Required property 'availability_zones' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''VPC id.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def isolated_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IDs of all isolated subnets.

        Element count: #(availabilityZones) · #(isolatedGroups)
        '''
        result = self._values.get("isolated_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def isolated_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Name of isolated subnet groups.

        Element count: #(isolatedGroups)
        '''
        result = self._values.get("isolated_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def isolated_subnet_route_table_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Route Table IDs of isolated subnet groups.

        Element count: #(availabilityZones) · #(isolatedGroups)
        '''
        result = self._values.get("isolated_subnet_route_table_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def owner_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS account that owns the VPC.

        :default: the account id of the parent stack
        '''
        result = self._values.get("owner_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IDs of all private subnets.

        Element count: #(availabilityZones) · #(privateGroups)
        '''
        result = self._values.get("private_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Name of private subnet groups.

        Element count: #(privateGroups)
        '''
        result = self._values.get("private_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_subnet_route_table_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Route Table IDs of private subnet groups.

        Element count: #(availabilityZones) · #(privateGroups)
        '''
        result = self._values.get("private_subnet_route_table_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IDs of all public subnets.

        Element count: #(availabilityZones) · #(publicGroups)
        '''
        result = self._values.get("public_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Name of public subnet groups.

        Element count: #(publicGroups)
        '''
        result = self._values.get("public_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_subnet_route_table_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Route Table IDs of public subnet groups.

        Element count: #(availabilityZones) · #(publicGroups)
        '''
        result = self._values.get("public_subnet_route_table_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region in which the VPC is in.

        :default: - Region of the parent stack
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_groups(self) -> typing.Optional[typing.List["VpcSubnetGroup"]]:
        '''The subnet groups discovered for the given VPC.

        Unlike the above properties, this will include asymmetric subnets,
        if the VPC has any.
        This property will only be populated if ``VpcContextQuery.returnAsymmetricSubnets``
        is true.

        :default: - no subnet groups will be returned unless ``VpcContextQuery.returnAsymmetricSubnets`` is true
        '''
        result = self._values.get("subnet_groups")
        return typing.cast(typing.Optional[typing.List["VpcSubnetGroup"]], result)

    @builtins.property
    def vpc_cidr_block(self) -> typing.Optional[builtins.str]:
        '''VPC cidr.

        :default: - CIDR information not available
        '''
        result = self._values.get("vpc_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_gateway_id(self) -> typing.Optional[builtins.str]:
        '''The VPN gateway ID.'''
        result = self._values.get("vpn_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcContextResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.VpcSubnet",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "route_table_id": "routeTableId",
        "subnet_id": "subnetId",
        "cidr": "cidr",
    },
)
class VpcSubnet:
    def __init__(
        self,
        *,
        availability_zone: builtins.str,
        route_table_id: builtins.str,
        subnet_id: builtins.str,
        cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A subnet representation that the VPC provider uses.

        :param availability_zone: The code of the availability zone this subnet is in (for example, 'us-west-2a').
        :param route_table_id: The identifier of the route table for this subnet.
        :param subnet_id: The identifier of the subnet.
        :param cidr: CIDR range of the subnet. Default: - CIDR information not available

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            vpc_subnet = cx_api.VpcSubnet(
                availability_zone="availabilityZone",
                route_table_id="routeTableId",
                subnet_id="subnetId",
            
                # the properties below are optional
                cidr="cidr"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358370651f26ad7cbe7c86ea5aa2291df4cf12ab5370c9e7592e4591ebb4acf9)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument route_table_id", value=route_table_id, expected_type=type_hints["route_table_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_zone": availability_zone,
            "route_table_id": route_table_id,
            "subnet_id": subnet_id,
        }
        if cidr is not None:
            self._values["cidr"] = cidr

    @builtins.property
    def availability_zone(self) -> builtins.str:
        '''The code of the availability zone this subnet is in (for example, 'us-west-2a').'''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_table_id(self) -> builtins.str:
        '''The identifier of the route table for this subnet.'''
        result = self._values.get("route_table_id")
        assert result is not None, "Required property 'route_table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The identifier of the subnet.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr(self) -> typing.Optional[builtins.str]:
        '''CIDR range of the subnet.

        :default: - CIDR information not available
        '''
        result = self._values.get("cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcSubnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cx_api.VpcSubnetGroup",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "subnets": "subnets", "type": "type"},
)
class VpcSubnetGroup:
    def __init__(
        self,
        *,
        name: builtins.str,
        subnets: typing.Sequence[typing.Union[VpcSubnet, typing.Dict[builtins.str, typing.Any]]],
        type: "VpcSubnetGroupType",
    ) -> None:
        '''A group of subnets returned by the VPC provider.

        The included subnets do NOT have to be symmetric!

        :param name: The name of the subnet group, determined by looking at the tags of of the subnets that belong to it.
        :param subnets: The subnets that are part of this group. There is no condition that the subnets have to be symmetric in the group.
        :param type: The type of the subnet group.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cx_api
            
            vpc_subnet_group = cx_api.VpcSubnetGroup(
                name="name",
                subnets=[cx_api.VpcSubnet(
                    availability_zone="availabilityZone",
                    route_table_id="routeTableId",
                    subnet_id="subnetId",
            
                    # the properties below are optional
                    cidr="cidr"
                )],
                type=cx_api.VpcSubnetGroupType.PUBLIC
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcc71b9bbef79ab1afad1f5d8848a55e138477df6b699bd401ed5d4b6be7d859)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "subnets": subnets,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the subnet group, determined by looking at the tags of of the subnets that belong to it.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnets(self) -> typing.List[VpcSubnet]:
        '''The subnets that are part of this group.

        There is no condition that the subnets have to be symmetric
        in the group.
        '''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[VpcSubnet], result)

    @builtins.property
    def type(self) -> "VpcSubnetGroupType":
        '''The type of the subnet group.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("VpcSubnetGroupType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcSubnetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cx_api.VpcSubnetGroupType")
class VpcSubnetGroupType(enum.Enum):
    '''The type of subnet group.

    Same as SubnetType in the aws-cdk-lib/aws-ec2 package,
    but we can't use that because of cyclical dependencies.
    '''

    PUBLIC = "PUBLIC"
    '''Public subnet group type.'''
    PRIVATE = "PRIVATE"
    '''Private subnet group type.'''
    ISOLATED = "ISOLATED"
    '''Isolated subnet group type.'''


class AssetManifestArtifact(
    CloudArtifact,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cx_api.AssetManifestArtifact",
):
    '''Asset manifest is a description of a set of assets which need to be built and published.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cloud_assembly_schema
        from aws_cdk import cx_api
        
        # cloud_assembly: cx_api.CloudAssembly
        
        asset_manifest_artifact = cx_api.AssetManifestArtifact(cloud_assembly, "name",
            type=cloud_assembly_schema.ArtifactType.NONE,
        
            # the properties below are optional
            dependencies=["dependencies"],
            display_name="displayName",
            environment="environment",
            metadata={
                "metadata_key": [cloud_assembly_schema.MetadataEntry(
                    type="type",
        
                    # the properties below are optional
                    data="data",
                    trace=["trace"]
                )]
            },
            properties=cloud_assembly_schema.AwsCloudFormationStackProperties(
                template_file="templateFile",
        
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                cloud_formation_execution_role_arn="cloudFormationExecutionRoleArn",
                lookup_role=cloud_assembly_schema.BootstrapRole(
                    arn="arn",
        
                    # the properties below are optional
                    assume_role_external_id="assumeRoleExternalId",
                    bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                    requires_bootstrap_stack_version=123
                ),
                parameters={
                    "parameters_key": "parameters"
                },
                requires_bootstrap_stack_version=123,
                stack_name="stackName",
                stack_template_asset_object_url="stackTemplateAssetObjectUrl",
                tags={
                    "tags_key": "tags"
                },
                termination_protection=False,
                validate_on_synth=False
            )
        )
    '''

    def __init__(
        self,
        assembly: CloudAssembly,
        name: builtins.str,
        *,
        type: _ArtifactType_1d870526,
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param assembly: -
        :param name: -
        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d3ca09f65f0b6d82995f24fb98a9330c17865775e1a04d254348d053cac5636)
            check_type(argname="argument assembly", value=assembly, expected_type=type_hints["assembly"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        artifact = _ArtifactManifest_f79eef21(
            type=type,
            dependencies=dependencies,
            display_name=display_name,
            environment=environment,
            metadata=metadata,
            properties=properties,
        )

        jsii.create(self.__class__, self, [assembly, name, artifact])

    @jsii.member(jsii_name="isAssetManifestArtifact")
    @builtins.classmethod
    def is_asset_manifest_artifact(cls, art: typing.Any) -> builtins.bool:
        '''Checks if ``art`` is an instance of this class.

        Use this method instead of ``instanceof`` to properly detect ``AssetManifestArtifact``
        instances, even when the construct library is symlinked.

        Explanation: in JavaScript, multiple copies of the ``cx-api`` library on
        disk are seen as independent, completely different libraries. As a
        consequence, the class ``AssetManifestArtifact`` in each copy of the ``cx-api`` library
        is seen as a different class, and an instance of one class will not test as
        ``instanceof`` the other class. ``npm install`` will not create installations
        like this, but users may manually symlink construct libraries together or
        use a monorepo tool: in those cases, multiple copies of the ``cx-api``
        library can be accidentally installed, and ``instanceof`` will behave
        unpredictably. It is safest to avoid using ``instanceof``, and using
        this type-testing method instead.

        :param art: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cdb3373494bc6b73de4ef674ad469482cb5462066462262be592ba7f4dedc72)
            check_type(argname="argument art", value=art, expected_type=type_hints["art"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isAssetManifestArtifact", [art]))

    @builtins.property
    @jsii.member(jsii_name="contents")
    def contents(self) -> _AssetManifest_6cc3f0bc:
        '''The Asset Manifest contents.'''
        return typing.cast(_AssetManifest_6cc3f0bc, jsii.get(self, "contents"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        '''The file name of the asset manifest.'''
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapStackVersionSsmParameter")
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''Name of SSM parameter with bootstrap stack version.

        :default: - Discover SSM parameter by reading stack
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootstrapStackVersionSsmParameter"))

    @builtins.property
    @jsii.member(jsii_name="requiresBootstrapStackVersion")
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to deploy this stack.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requiresBootstrapStackVersion"))


__all__ = [
    "AssemblyBuildOptions",
    "AssetManifestArtifact",
    "AwsCloudFormationStackProperties",
    "CloudArtifact",
    "CloudAssembly",
    "CloudAssemblyBuilder",
    "CloudAssemblyBuilderProps",
    "CloudFormationStackArtifact",
    "EndpointServiceAvailabilityZonesContextQuery",
    "Environment",
    "EnvironmentPlaceholderValues",
    "EnvironmentPlaceholders",
    "EnvironmentUtils",
    "IEnvironmentPlaceholderProvider",
    "KeyContextResponse",
    "LoadBalancerContextResponse",
    "LoadBalancerIpAddressType",
    "LoadBalancerListenerContextResponse",
    "MetadataEntryResult",
    "NestedCloudAssemblyArtifact",
    "SecurityGroupContextResponse",
    "SynthesisMessage",
    "SynthesisMessageLevel",
    "TreeCloudArtifact",
    "VpcContextResponse",
    "VpcSubnet",
    "VpcSubnetGroup",
    "VpcSubnetGroupType",
]

publication.publish()

def _typecheckingstub__bb5c34615f91cec20ab023825c3decd0924a1d39d649c98c600cea970833ced2(
    *,
    template_file: builtins.str,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    stack_name: typing.Optional[builtins.str] = None,
    termination_protection: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d9df0767e898e3c7d2743835aa9ce65467ceb2a717a448ad988e9d722408a1(
    assembly: CloudAssembly,
    id: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43b33c096c23def76559e7ae04cbbfebe9400c25a9d7ec0ac79410d9352d1ae(
    assembly: CloudAssembly,
    id: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd3800ffb245fcadd6ec9780f43d13dc9f50e017d0c1cf6773cb5aa63830bca1(
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fddddcb2935767018d09ab9bba771c647da4dca6bcf2951acca71837d23ce0f2(
    directory: builtins.str,
    *,
    skip_enum_check: typing.Optional[builtins.bool] = None,
    skip_version_check: typing.Optional[builtins.bool] = None,
    topo_sort: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f303b13d87775fd1d362c0be6661fb685434df6fe5e86613a878ccc458c13c4a(
    artifact_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca1be00ea6d5a6a3181e15cd3a7f56176d04c8f133fb678d50aac534642ef410(
    artifact_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8fde0b2ca8fe6d68a7cd056ccfad10bf4236a83c0ac2d68ceff5eb735a15a1(
    artifact_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b840a228aed1fef6a09c8ac443f560499b8b76163fcfca5f4fcdae412e7ce2ec(
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7c8acc8076027cc90b668ac3309172b04bcab88dfe6087bd99e1947e5f5824(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6a1363879dd2a5bcc5f520c0f431ae7555bcd85bdb9c732ec6bb62af4c7f5b(
    outdir: typing.Optional[builtins.str] = None,
    *,
    asset_outdir: typing.Optional[builtins.str] = None,
    parent_builder: typing.Optional[CloudAssemblyBuilder] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261d018bdb1dc9a71bf2eedbb2cef096556840e4a312cda97d52542715b7bddc(
    id: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e63712a9b3643ce667b29b1f646c53fbff128df67c060f5e9a1f8cd350a0354(
    artifact_id: builtins.str,
    display_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cf08d1d4732cadcfbad0197fedaa9b4ea676984caad92dcdf90c09904e0faa5(
    *,
    asset_outdir: typing.Optional[builtins.str] = None,
    parent_builder: typing.Optional[CloudAssemblyBuilder] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efbcfecbcc773b1f90d568df2c82e4e67168ad418a9cd97880b975d214994119(
    assembly: CloudAssembly,
    artifact_id: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b66444028144603e6b05b0b8247226ffeb9078622ddf73bd9d540b8ce722630(
    art: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18b8b66b1c10428da0ac775df90fa02d4536a3abf32809fd4aa5613c7b749708(
    *,
    account: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b89ece71f0626cb86a981885eb005d80d37b76239395b1fb770f98af0feb287(
    *,
    account: builtins.str,
    name: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed6e19535466d26cdb82f05ca1d5f232f037fa0049d12f75cf29ad817a5d7f32(
    *,
    account_id: builtins.str,
    partition: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c501acc043bc39a8bac96f39d791a6247df0ff4b85022293cf10a9e35c2cbf(
    object: typing.Any,
    *,
    account_id: builtins.str,
    partition: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1afabc7b5a7558dae687aa1b5d2443a52cc7b5f0e6aab01ccd7c06217f2346d(
    object: typing.Any,
    provider: IEnvironmentPlaceholderProvider,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ab540cd47ccd18967a60dbc22dd525d173430ed5fd87a09975a27c1b4a1e40(
    account: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc28e540849733b49f0e7ba0129dc101535f53a2636a768cad3fa3ebe9ee5dbf(
    account: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b352e789835b9c9e77225861068bcffa327be4b34b87310b0ac375b17023fb(
    environment: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f13cf02baa9a996348503c81bdcb5503ad573a31d58b8846bc221099cffd660(
    *,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac79c3d47933ad7a274fcd1507b7e94ece2bc4338505867e28ea64343cdbe0d(
    *,
    ip_address_type: LoadBalancerIpAddressType,
    load_balancer_arn: builtins.str,
    load_balancer_canonical_hosted_zone_id: builtins.str,
    load_balancer_dns_name: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a91c0cb0c6c1935935039ee08853827eb62ce0b9747a7e1792fe0e444a64bd1(
    *,
    listener_arn: builtins.str,
    listener_port: jsii.Number,
    security_group_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb7cda500898c592440fb240140921316008dc94a4ac6385c5fe171bac93252(
    *,
    type: builtins.str,
    data: typing.Optional[typing.Union[builtins.str, typing.Union[_FileAssetMetadataEntry_50173f8f, typing.Dict[builtins.str, typing.Any]], typing.Union[_ContainerImageAssetMetadataEntry_0a212d1d, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[_Tag_554dd7f9, typing.Dict[builtins.str, typing.Any]]]]] = None,
    trace: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58cd751fc0676bdece56072cebc370619182e12e08433ef6415db29d47ea7fb4(
    assembly: CloudAssembly,
    name: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a2e95d592babe551ba1095814395519ee8ddb44b75386590a67acad58e21be(
    art: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f30736a8fbf7f3faa6b49be9a48d529ff37ecf26b24a4bae9cb6821dbe8bdc(
    *,
    allow_all_outbound: builtins.bool,
    security_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29937f9afd429e77cb3104d8535016507a83d9824ac8c4c46469e321925a6d3e(
    *,
    entry: typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]],
    id: builtins.str,
    level: SynthesisMessageLevel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac926e1ee09e8dfca43023911e9514e33e19b8a91828eab4d450a48d0bea631(
    assembly: CloudAssembly,
    name: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__719623729bff1c3a8f1e1bd1a4f6a3f18b01238945d9e3de639d5e629e4b449c(
    art: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b99c21e77b73d3bb2ec2b5e4d552fdc6d32ae642513f2ea084181982c50129(
    *,
    availability_zones: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    isolated_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    isolated_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    isolated_subnet_route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    owner_account_id: typing.Optional[builtins.str] = None,
    private_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    region: typing.Optional[builtins.str] = None,
    subnet_groups: typing.Optional[typing.Sequence[typing.Union[VpcSubnetGroup, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_cidr_block: typing.Optional[builtins.str] = None,
    vpn_gateway_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358370651f26ad7cbe7c86ea5aa2291df4cf12ab5370c9e7592e4591ebb4acf9(
    *,
    availability_zone: builtins.str,
    route_table_id: builtins.str,
    subnet_id: builtins.str,
    cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc71b9bbef79ab1afad1f5d8848a55e138477df6b699bd401ed5d4b6be7d859(
    *,
    name: builtins.str,
    subnets: typing.Sequence[typing.Union[VpcSubnet, typing.Dict[builtins.str, typing.Any]]],
    type: VpcSubnetGroupType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3ca09f65f0b6d82995f24fb98a9330c17865775e1a04d254348d053cac5636(
    assembly: CloudAssembly,
    name: builtins.str,
    *,
    type: _ArtifactType_1d870526,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[_MetadataEntry_13e1bf79, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[_AwsCloudFormationStackProperties_50fb16af, typing.Dict[builtins.str, typing.Any]], typing.Union[_AssetManifestProperties_9084879a, typing.Dict[builtins.str, typing.Any]], typing.Union[_TreeArtifactProperties_4092757e, typing.Dict[builtins.str, typing.Any]], typing.Union[_NestedCloudAssemblyProperties_c2fa342d, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cdb3373494bc6b73de4ef674ad469482cb5462066462262be592ba7f4dedc72(
    art: typing.Any,
) -> None:
    """Type checking stubs"""
    pass
