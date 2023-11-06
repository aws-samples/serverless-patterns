'''
# Cloud Assembly Schema

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Cloud Assembly

The *Cloud Assembly* is the output of the synthesis operation. It is produced as part of the
[`cdk synth`](https://github.com/aws/aws-cdk/tree/main/packages/aws-cdk#cdk-synthesize)
command, or the [`app.synth()`](https://github.com/aws/aws-cdk/blob/main/packages/@aws-cdk/core/lib/app.ts#L135) method invocation.

Its essentially a set of files and directories, one of which is the `manifest.json` file. It defines the set of instructions that are
needed in order to deploy the assembly directory.

> For example, when `cdk deploy` is executed, the CLI reads this file and performs its instructions:
>
> * Build container images.
> * Upload assets.
> * Deploy CloudFormation templates.

Therefore, the assembly is how the CDK class library and CDK CLI (or any other consumer) communicate. To ensure compatibility
between the assembly and its consumers, we treat the manifest file as a well defined, versioned schema.

## Schema

This module contains the typescript structs that comprise the `manifest.json` file, as well as the
generated [*json-schema*](./schema/cloud-assembly.schema.json).

## Versioning

The schema version is specified in the [`cloud-assembly.version.json`](./schema/cloud-assembly.schema.json) file, under the `version` property.
It follows semantic versioning, but with a small twist.

When we add instructions to the assembly, they are reflected in the manifest file and the *json-schema* accordingly.
Every such instruction, is crucial for ensuring the correct deployment behavior. This means that to properly deploy a cloud assembly,
consumers must be aware of every such instruction modification.

For this reason, every change to the schema, even though it might not strictly break validation of the *json-schema* format,
is considered `major` version bump.

## How to consume

If you'd like to consume the [schema file](./schema/cloud-assembly.schema.json) in order to do validations on `manifest.json` files,
simply download it from this repo and run it against standard *json-schema* validators, such as [jsonschema](https://www.npmjs.com/package/jsonschema).

Consumers must take into account the `major` version of the schema they are consuming. They should reject cloud assemblies
with a `major` version that is higher than what they expect. While schema validation might pass on such assemblies, the deployment integrity
cannot be guaranteed because some instructions will be ignored.

> For example, if your consumer was built when the schema version was 2.0.0, you should reject deploying cloud assemblies with a
> manifest version of 3.0.0.

## Contributing

See [Contribution Guide](./CONTRIBUTING.md)
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AmiContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "filters": "filters",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
        "owners": "owners",
    },
)
class AmiContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        filters: typing.Mapping[builtins.str, typing.Sequence[builtins.str]],
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Query to AMI context provider.

        :param account: Account to query.
        :param filters: Filters to DescribeImages call.
        :param region: Region to query.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None
        :param owners: Owners to DescribeImages call. Default: - All owners

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            ami_context_query = cloud_assembly_schema.AmiContextQuery(
                account="account",
                filters={
                    "filters_key": ["filters"]
                },
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn",
                owners=["owners"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ad6944b308c0d053938a9bf5ce1be77af5b529135dc35a4c245384840501111)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
            check_type(argname="argument owners", value=owners, expected_type=type_hints["owners"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "filters": filters,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn
        if owners is not None:
            self._values["owners"] = owners

    @builtins.property
    def account(self) -> builtins.str:
        '''Account to query.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filters(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        '''Filters to DescribeImages call.'''
        result = self._values.get("filters")
        assert result is not None, "Required property 'filters' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.List[builtins.str]], result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Region to query.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Owners to DescribeImages call.

        :default: - All owners
        '''
        result = self._values.get("owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AmiContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.ArtifactManifest",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "dependencies": "dependencies",
        "display_name": "displayName",
        "environment": "environment",
        "metadata": "metadata",
        "properties": "properties",
    },
)
class ArtifactManifest:
    def __init__(
        self,
        *,
        type: "ArtifactType",
        dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union["MetadataEntry", typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[typing.Union["AwsCloudFormationStackProperties", typing.Dict[builtins.str, typing.Any]], typing.Union["AssetManifestProperties", typing.Dict[builtins.str, typing.Any]], typing.Union["TreeArtifactProperties", typing.Dict[builtins.str, typing.Any]], typing.Union["NestedCloudAssemblyProperties", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''A manifest for a single artifact within the cloud assembly.

        :param type: The type of artifact.
        :param dependencies: IDs of artifacts that must be deployed before this artifact. Default: - no dependencies.
        :param display_name: A string that represents this artifact. Should only be used in user interfaces. Default: - no display name
        :param environment: The environment into which this artifact is deployed. Default: - no envrionment.
        :param metadata: Associated metadata. Default: - no metadata.
        :param properties: The set of properties for this artifact (depends on type). Default: - no properties.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            artifact_manifest = cloud_assembly_schema.ArtifactManifest(
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
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0fe0dea35f8750630dc6eb16d5f979ef40079f01dc4afec1b7ebf62d6958505)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument dependencies", value=dependencies, expected_type=type_hints["dependencies"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if dependencies is not None:
            self._values["dependencies"] = dependencies
        if display_name is not None:
            self._values["display_name"] = display_name
        if environment is not None:
            self._values["environment"] = environment
        if metadata is not None:
            self._values["metadata"] = metadata
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def type(self) -> "ArtifactType":
        '''The type of artifact.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("ArtifactType", result)

    @builtins.property
    def dependencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IDs of artifacts that must be deployed before this artifact.

        :default: - no dependencies.
        '''
        result = self._values.get("dependencies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A string that represents this artifact.

        Should only be used in user interfaces.

        :default: - no display name
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The environment into which this artifact is deployed.

        :default: - no envrionment.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List["MetadataEntry"]]]:
        '''Associated metadata.

        :default: - no metadata.
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List["MetadataEntry"]]], result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union["AwsCloudFormationStackProperties", "AssetManifestProperties", "TreeArtifactProperties", "NestedCloudAssemblyProperties"]]:
        '''The set of properties for this artifact (depends on type).

        :default: - no properties.
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union["AwsCloudFormationStackProperties", "AssetManifestProperties", "TreeArtifactProperties", "NestedCloudAssemblyProperties"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArtifactManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.ArtifactMetadataEntryType")
class ArtifactMetadataEntryType(enum.Enum):
    '''Type of artifact metadata entry.'''

    ASSET = "ASSET"
    '''Asset in metadata.'''
    INFO = "INFO"
    '''Metadata key used to print INFO-level messages by the toolkit when an app is syntheized.'''
    WARN = "WARN"
    '''Metadata key used to print WARNING-level messages by the toolkit when an app is syntheized.'''
    ERROR = "ERROR"
    '''Metadata key used to print ERROR-level messages by the toolkit when an app is syntheized.'''
    LOGICAL_ID = "LOGICAL_ID"
    '''Represents the CloudFormation logical ID of a resource at a certain path.'''
    STACK_TAGS = "STACK_TAGS"
    '''Represents tags of a stack.'''


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.ArtifactType")
class ArtifactType(enum.Enum):
    '''Type of cloud artifact.'''

    NONE = "NONE"
    '''Stub required because of JSII.'''
    AWS_CLOUDFORMATION_STACK = "AWS_CLOUDFORMATION_STACK"
    '''The artifact is an AWS CloudFormation stack.'''
    CDK_TREE = "CDK_TREE"
    '''The artifact contains the CDK application's construct tree.'''
    ASSET_MANIFEST = "ASSET_MANIFEST"
    '''Manifest for all assets in the Cloud Assembly.'''
    NESTED_CLOUD_ASSEMBLY = "NESTED_CLOUD_ASSEMBLY"
    '''Nested Cloud Assembly.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AssemblyManifest",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "artifacts": "artifacts",
        "missing": "missing",
        "runtime": "runtime",
    },
)
class AssemblyManifest:
    def __init__(
        self,
        *,
        version: builtins.str,
        artifacts: typing.Optional[typing.Mapping[builtins.str, typing.Union[ArtifactManifest, typing.Dict[builtins.str, typing.Any]]]] = None,
        missing: typing.Optional[typing.Sequence[typing.Union["MissingContext", typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime: typing.Optional[typing.Union["RuntimeInfo", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''A manifest which describes the cloud assembly.

        :param version: Protocol version.
        :param artifacts: The set of artifacts in this assembly. Default: - no artifacts.
        :param missing: Missing context information. If this field has values, it means that the cloud assembly is not complete and should not be deployed. Default: - no missing context.
        :param runtime: Runtime information. Default: - no info.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            assembly_manifest = cloud_assembly_schema.AssemblyManifest(
                version="version",
            
                # the properties below are optional
                artifacts={
                    "artifacts_key": cloud_assembly_schema.ArtifactManifest(
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
                },
                missing=[cloud_assembly_schema.MissingContext(
                    key="key",
                    props=cloud_assembly_schema.AmiContextQuery(
                        account="account",
                        filters={
                            "filters_key": ["filters"]
                        },
                        region="region",
            
                        # the properties below are optional
                        lookup_role_arn="lookupRoleArn",
                        owners=["owners"]
                    ),
                    provider=cloud_assembly_schema.ContextProvider.AMI_PROVIDER
                )],
                runtime=cloud_assembly_schema.RuntimeInfo(
                    libraries={
                        "libraries_key": "libraries"
                    }
                )
            )
        '''
        if isinstance(runtime, dict):
            runtime = RuntimeInfo(**runtime)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d707328dcc86d4e43fc56bf16523e6c309819b8983de0d413e55cdeb244d4810)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            check_type(argname="argument missing", value=missing, expected_type=type_hints["missing"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if artifacts is not None:
            self._values["artifacts"] = artifacts
        if missing is not None:
            self._values["missing"] = missing
        if runtime is not None:
            self._values["runtime"] = runtime

    @builtins.property
    def version(self) -> builtins.str:
        '''Protocol version.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def artifacts(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, ArtifactManifest]]:
        '''The set of artifacts in this assembly.

        :default: - no artifacts.
        '''
        result = self._values.get("artifacts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, ArtifactManifest]], result)

    @builtins.property
    def missing(self) -> typing.Optional[typing.List["MissingContext"]]:
        '''Missing context information.

        If this field has values, it means that the
        cloud assembly is not complete and should not be deployed.

        :default: - no missing context.
        '''
        result = self._values.get("missing")
        return typing.cast(typing.Optional[typing.List["MissingContext"]], result)

    @builtins.property
    def runtime(self) -> typing.Optional["RuntimeInfo"]:
        '''Runtime information.

        :default: - no info.
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["RuntimeInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssemblyManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AssetManifest",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "docker_images": "dockerImages",
        "files": "files",
    },
)
class AssetManifest:
    def __init__(
        self,
        *,
        version: builtins.str,
        docker_images: typing.Optional[typing.Mapping[builtins.str, typing.Union["DockerImageAsset", typing.Dict[builtins.str, typing.Any]]]] = None,
        files: typing.Optional[typing.Mapping[builtins.str, typing.Union["FileAsset", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Definitions for the asset manifest.

        :param version: Version of the manifest.
        :param docker_images: The Docker image assets in this manifest. Default: - No Docker images
        :param files: The file assets in this manifest. Default: - No files

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            asset_manifest = cloud_assembly_schema.AssetManifest(
                version="version",
            
                # the properties below are optional
                docker_images={
                    "docker_images_key": cloud_assembly_schema.DockerImageAsset(
                        destinations={
                            "destinations_key": cloud_assembly_schema.DockerImageDestination(
                                image_tag="imageTag",
                                repository_name="repositoryName",
            
                                # the properties below are optional
                                assume_role_arn="assumeRoleArn",
                                assume_role_external_id="assumeRoleExternalId",
                                region="region"
                            )
                        },
                        source=cloud_assembly_schema.DockerImageSource(
                            cache_from=[cloud_assembly_schema.DockerCacheOption(
                                type="type",
            
                                # the properties below are optional
                                params={
                                    "params_key": "params"
                                }
                            )],
                            cache_to=cloud_assembly_schema.DockerCacheOption(
                                type="type",
            
                                # the properties below are optional
                                params={
                                    "params_key": "params"
                                }
                            ),
                            directory="directory",
                            docker_build_args={
                                "docker_build_args_key": "dockerBuildArgs"
                            },
                            docker_build_secrets={
                                "docker_build_secrets_key": "dockerBuildSecrets"
                            },
                            docker_build_ssh="dockerBuildSsh",
                            docker_build_target="dockerBuildTarget",
                            docker_file="dockerFile",
                            docker_outputs=["dockerOutputs"],
                            executable=["executable"],
                            network_mode="networkMode",
                            platform="platform"
                        )
                    )
                },
                files={
                    "files_key": cloud_assembly_schema.FileAsset(
                        destinations={
                            "destinations_key": cloud_assembly_schema.FileDestination(
                                bucket_name="bucketName",
                                object_key="objectKey",
            
                                # the properties below are optional
                                assume_role_arn="assumeRoleArn",
                                assume_role_external_id="assumeRoleExternalId",
                                region="region"
                            )
                        },
                        source=cloud_assembly_schema.FileSource(
                            executable=["executable"],
                            packaging=cloud_assembly_schema.FileAssetPackaging.FILE,
                            path="path"
                        )
                    )
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95123227e2e39f7b45c300f671954210a3191a5acc352a40f4cea7ba623ee015)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument docker_images", value=docker_images, expected_type=type_hints["docker_images"])
            check_type(argname="argument files", value=files, expected_type=type_hints["files"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version": version,
        }
        if docker_images is not None:
            self._values["docker_images"] = docker_images
        if files is not None:
            self._values["files"] = files

    @builtins.property
    def version(self) -> builtins.str:
        '''Version of the manifest.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def docker_images(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "DockerImageAsset"]]:
        '''The Docker image assets in this manifest.

        :default: - No Docker images
        '''
        result = self._values.get("docker_images")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "DockerImageAsset"]], result)

    @builtins.property
    def files(self) -> typing.Optional[typing.Mapping[builtins.str, "FileAsset"]]:
        '''The file assets in this manifest.

        :default: - No files
        '''
        result = self._values.get("files")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "FileAsset"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AssetManifestOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bootstrap_stack_version_ssm_parameter": "bootstrapStackVersionSsmParameter",
        "requires_bootstrap_stack_version": "requiresBootstrapStackVersion",
    },
)
class AssetManifestOptions:
    def __init__(
        self,
        *,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configuration options for the Asset Manifest.

        :param bootstrap_stack_version_ssm_parameter: SSM parameter where the bootstrap stack version number can be found. - If this value is not set, the bootstrap stack name must be known at deployment time so the stack version can be looked up from the stack outputs. - If this value is set, the bootstrap stack can have any name because we won't need to look it up. Default: - Bootstrap stack version number looked up
        :param requires_bootstrap_stack_version: Version of bootstrap stack required to deploy this stack. Default: - Version 1 (basic modern bootstrap stack)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            asset_manifest_options = cloud_assembly_schema.AssetManifestOptions(
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                requires_bootstrap_stack_version=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86c77da34e0417278ebaea2f325f2a5b2793410bbe22b270a09a8899516a35f5)
            check_type(argname="argument bootstrap_stack_version_ssm_parameter", value=bootstrap_stack_version_ssm_parameter, expected_type=type_hints["bootstrap_stack_version_ssm_parameter"])
            check_type(argname="argument requires_bootstrap_stack_version", value=requires_bootstrap_stack_version, expected_type=type_hints["requires_bootstrap_stack_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bootstrap_stack_version_ssm_parameter is not None:
            self._values["bootstrap_stack_version_ssm_parameter"] = bootstrap_stack_version_ssm_parameter
        if requires_bootstrap_stack_version is not None:
            self._values["requires_bootstrap_stack_version"] = requires_bootstrap_stack_version

    @builtins.property
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''SSM parameter where the bootstrap stack version number can be found.

        - If this value is not set, the bootstrap stack name must be known at
          deployment time so the stack version can be looked up from the stack
          outputs.
        - If this value is set, the bootstrap stack can have any name because
          we won't need to look it up.

        :default: - Bootstrap stack version number looked up
        '''
        result = self._values.get("bootstrap_stack_version_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to deploy this stack.

        :default: - Version 1 (basic modern bootstrap stack)
        '''
        result = self._values.get("requires_bootstrap_stack_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetManifestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AssetManifestProperties",
    jsii_struct_bases=[AssetManifestOptions],
    name_mapping={
        "bootstrap_stack_version_ssm_parameter": "bootstrapStackVersionSsmParameter",
        "requires_bootstrap_stack_version": "requiresBootstrapStackVersion",
        "file": "file",
    },
)
class AssetManifestProperties(AssetManifestOptions):
    def __init__(
        self,
        *,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
        file: builtins.str,
    ) -> None:
        '''Artifact properties for the Asset Manifest.

        :param bootstrap_stack_version_ssm_parameter: SSM parameter where the bootstrap stack version number can be found. - If this value is not set, the bootstrap stack name must be known at deployment time so the stack version can be looked up from the stack outputs. - If this value is set, the bootstrap stack can have any name because we won't need to look it up. Default: - Bootstrap stack version number looked up
        :param requires_bootstrap_stack_version: Version of bootstrap stack required to deploy this stack. Default: - Version 1 (basic modern bootstrap stack)
        :param file: Filename of the asset manifest.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            asset_manifest_properties = cloud_assembly_schema.AssetManifestProperties(
                file="file",
            
                # the properties below are optional
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                requires_bootstrap_stack_version=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5d2e8772dd80ce81405cd98707a3f710c439c66cd9580fecad1be8252feae38)
            check_type(argname="argument bootstrap_stack_version_ssm_parameter", value=bootstrap_stack_version_ssm_parameter, expected_type=type_hints["bootstrap_stack_version_ssm_parameter"])
            check_type(argname="argument requires_bootstrap_stack_version", value=requires_bootstrap_stack_version, expected_type=type_hints["requires_bootstrap_stack_version"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file": file,
        }
        if bootstrap_stack_version_ssm_parameter is not None:
            self._values["bootstrap_stack_version_ssm_parameter"] = bootstrap_stack_version_ssm_parameter
        if requires_bootstrap_stack_version is not None:
            self._values["requires_bootstrap_stack_version"] = requires_bootstrap_stack_version

    @builtins.property
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''SSM parameter where the bootstrap stack version number can be found.

        - If this value is not set, the bootstrap stack name must be known at
          deployment time so the stack version can be looked up from the stack
          outputs.
        - If this value is set, the bootstrap stack can have any name because
          we won't need to look it up.

        :default: - Bootstrap stack version number looked up
        '''
        result = self._values.get("bootstrap_stack_version_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to deploy this stack.

        :default: - Version 1 (basic modern bootstrap stack)
        '''
        result = self._values.get("requires_bootstrap_stack_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def file(self) -> builtins.str:
        '''Filename of the asset manifest.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetManifestProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AvailabilityZonesContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
    },
)
class AvailabilityZonesContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query to availability zone context provider.

        :param account: Query account.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            availability_zones_context_query = cloud_assembly_schema.AvailabilityZonesContextQuery(
                account="account",
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e23cb5710241f65fda5e65504911a7340786a62ce9cf7c60c9cfc1d4d4a05753)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AvailabilityZonesContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AwsCloudFormationStackProperties",
    jsii_struct_bases=[],
    name_mapping={
        "template_file": "templateFile",
        "assume_role_arn": "assumeRoleArn",
        "assume_role_external_id": "assumeRoleExternalId",
        "bootstrap_stack_version_ssm_parameter": "bootstrapStackVersionSsmParameter",
        "cloud_formation_execution_role_arn": "cloudFormationExecutionRoleArn",
        "lookup_role": "lookupRole",
        "parameters": "parameters",
        "requires_bootstrap_stack_version": "requiresBootstrapStackVersion",
        "stack_name": "stackName",
        "stack_template_asset_object_url": "stackTemplateAssetObjectUrl",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "validate_on_synth": "validateOnSynth",
    },
)
class AwsCloudFormationStackProperties:
    def __init__(
        self,
        *,
        template_file: builtins.str,
        assume_role_arn: typing.Optional[builtins.str] = None,
        assume_role_external_id: typing.Optional[builtins.str] = None,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        cloud_formation_execution_role_arn: typing.Optional[builtins.str] = None,
        lookup_role: typing.Optional[typing.Union["BootstrapRole", typing.Dict[builtins.str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
        stack_name: typing.Optional[builtins.str] = None,
        stack_template_asset_object_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        validate_on_synth: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Artifact properties for CloudFormation stacks.

        :param template_file: A file relative to the assembly root which contains the CloudFormation template for this stack.
        :param assume_role_arn: The role that needs to be assumed to deploy the stack. Default: - No role is assumed (current credentials are used)
        :param assume_role_external_id: External ID to use when assuming role for cloudformation deployments. Default: - No external ID
        :param bootstrap_stack_version_ssm_parameter: SSM parameter where the bootstrap stack version number can be found. Only used if ``requiresBootstrapStackVersion`` is set. - If this value is not set, the bootstrap stack name must be known at deployment time so the stack version can be looked up from the stack outputs. - If this value is set, the bootstrap stack can have any name because we won't need to look it up. Default: - Bootstrap stack version number looked up
        :param cloud_formation_execution_role_arn: The role that is passed to CloudFormation to execute the change set. Default: - No role is passed (currently assumed role/credentials are used)
        :param lookup_role: The role to use to look up values from the target AWS account. Default: - No role is assumed (current credentials are used)
        :param parameters: Values for CloudFormation stack parameters that should be passed when the stack is deployed. Default: - No parameters
        :param requires_bootstrap_stack_version: Version of bootstrap stack required to deploy this stack. Default: - No bootstrap stack required
        :param stack_name: The name to use for the CloudFormation stack. Default: - name derived from artifact ID
        :param stack_template_asset_object_url: If the stack template has already been included in the asset manifest, its asset URL. Default: - Not uploaded yet, upload just before deploying
        :param tags: Values for CloudFormation stack tags that should be passed when the stack is deployed. Default: - No tags
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param validate_on_synth: Whether this stack should be validated by the CLI after synthesis. Default: - false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            aws_cloud_formation_stack_properties = cloud_assembly_schema.AwsCloudFormationStackProperties(
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
        '''
        if isinstance(lookup_role, dict):
            lookup_role = BootstrapRole(**lookup_role)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662c8e7475bc8ebd11512c676ac10ca4f84539770ce9a2a5d5d96a46956fe50e)
            check_type(argname="argument template_file", value=template_file, expected_type=type_hints["template_file"])
            check_type(argname="argument assume_role_arn", value=assume_role_arn, expected_type=type_hints["assume_role_arn"])
            check_type(argname="argument assume_role_external_id", value=assume_role_external_id, expected_type=type_hints["assume_role_external_id"])
            check_type(argname="argument bootstrap_stack_version_ssm_parameter", value=bootstrap_stack_version_ssm_parameter, expected_type=type_hints["bootstrap_stack_version_ssm_parameter"])
            check_type(argname="argument cloud_formation_execution_role_arn", value=cloud_formation_execution_role_arn, expected_type=type_hints["cloud_formation_execution_role_arn"])
            check_type(argname="argument lookup_role", value=lookup_role, expected_type=type_hints["lookup_role"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument requires_bootstrap_stack_version", value=requires_bootstrap_stack_version, expected_type=type_hints["requires_bootstrap_stack_version"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument stack_template_asset_object_url", value=stack_template_asset_object_url, expected_type=type_hints["stack_template_asset_object_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument validate_on_synth", value=validate_on_synth, expected_type=type_hints["validate_on_synth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_file": template_file,
        }
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if assume_role_external_id is not None:
            self._values["assume_role_external_id"] = assume_role_external_id
        if bootstrap_stack_version_ssm_parameter is not None:
            self._values["bootstrap_stack_version_ssm_parameter"] = bootstrap_stack_version_ssm_parameter
        if cloud_formation_execution_role_arn is not None:
            self._values["cloud_formation_execution_role_arn"] = cloud_formation_execution_role_arn
        if lookup_role is not None:
            self._values["lookup_role"] = lookup_role
        if parameters is not None:
            self._values["parameters"] = parameters
        if requires_bootstrap_stack_version is not None:
            self._values["requires_bootstrap_stack_version"] = requires_bootstrap_stack_version
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if stack_template_asset_object_url is not None:
            self._values["stack_template_asset_object_url"] = stack_template_asset_object_url
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if validate_on_synth is not None:
            self._values["validate_on_synth"] = validate_on_synth

    @builtins.property
    def template_file(self) -> builtins.str:
        '''A file relative to the assembly root which contains the CloudFormation template for this stack.'''
        result = self._values.get("template_file")
        assert result is not None, "Required property 'template_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that needs to be assumed to deploy the stack.

        :default: - No role is assumed (current credentials are used)
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_external_id(self) -> typing.Optional[builtins.str]:
        '''External ID to use when assuming role for cloudformation deployments.

        :default: - No external ID
        '''
        result = self._values.get("assume_role_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''SSM parameter where the bootstrap stack version number can be found.

        Only used if ``requiresBootstrapStackVersion`` is set.

        - If this value is not set, the bootstrap stack name must be known at
          deployment time so the stack version can be looked up from the stack
          outputs.
        - If this value is set, the bootstrap stack can have any name because
          we won't need to look it up.

        :default: - Bootstrap stack version number looked up
        '''
        result = self._values.get("bootstrap_stack_version_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_formation_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that is passed to CloudFormation to execute the change set.

        :default: - No role is passed (currently assumed role/credentials are used)
        '''
        result = self._values.get("cloud_formation_execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lookup_role(self) -> typing.Optional["BootstrapRole"]:
        '''The role to use to look up values from the target AWS account.

        :default: - No role is assumed (current credentials are used)
        '''
        result = self._values.get("lookup_role")
        return typing.cast(typing.Optional["BootstrapRole"], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Values for CloudFormation stack parameters that should be passed when the stack is deployed.

        :default: - No parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to deploy this stack.

        :default: - No bootstrap stack required
        '''
        result = self._values.get("requires_bootstrap_stack_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the CloudFormation stack.

        :default: - name derived from artifact ID
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stack_template_asset_object_url(self) -> typing.Optional[builtins.str]:
        '''If the stack template has already been included in the asset manifest, its asset URL.

        :default: - Not uploaded yet, upload just before deploying
        '''
        result = self._values.get("stack_template_asset_object_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Values for CloudFormation stack tags that should be passed when the stack is deployed.

        :default: - No tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validate_on_synth(self) -> typing.Optional[builtins.bool]:
        '''Whether this stack should be validated by the CLI after synthesis.

        :default: - false
        '''
        result = self._values.get("validate_on_synth")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsCloudFormationStackProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.AwsDestination",
    jsii_struct_bases=[],
    name_mapping={
        "assume_role_arn": "assumeRoleArn",
        "assume_role_external_id": "assumeRoleExternalId",
        "region": "region",
    },
)
class AwsDestination:
    def __init__(
        self,
        *,
        assume_role_arn: typing.Optional[builtins.str] = None,
        assume_role_external_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Destination for assets that need to be uploaded to AWS.

        :param assume_role_arn: The role that needs to be assumed while publishing this asset. Default: - No role will be assumed
        :param assume_role_external_id: The ExternalId that needs to be supplied while assuming this role. Default: - No ExternalId will be supplied
        :param region: The region where this asset will need to be published. Default: - Current region

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            aws_destination = cloud_assembly_schema.AwsDestination(
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e91cfad0a891b03534a612d02721f5d8d6378d9951a8f62fa2272323da013b6c)
            check_type(argname="argument assume_role_arn", value=assume_role_arn, expected_type=type_hints["assume_role_arn"])
            check_type(argname="argument assume_role_external_id", value=assume_role_external_id, expected_type=type_hints["assume_role_external_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if assume_role_external_id is not None:
            self._values["assume_role_external_id"] = assume_role_external_id
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that needs to be assumed while publishing this asset.

        :default: - No role will be assumed
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_external_id(self) -> typing.Optional[builtins.str]:
        '''The ExternalId that needs to be supplied while assuming this role.

        :default: - No ExternalId will be supplied
        '''
        result = self._values.get("assume_role_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where this asset will need to be published.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.BootstrapRole",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "assume_role_external_id": "assumeRoleExternalId",
        "bootstrap_stack_version_ssm_parameter": "bootstrapStackVersionSsmParameter",
        "requires_bootstrap_stack_version": "requiresBootstrapStackVersion",
    },
)
class BootstrapRole:
    def __init__(
        self,
        *,
        arn: builtins.str,
        assume_role_external_id: typing.Optional[builtins.str] = None,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Information needed to access an IAM role created as part of the bootstrap process.

        :param arn: The ARN of the IAM role created as part of bootrapping e.g. lookupRoleArn.
        :param assume_role_external_id: External ID to use when assuming the bootstrap role. Default: - No external ID
        :param bootstrap_stack_version_ssm_parameter: Name of SSM parameter with bootstrap stack version. Default: - Discover SSM parameter by reading stack
        :param requires_bootstrap_stack_version: Version of bootstrap stack required to use this role. Default: - No bootstrap stack required

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            bootstrap_role = cloud_assembly_schema.BootstrapRole(
                arn="arn",
            
                # the properties below are optional
                assume_role_external_id="assumeRoleExternalId",
                bootstrap_stack_version_ssm_parameter="bootstrapStackVersionSsmParameter",
                requires_bootstrap_stack_version=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a573afe6fe73a260b78458b7d6ff4d548c9379eb945ffcadd64389efe9b6e65d)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument assume_role_external_id", value=assume_role_external_id, expected_type=type_hints["assume_role_external_id"])
            check_type(argname="argument bootstrap_stack_version_ssm_parameter", value=bootstrap_stack_version_ssm_parameter, expected_type=type_hints["bootstrap_stack_version_ssm_parameter"])
            check_type(argname="argument requires_bootstrap_stack_version", value=requires_bootstrap_stack_version, expected_type=type_hints["requires_bootstrap_stack_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }
        if assume_role_external_id is not None:
            self._values["assume_role_external_id"] = assume_role_external_id
        if bootstrap_stack_version_ssm_parameter is not None:
            self._values["bootstrap_stack_version_ssm_parameter"] = bootstrap_stack_version_ssm_parameter
        if requires_bootstrap_stack_version is not None:
            self._values["requires_bootstrap_stack_version"] = requires_bootstrap_stack_version

    @builtins.property
    def arn(self) -> builtins.str:
        '''The ARN of the IAM role created as part of bootrapping e.g. lookupRoleArn.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assume_role_external_id(self) -> typing.Optional[builtins.str]:
        '''External ID to use when assuming the bootstrap role.

        :default: - No external ID
        '''
        result = self._values.get("assume_role_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''Name of SSM parameter with bootstrap stack version.

        :default: - Discover SSM parameter by reading stack
        '''
        result = self._values.get("bootstrap_stack_version_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to use this role.

        :default: - No bootstrap stack required
        '''
        result = self._values.get("requires_bootstrap_stack_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BootstrapRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.CdkCommand",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "expected_message": "expectedMessage",
        "expect_error": "expectError",
    },
)
class CdkCommand:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        expected_message: typing.Optional[builtins.str] = None,
        expect_error: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Represents a cdk command i.e. ``synth``, ``deploy``, & ``destroy``.

        :param enabled: Whether or not to run this command as part of the workflow This can be used if you only want to test some of the workflow for example enable ``synth`` and disable ``deploy`` & ``destroy`` in order to limit the test to synthesis. Default: true
        :param expected_message: This can be used in combination with ``expectedError`` to validate that a specific message is returned. Default: - do not validate message
        :param expect_error: If the runner should expect this command to fail. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            cdk_command = cloud_assembly_schema.CdkCommand(
                enabled=False,
                expected_message="expectedMessage",
                expect_error=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fab42c5155b5514b7e0da3a4196cd98c96a1d3c1d1581dc4ff88dc1fb1358903)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument expected_message", value=expected_message, expected_type=type_hints["expected_message"])
            check_type(argname="argument expect_error", value=expect_error, expected_type=type_hints["expect_error"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if expected_message is not None:
            self._values["expected_message"] = expected_message
        if expect_error is not None:
            self._values["expect_error"] = expect_error

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to run this command as part of the workflow This can be used if you only want to test some of the workflow for example enable ``synth`` and disable ``deploy`` & ``destroy`` in order to limit the test to synthesis.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expected_message(self) -> typing.Optional[builtins.str]:
        '''This can be used in combination with ``expectedError`` to validate that a specific message is returned.

        :default: - do not validate message
        '''
        result = self._values.get("expected_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expect_error(self) -> typing.Optional[builtins.bool]:
        '''If the runner should expect this command to fail.

        :default: false
        '''
        result = self._values.get("expect_error")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdkCommand(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.CdkCommands",
    jsii_struct_bases=[],
    name_mapping={"deploy": "deploy", "destroy": "destroy"},
)
class CdkCommands:
    def __init__(
        self,
        *,
        deploy: typing.Optional[typing.Union["DeployCommand", typing.Dict[builtins.str, typing.Any]]] = None,
        destroy: typing.Optional[typing.Union["DestroyCommand", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Options for specific cdk commands that are run as part of the integration test workflow.

        :param deploy: Options to for the cdk deploy command. Default: - default deploy options
        :param destroy: Options to for the cdk destroy command. Default: - default destroy options

        :exampleMetadata: infused

        Example::

            app = App()
            
            stack_under_test = Stack(app, "StackUnderTest")
            
            stack = Stack(app, "stack")
            
            test_case = IntegTest(app, "CustomizedDeploymentWorkflow",
                test_cases=[stack_under_test],
                diff_assets=True,
                stack_update_workflow=True,
                cdk_command_options=CdkCommands(
                    deploy=DeployCommand(
                        args=DeployOptions(
                            require_approval=RequireApproval.NEVER,
                            json=True
                        )
                    ),
                    destroy=DestroyCommand(
                        args=DestroyOptions(
                            force=True
                        )
                    )
                )
            )
        '''
        if isinstance(deploy, dict):
            deploy = DeployCommand(**deploy)
        if isinstance(destroy, dict):
            destroy = DestroyCommand(**destroy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95ac9609e4f4d0c031d4e642395354b784dff236227aa06f3731df5f762d0ffc)
            check_type(argname="argument deploy", value=deploy, expected_type=type_hints["deploy"])
            check_type(argname="argument destroy", value=destroy, expected_type=type_hints["destroy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deploy is not None:
            self._values["deploy"] = deploy
        if destroy is not None:
            self._values["destroy"] = destroy

    @builtins.property
    def deploy(self) -> typing.Optional["DeployCommand"]:
        '''Options to for the cdk deploy command.

        :default: - default deploy options
        '''
        result = self._values.get("deploy")
        return typing.cast(typing.Optional["DeployCommand"], result)

    @builtins.property
    def destroy(self) -> typing.Optional["DestroyCommand"]:
        '''Options to for the cdk destroy command.

        :default: - default destroy options
        '''
        result = self._values.get("destroy")
        return typing.cast(typing.Optional["DestroyCommand"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdkCommands(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.ContainerImageAssetCacheOption",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "params": "params"},
)
class ContainerImageAssetCacheOption:
    def __init__(
        self,
        *,
        type: builtins.str,
        params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Options for configuring the Docker cache backend.

        :param type: The type of cache to use. Refer to https://docs.docker.com/build/cache/backends/ for full list of backends. Default: - unspecified
        :param params: Any parameters to pass into the docker cache backend configuration. Refer to https://docs.docker.com/build/cache/backends/ for cache backend configuration. Default: {} No options provided

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            container_image_asset_cache_option = cloud_assembly_schema.ContainerImageAssetCacheOption(
                type="type",
            
                # the properties below are optional
                params={
                    "params_key": "params"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a9c7388f9bfe95e50651a69fc2619a3384f0dac2162a8001fd626420b069e9b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if params is not None:
            self._values["params"] = params

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of cache to use.

        Refer to https://docs.docker.com/build/cache/backends/ for full list of backends.

        :default: - unspecified

        Example::

            "registry"
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def params(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any parameters to pass into the docker cache backend configuration.

        Refer to https://docs.docker.com/build/cache/backends/ for cache backend configuration.

        :default: {} No options provided

        Example::

            # branch: str
            
            
            params = {
                "ref": f"12345678.dkr.ecr.us-west-2.amazonaws.com/cache:{branch}",
                "mode": "max"
            }
        '''
        result = self._values.get("params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerImageAssetCacheOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.ContainerImageAssetMetadataEntry",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "packaging": "packaging",
        "path": "path",
        "source_hash": "sourceHash",
        "build_args": "buildArgs",
        "build_secrets": "buildSecrets",
        "build_ssh": "buildSsh",
        "cache_from": "cacheFrom",
        "cache_to": "cacheTo",
        "file": "file",
        "image_tag": "imageTag",
        "network_mode": "networkMode",
        "outputs": "outputs",
        "platform": "platform",
        "repository_name": "repositoryName",
        "target": "target",
    },
)
class ContainerImageAssetMetadataEntry:
    def __init__(
        self,
        *,
        id: builtins.str,
        packaging: builtins.str,
        path: builtins.str,
        source_hash: builtins.str,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_ssh: typing.Optional[builtins.str] = None,
        cache_from: typing.Optional[typing.Sequence[typing.Union[ContainerImageAssetCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
        cache_to: typing.Optional[typing.Union[ContainerImageAssetCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[builtins.str] = None,
        image_tag: typing.Optional[builtins.str] = None,
        network_mode: typing.Optional[builtins.str] = None,
        outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
        platform: typing.Optional[builtins.str] = None,
        repository_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Metadata Entry spec for container images.

        :param id: Logical identifier for the asset.
        :param packaging: Type of asset.
        :param path: Path on disk to the asset.
        :param source_hash: The hash of the asset source.
        :param build_args: Build args to pass to the ``docker build`` command. Default: no build args are passed
        :param build_secrets: Build secrets to pass to the ``docker build`` command. Default: no build secrets are passed
        :param build_ssh: SSH agent socket or keys to pass to the ``docker build`` command. Default: no ssh arg is passed
        :param cache_from: Cache from options to pass to the ``docker build`` command. Default: - no cache from options are passed to the build command
        :param cache_to: Cache to options to pass to the ``docker build`` command. Default: - no cache to options are passed to the build command
        :param file: Path to the Dockerfile (relative to the directory). Default: - no file is passed
        :param image_tag: The docker image tag to use for tagging pushed images. This field is required if ``imageParameterName`` is ommited (otherwise, the app won't be able to find the image). Default: - this parameter is REQUIRED after 1.21.0
        :param network_mode: Networking mode for the RUN commands during build. Default: - no networking mode specified
        :param outputs: Outputs to pass to the ``docker build`` command. Default: - no outputs are passed to the build command (default outputs are used)
        :param platform: Platform to build for. *Requires Docker Buildx*. Default: - current machine platform
        :param repository_name: ECR repository name, if omitted a default name based on the asset's ID is used instead. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - this parameter is REQUIRED after 1.21.0
        :param target: Docker target to build to. Default: no build target

        Example::

            entry = {
                "packaging": "container-image",
                "repository_name": "repository-name",
                "image_tag": "tag"
            }
        '''
        if isinstance(cache_to, dict):
            cache_to = ContainerImageAssetCacheOption(**cache_to)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5331a5e47b1bb2aafb851bd548f765940424af583650927b525fa39d04be4a8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument source_hash", value=source_hash, expected_type=type_hints["source_hash"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument build_secrets", value=build_secrets, expected_type=type_hints["build_secrets"])
            check_type(argname="argument build_ssh", value=build_ssh, expected_type=type_hints["build_ssh"])
            check_type(argname="argument cache_from", value=cache_from, expected_type=type_hints["cache_from"])
            check_type(argname="argument cache_to", value=cache_to, expected_type=type_hints["cache_to"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "packaging": packaging,
            "path": path,
            "source_hash": source_hash,
        }
        if build_args is not None:
            self._values["build_args"] = build_args
        if build_secrets is not None:
            self._values["build_secrets"] = build_secrets
        if build_ssh is not None:
            self._values["build_ssh"] = build_ssh
        if cache_from is not None:
            self._values["cache_from"] = cache_from
        if cache_to is not None:
            self._values["cache_to"] = cache_to
        if file is not None:
            self._values["file"] = file
        if image_tag is not None:
            self._values["image_tag"] = image_tag
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if outputs is not None:
            self._values["outputs"] = outputs
        if platform is not None:
            self._values["platform"] = platform
        if repository_name is not None:
            self._values["repository_name"] = repository_name
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def id(self) -> builtins.str:
        '''Logical identifier for the asset.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging(self) -> builtins.str:
        '''Type of asset.'''
        result = self._values.get("packaging")
        assert result is not None, "Required property 'packaging' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path on disk to the asset.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_hash(self) -> builtins.str:
        '''The hash of the asset source.'''
        result = self._values.get("source_hash")
        assert result is not None, "Required property 'source_hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build args to pass to the ``docker build`` command.

        :default: no build args are passed
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_secrets(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build secrets to pass to the ``docker build`` command.

        :default: no build secrets are passed
        '''
        result = self._values.get("build_secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_ssh(self) -> typing.Optional[builtins.str]:
        '''SSH agent socket or keys to pass to the ``docker build`` command.

        :default: no ssh arg is passed
        '''
        result = self._values.get("build_ssh")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_from(
        self,
    ) -> typing.Optional[typing.List[ContainerImageAssetCacheOption]]:
        '''Cache from options to pass to the ``docker build`` command.

        :default: - no cache from options are passed to the build command

        :see: https://docs.docker.com/build/cache/backends/
        '''
        result = self._values.get("cache_from")
        return typing.cast(typing.Optional[typing.List[ContainerImageAssetCacheOption]], result)

    @builtins.property
    def cache_to(self) -> typing.Optional[ContainerImageAssetCacheOption]:
        '''Cache to options to pass to the ``docker build`` command.

        :default: - no cache to options are passed to the build command

        :see: https://docs.docker.com/build/cache/backends/
        '''
        result = self._values.get("cache_to")
        return typing.cast(typing.Optional[ContainerImageAssetCacheOption], result)

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        '''Path to the Dockerfile (relative to the directory).

        :default: - no file is passed
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_tag(self) -> typing.Optional[builtins.str]:
        '''The docker image tag to use for tagging pushed images.

        This field is
        required if ``imageParameterName`` is ommited (otherwise, the app won't be
        able to find the image).

        :default: - this parameter is REQUIRED after 1.21.0
        '''
        result = self._values.get("image_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Networking mode for the RUN commands during build.

        :default: - no networking mode specified
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Outputs to pass to the ``docker build`` command.

        :default: - no outputs are passed to the build command (default outputs are used)

        :see: https://docs.docker.com/engine/reference/commandline/build/#custom-build-outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Platform to build for.

        *Requires Docker Buildx*.

        :default: - current machine platform
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''ECR repository name, if omitted a default name based on the asset's ID is used instead.

        Specify this property if you need to statically address the
        image, e.g. from a Kubernetes Pod. Note, this is only the repository name,
        without the registry and the tag parts.

        :default: - this parameter is REQUIRED after 1.21.0
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docker target to build to.

        :default: no build target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerImageAssetMetadataEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.ContextProvider")
class ContextProvider(enum.Enum):
    '''Identifier for the context provider.'''

    AMI_PROVIDER = "AMI_PROVIDER"
    '''AMI provider.'''
    AVAILABILITY_ZONE_PROVIDER = "AVAILABILITY_ZONE_PROVIDER"
    '''AZ provider.'''
    HOSTED_ZONE_PROVIDER = "HOSTED_ZONE_PROVIDER"
    '''Route53 Hosted Zone provider.'''
    SSM_PARAMETER_PROVIDER = "SSM_PARAMETER_PROVIDER"
    '''SSM Parameter Provider.'''
    VPC_PROVIDER = "VPC_PROVIDER"
    '''VPC Provider.'''
    ENDPOINT_SERVICE_AVAILABILITY_ZONE_PROVIDER = "ENDPOINT_SERVICE_AVAILABILITY_ZONE_PROVIDER"
    '''VPC Endpoint Service AZ Provider.'''
    LOAD_BALANCER_PROVIDER = "LOAD_BALANCER_PROVIDER"
    '''Load balancer provider.'''
    LOAD_BALANCER_LISTENER_PROVIDER = "LOAD_BALANCER_LISTENER_PROVIDER"
    '''Load balancer listener provider.'''
    SECURITY_GROUP_PROVIDER = "SECURITY_GROUP_PROVIDER"
    '''Security group provider.'''
    KEY_PROVIDER = "KEY_PROVIDER"
    '''KMS Key Provider.'''
    PLUGIN = "PLUGIN"
    '''A plugin provider (the actual plugin name will be in the properties).'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DefaultCdkOptions",
    jsii_struct_bases=[],
    name_mapping={
        "all": "all",
        "app": "app",
        "asset_metadata": "assetMetadata",
        "ca_bundle_path": "caBundlePath",
        "color": "color",
        "context": "context",
        "debug": "debug",
        "ec2_creds": "ec2Creds",
        "ignore_errors": "ignoreErrors",
        "json": "json",
        "lookups": "lookups",
        "notices": "notices",
        "output": "output",
        "path_metadata": "pathMetadata",
        "profile": "profile",
        "proxy": "proxy",
        "role_arn": "roleArn",
        "stacks": "stacks",
        "staging": "staging",
        "strict": "strict",
        "trace": "trace",
        "verbose": "verbose",
        "version_reporting": "versionReporting",
    },
)
class DefaultCdkOptions:
    def __init__(
        self,
        *,
        all: typing.Optional[builtins.bool] = None,
        app: typing.Optional[builtins.str] = None,
        asset_metadata: typing.Optional[builtins.bool] = None,
        ca_bundle_path: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        debug: typing.Optional[builtins.bool] = None,
        ec2_creds: typing.Optional[builtins.bool] = None,
        ignore_errors: typing.Optional[builtins.bool] = None,
        json: typing.Optional[builtins.bool] = None,
        lookups: typing.Optional[builtins.bool] = None,
        notices: typing.Optional[builtins.bool] = None,
        output: typing.Optional[builtins.str] = None,
        path_metadata: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        stacks: typing.Optional[typing.Sequence[builtins.str]] = None,
        staging: typing.Optional[builtins.bool] = None,
        strict: typing.Optional[builtins.bool] = None,
        trace: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
        version_reporting: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Default CDK CLI options that apply to all commands.

        :param all: Deploy all stacks. Requried if ``stacks`` is not set Default: - false
        :param app: command-line for executing your app or a cloud assembly directory e.g. "node bin/my-app.js" or "cdk.out". Default: - read from cdk.json
        :param asset_metadata: Include "aws:asset:*" CloudFormation metadata for resources that use assets. Default: true
        :param ca_bundle_path: Path to CA certificate to use when validating HTTPS requests. Default: - read from AWS_CA_BUNDLE environment variable
        :param color: Show colors and other style from console output. Default: true
        :param context: Additional context. Default: - no additional context
        :param debug: enable emission of additional debugging information, such as creation stack traces of tokens. Default: false
        :param ec2_creds: Force trying to fetch EC2 instance credentials. Default: - guess EC2 instance status
        :param ignore_errors: Ignores synthesis errors, which will likely produce an invalid output. Default: false
        :param json: Use JSON output instead of YAML when templates are printed to STDOUT. Default: false
        :param lookups: Perform context lookups. Synthesis fails if this is disabled and context lookups need to be performed Default: true
        :param notices: Show relevant notices. Default: true
        :param output: Emits the synthesized cloud assembly into a directory. Default: cdk.out
        :param path_metadata: Include "aws:cdk:path" CloudFormation metadata for each resource. Default: true
        :param profile: Use the indicated AWS profile as the default environment. Default: - no profile is used
        :param proxy: Use the indicated proxy. Will read from HTTPS_PROXY environment if specified Default: - no proxy
        :param role_arn: Role to pass to CloudFormation for deployment. Default: - use the bootstrap cfn-exec role
        :param stacks: List of stacks to deploy. Requried if ``all`` is not set Default: - []
        :param staging: Copy assets to the output directory. Needed for local debugging the source files with SAM CLI Default: false
        :param strict: Do not construct stacks with warnings. Default: false
        :param trace: Print trace for stack warnings. Default: false
        :param verbose: show debug logs. Default: false
        :param version_reporting: Include "AWS::CDK::Metadata" resource in synthesized templates. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            default_cdk_options = cloud_assembly_schema.DefaultCdkOptions(
                all=False,
                app="app",
                asset_metadata=False,
                ca_bundle_path="caBundlePath",
                color=False,
                context={
                    "context_key": "context"
                },
                debug=False,
                ec2_creds=False,
                ignore_errors=False,
                json=False,
                lookups=False,
                notices=False,
                output="output",
                path_metadata=False,
                profile="profile",
                proxy="proxy",
                role_arn="roleArn",
                stacks=["stacks"],
                staging=False,
                strict=False,
                trace=False,
                verbose=False,
                version_reporting=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594ca36867231e310239038fdad0490ae5b2dfc45ce83bd893a483d4e4b5e150)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument app", value=app, expected_type=type_hints["app"])
            check_type(argname="argument asset_metadata", value=asset_metadata, expected_type=type_hints["asset_metadata"])
            check_type(argname="argument ca_bundle_path", value=ca_bundle_path, expected_type=type_hints["ca_bundle_path"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument debug", value=debug, expected_type=type_hints["debug"])
            check_type(argname="argument ec2_creds", value=ec2_creds, expected_type=type_hints["ec2_creds"])
            check_type(argname="argument ignore_errors", value=ignore_errors, expected_type=type_hints["ignore_errors"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
            check_type(argname="argument lookups", value=lookups, expected_type=type_hints["lookups"])
            check_type(argname="argument notices", value=notices, expected_type=type_hints["notices"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument path_metadata", value=path_metadata, expected_type=type_hints["path_metadata"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument staging", value=staging, expected_type=type_hints["staging"])
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
            check_type(argname="argument version_reporting", value=version_reporting, expected_type=type_hints["version_reporting"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if app is not None:
            self._values["app"] = app
        if asset_metadata is not None:
            self._values["asset_metadata"] = asset_metadata
        if ca_bundle_path is not None:
            self._values["ca_bundle_path"] = ca_bundle_path
        if color is not None:
            self._values["color"] = color
        if context is not None:
            self._values["context"] = context
        if debug is not None:
            self._values["debug"] = debug
        if ec2_creds is not None:
            self._values["ec2_creds"] = ec2_creds
        if ignore_errors is not None:
            self._values["ignore_errors"] = ignore_errors
        if json is not None:
            self._values["json"] = json
        if lookups is not None:
            self._values["lookups"] = lookups
        if notices is not None:
            self._values["notices"] = notices
        if output is not None:
            self._values["output"] = output
        if path_metadata is not None:
            self._values["path_metadata"] = path_metadata
        if profile is not None:
            self._values["profile"] = profile
        if proxy is not None:
            self._values["proxy"] = proxy
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if stacks is not None:
            self._values["stacks"] = stacks
        if staging is not None:
            self._values["staging"] = staging
        if strict is not None:
            self._values["strict"] = strict
        if trace is not None:
            self._values["trace"] = trace
        if verbose is not None:
            self._values["verbose"] = verbose
        if version_reporting is not None:
            self._values["version_reporting"] = version_reporting

    @builtins.property
    def all(self) -> typing.Optional[builtins.bool]:
        '''Deploy all stacks.

        Requried if ``stacks`` is not set

        :default: - false
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def app(self) -> typing.Optional[builtins.str]:
        '''command-line for executing your app or a cloud assembly directory e.g. "node bin/my-app.js" or "cdk.out".

        :default: - read from cdk.json
        '''
        result = self._values.get("app")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include "aws:asset:*" CloudFormation metadata for resources that use assets.

        :default: true
        '''
        result = self._values.get("asset_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ca_bundle_path(self) -> typing.Optional[builtins.str]:
        '''Path to CA certificate to use when validating HTTPS requests.

        :default: - read from AWS_CA_BUNDLE environment variable
        '''
        result = self._values.get("ca_bundle_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.bool]:
        '''Show colors and other style from console output.

        :default: true
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional context.

        :default: - no additional context
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def debug(self) -> typing.Optional[builtins.bool]:
        '''enable emission of additional debugging information, such as creation stack traces of tokens.

        :default: false
        '''
        result = self._values.get("debug")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ec2_creds(self) -> typing.Optional[builtins.bool]:
        '''Force trying to fetch EC2 instance credentials.

        :default: - guess EC2 instance status
        '''
        result = self._values.get("ec2_creds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_errors(self) -> typing.Optional[builtins.bool]:
        '''Ignores synthesis errors, which will likely produce an invalid output.

        :default: false
        '''
        result = self._values.get("ignore_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def json(self) -> typing.Optional[builtins.bool]:
        '''Use JSON output instead of YAML when templates are printed to STDOUT.

        :default: false
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lookups(self) -> typing.Optional[builtins.bool]:
        '''Perform context lookups.

        Synthesis fails if this is disabled and context lookups need
        to be performed

        :default: true
        '''
        result = self._values.get("lookups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notices(self) -> typing.Optional[builtins.bool]:
        '''Show relevant notices.

        :default: true
        '''
        result = self._values.get("notices")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def output(self) -> typing.Optional[builtins.str]:
        '''Emits the synthesized cloud assembly into a directory.

        :default: cdk.out
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include "aws:cdk:path" CloudFormation metadata for each resource.

        :default: true
        '''
        result = self._values.get("path_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Use the indicated AWS profile as the default environment.

        :default: - no profile is used
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy(self) -> typing.Optional[builtins.str]:
        '''Use the indicated proxy.

        Will read from
        HTTPS_PROXY environment if specified

        :default: - no proxy
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Role to pass to CloudFormation for deployment.

        :default: - use the bootstrap cfn-exec role
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stacks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of stacks to deploy.

        Requried if ``all`` is not set

        :default: - []
        '''
        result = self._values.get("stacks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def staging(self) -> typing.Optional[builtins.bool]:
        '''Copy assets to the output directory.

        Needed for local debugging the source files with SAM CLI

        :default: false
        '''
        result = self._values.get("staging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def strict(self) -> typing.Optional[builtins.bool]:
        '''Do not construct stacks with warnings.

        :default: false
        '''
        result = self._values.get("strict")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def trace(self) -> typing.Optional[builtins.bool]:
        '''Print trace for stack warnings.

        :default: false
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def verbose(self) -> typing.Optional[builtins.bool]:
        '''show debug logs.

        :default: false
        '''
        result = self._values.get("verbose")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include "AWS::CDK::Metadata" resource in synthesized templates.

        :default: true
        '''
        result = self._values.get("version_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultCdkOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DeployCommand",
    jsii_struct_bases=[CdkCommand],
    name_mapping={
        "enabled": "enabled",
        "expected_message": "expectedMessage",
        "expect_error": "expectError",
        "args": "args",
    },
)
class DeployCommand(CdkCommand):
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        expected_message: typing.Optional[builtins.str] = None,
        expect_error: typing.Optional[builtins.bool] = None,
        args: typing.Optional[typing.Union["DeployOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Represents a cdk deploy command.

        :param enabled: Whether or not to run this command as part of the workflow This can be used if you only want to test some of the workflow for example enable ``synth`` and disable ``deploy`` & ``destroy`` in order to limit the test to synthesis. Default: true
        :param expected_message: This can be used in combination with ``expectedError`` to validate that a specific message is returned. Default: - do not validate message
        :param expect_error: If the runner should expect this command to fail. Default: false
        :param args: Additional arguments to pass to the command This can be used to test specific CLI functionality. Default: - only default args are used

        :exampleMetadata: infused

        Example::

            app = App()
            
            stack_under_test = Stack(app, "StackUnderTest")
            
            stack = Stack(app, "stack")
            
            test_case = IntegTest(app, "CustomizedDeploymentWorkflow",
                test_cases=[stack_under_test],
                diff_assets=True,
                stack_update_workflow=True,
                cdk_command_options=CdkCommands(
                    deploy=DeployCommand(
                        args=DeployOptions(
                            require_approval=RequireApproval.NEVER,
                            json=True
                        )
                    ),
                    destroy=DestroyCommand(
                        args=DestroyOptions(
                            force=True
                        )
                    )
                )
            )
        '''
        if isinstance(args, dict):
            args = DeployOptions(**args)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c759005400637b5bd106a020b90be905666b7bd21223ad43cd2dc6c3dff6d68e)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument expected_message", value=expected_message, expected_type=type_hints["expected_message"])
            check_type(argname="argument expect_error", value=expect_error, expected_type=type_hints["expect_error"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if expected_message is not None:
            self._values["expected_message"] = expected_message
        if expect_error is not None:
            self._values["expect_error"] = expect_error
        if args is not None:
            self._values["args"] = args

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to run this command as part of the workflow This can be used if you only want to test some of the workflow for example enable ``synth`` and disable ``deploy`` & ``destroy`` in order to limit the test to synthesis.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expected_message(self) -> typing.Optional[builtins.str]:
        '''This can be used in combination with ``expectedError`` to validate that a specific message is returned.

        :default: - do not validate message
        '''
        result = self._values.get("expected_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expect_error(self) -> typing.Optional[builtins.bool]:
        '''If the runner should expect this command to fail.

        :default: false
        '''
        result = self._values.get("expect_error")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def args(self) -> typing.Optional["DeployOptions"]:
        '''Additional arguments to pass to the command This can be used to test specific CLI functionality.

        :default: - only default args are used
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional["DeployOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeployCommand(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DeployOptions",
    jsii_struct_bases=[DefaultCdkOptions],
    name_mapping={
        "all": "all",
        "app": "app",
        "asset_metadata": "assetMetadata",
        "ca_bundle_path": "caBundlePath",
        "color": "color",
        "context": "context",
        "debug": "debug",
        "ec2_creds": "ec2Creds",
        "ignore_errors": "ignoreErrors",
        "json": "json",
        "lookups": "lookups",
        "notices": "notices",
        "output": "output",
        "path_metadata": "pathMetadata",
        "profile": "profile",
        "proxy": "proxy",
        "role_arn": "roleArn",
        "stacks": "stacks",
        "staging": "staging",
        "strict": "strict",
        "trace": "trace",
        "verbose": "verbose",
        "version_reporting": "versionReporting",
        "change_set_name": "changeSetName",
        "ci": "ci",
        "exclusively": "exclusively",
        "execute": "execute",
        "force": "force",
        "notification_arns": "notificationArns",
        "outputs_file": "outputsFile",
        "parameters": "parameters",
        "require_approval": "requireApproval",
        "reuse_assets": "reuseAssets",
        "rollback": "rollback",
        "toolkit_stack_name": "toolkitStackName",
        "use_previous_parameters": "usePreviousParameters",
    },
)
class DeployOptions(DefaultCdkOptions):
    def __init__(
        self,
        *,
        all: typing.Optional[builtins.bool] = None,
        app: typing.Optional[builtins.str] = None,
        asset_metadata: typing.Optional[builtins.bool] = None,
        ca_bundle_path: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        debug: typing.Optional[builtins.bool] = None,
        ec2_creds: typing.Optional[builtins.bool] = None,
        ignore_errors: typing.Optional[builtins.bool] = None,
        json: typing.Optional[builtins.bool] = None,
        lookups: typing.Optional[builtins.bool] = None,
        notices: typing.Optional[builtins.bool] = None,
        output: typing.Optional[builtins.str] = None,
        path_metadata: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        stacks: typing.Optional[typing.Sequence[builtins.str]] = None,
        staging: typing.Optional[builtins.bool] = None,
        strict: typing.Optional[builtins.bool] = None,
        trace: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
        version_reporting: typing.Optional[builtins.bool] = None,
        change_set_name: typing.Optional[builtins.str] = None,
        ci: typing.Optional[builtins.bool] = None,
        exclusively: typing.Optional[builtins.bool] = None,
        execute: typing.Optional[builtins.bool] = None,
        force: typing.Optional[builtins.bool] = None,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        outputs_file: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        require_approval: typing.Optional["RequireApproval"] = None,
        reuse_assets: typing.Optional[typing.Sequence[builtins.str]] = None,
        rollback: typing.Optional[builtins.bool] = None,
        toolkit_stack_name: typing.Optional[builtins.str] = None,
        use_previous_parameters: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options to use with cdk deploy.

        :param all: Deploy all stacks. Requried if ``stacks`` is not set Default: - false
        :param app: command-line for executing your app or a cloud assembly directory e.g. "node bin/my-app.js" or "cdk.out". Default: - read from cdk.json
        :param asset_metadata: Include "aws:asset:*" CloudFormation metadata for resources that use assets. Default: true
        :param ca_bundle_path: Path to CA certificate to use when validating HTTPS requests. Default: - read from AWS_CA_BUNDLE environment variable
        :param color: Show colors and other style from console output. Default: true
        :param context: Additional context. Default: - no additional context
        :param debug: enable emission of additional debugging information, such as creation stack traces of tokens. Default: false
        :param ec2_creds: Force trying to fetch EC2 instance credentials. Default: - guess EC2 instance status
        :param ignore_errors: Ignores synthesis errors, which will likely produce an invalid output. Default: false
        :param json: Use JSON output instead of YAML when templates are printed to STDOUT. Default: false
        :param lookups: Perform context lookups. Synthesis fails if this is disabled and context lookups need to be performed Default: true
        :param notices: Show relevant notices. Default: true
        :param output: Emits the synthesized cloud assembly into a directory. Default: cdk.out
        :param path_metadata: Include "aws:cdk:path" CloudFormation metadata for each resource. Default: true
        :param profile: Use the indicated AWS profile as the default environment. Default: - no profile is used
        :param proxy: Use the indicated proxy. Will read from HTTPS_PROXY environment if specified Default: - no proxy
        :param role_arn: Role to pass to CloudFormation for deployment. Default: - use the bootstrap cfn-exec role
        :param stacks: List of stacks to deploy. Requried if ``all`` is not set Default: - []
        :param staging: Copy assets to the output directory. Needed for local debugging the source files with SAM CLI Default: false
        :param strict: Do not construct stacks with warnings. Default: false
        :param trace: Print trace for stack warnings. Default: false
        :param verbose: show debug logs. Default: false
        :param version_reporting: Include "AWS::CDK::Metadata" resource in synthesized templates. Default: true
        :param change_set_name: Optional name to use for the CloudFormation change set. If not provided, a name will be generated automatically. Default: - auto generate a name
        :param ci: Whether we are on a CI system. Default: false
        :param exclusively: Only perform action on the given stack. Default: false
        :param execute: Whether to execute the ChangeSet Not providing ``execute`` parameter will result in execution of ChangeSet. Default: true
        :param force: Always deploy, even if templates are identical. Default: false
        :param notification_arns: ARNs of SNS topics that CloudFormation will notify with stack related events. Default: - no notifications
        :param outputs_file: Path to file where stack outputs will be written after a successful deploy as JSON. Default: - Outputs are not written to any file
        :param parameters: Additional parameters for CloudFormation at deploy time. Default: {}
        :param require_approval: What kind of security changes require approval. Default: RequireApproval.Never
        :param reuse_assets: Reuse the assets with the given asset IDs. Default: - do not reuse assets
        :param rollback: Rollback failed deployments. Default: true
        :param toolkit_stack_name: Name of the toolkit stack to use/deploy. Default: CDKToolkit
        :param use_previous_parameters: Use previous values for unspecified parameters. If not set, all parameters must be specified for every deployment. Default: true

        :exampleMetadata: infused

        Example::

            app = App()
            
            stack_under_test = Stack(app, "StackUnderTest")
            
            stack = Stack(app, "stack")
            
            test_case = IntegTest(app, "CustomizedDeploymentWorkflow",
                test_cases=[stack_under_test],
                diff_assets=True,
                stack_update_workflow=True,
                cdk_command_options=CdkCommands(
                    deploy=DeployCommand(
                        args=DeployOptions(
                            require_approval=RequireApproval.NEVER,
                            json=True
                        )
                    ),
                    destroy=DestroyCommand(
                        args=DestroyOptions(
                            force=True
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e316f5465c42282e55b82d44529c7add374f8a6fee37838b3b05b930dea1b804)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument app", value=app, expected_type=type_hints["app"])
            check_type(argname="argument asset_metadata", value=asset_metadata, expected_type=type_hints["asset_metadata"])
            check_type(argname="argument ca_bundle_path", value=ca_bundle_path, expected_type=type_hints["ca_bundle_path"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument debug", value=debug, expected_type=type_hints["debug"])
            check_type(argname="argument ec2_creds", value=ec2_creds, expected_type=type_hints["ec2_creds"])
            check_type(argname="argument ignore_errors", value=ignore_errors, expected_type=type_hints["ignore_errors"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
            check_type(argname="argument lookups", value=lookups, expected_type=type_hints["lookups"])
            check_type(argname="argument notices", value=notices, expected_type=type_hints["notices"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument path_metadata", value=path_metadata, expected_type=type_hints["path_metadata"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument staging", value=staging, expected_type=type_hints["staging"])
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
            check_type(argname="argument version_reporting", value=version_reporting, expected_type=type_hints["version_reporting"])
            check_type(argname="argument change_set_name", value=change_set_name, expected_type=type_hints["change_set_name"])
            check_type(argname="argument ci", value=ci, expected_type=type_hints["ci"])
            check_type(argname="argument exclusively", value=exclusively, expected_type=type_hints["exclusively"])
            check_type(argname="argument execute", value=execute, expected_type=type_hints["execute"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument notification_arns", value=notification_arns, expected_type=type_hints["notification_arns"])
            check_type(argname="argument outputs_file", value=outputs_file, expected_type=type_hints["outputs_file"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument require_approval", value=require_approval, expected_type=type_hints["require_approval"])
            check_type(argname="argument reuse_assets", value=reuse_assets, expected_type=type_hints["reuse_assets"])
            check_type(argname="argument rollback", value=rollback, expected_type=type_hints["rollback"])
            check_type(argname="argument toolkit_stack_name", value=toolkit_stack_name, expected_type=type_hints["toolkit_stack_name"])
            check_type(argname="argument use_previous_parameters", value=use_previous_parameters, expected_type=type_hints["use_previous_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if app is not None:
            self._values["app"] = app
        if asset_metadata is not None:
            self._values["asset_metadata"] = asset_metadata
        if ca_bundle_path is not None:
            self._values["ca_bundle_path"] = ca_bundle_path
        if color is not None:
            self._values["color"] = color
        if context is not None:
            self._values["context"] = context
        if debug is not None:
            self._values["debug"] = debug
        if ec2_creds is not None:
            self._values["ec2_creds"] = ec2_creds
        if ignore_errors is not None:
            self._values["ignore_errors"] = ignore_errors
        if json is not None:
            self._values["json"] = json
        if lookups is not None:
            self._values["lookups"] = lookups
        if notices is not None:
            self._values["notices"] = notices
        if output is not None:
            self._values["output"] = output
        if path_metadata is not None:
            self._values["path_metadata"] = path_metadata
        if profile is not None:
            self._values["profile"] = profile
        if proxy is not None:
            self._values["proxy"] = proxy
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if stacks is not None:
            self._values["stacks"] = stacks
        if staging is not None:
            self._values["staging"] = staging
        if strict is not None:
            self._values["strict"] = strict
        if trace is not None:
            self._values["trace"] = trace
        if verbose is not None:
            self._values["verbose"] = verbose
        if version_reporting is not None:
            self._values["version_reporting"] = version_reporting
        if change_set_name is not None:
            self._values["change_set_name"] = change_set_name
        if ci is not None:
            self._values["ci"] = ci
        if exclusively is not None:
            self._values["exclusively"] = exclusively
        if execute is not None:
            self._values["execute"] = execute
        if force is not None:
            self._values["force"] = force
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if outputs_file is not None:
            self._values["outputs_file"] = outputs_file
        if parameters is not None:
            self._values["parameters"] = parameters
        if require_approval is not None:
            self._values["require_approval"] = require_approval
        if reuse_assets is not None:
            self._values["reuse_assets"] = reuse_assets
        if rollback is not None:
            self._values["rollback"] = rollback
        if toolkit_stack_name is not None:
            self._values["toolkit_stack_name"] = toolkit_stack_name
        if use_previous_parameters is not None:
            self._values["use_previous_parameters"] = use_previous_parameters

    @builtins.property
    def all(self) -> typing.Optional[builtins.bool]:
        '''Deploy all stacks.

        Requried if ``stacks`` is not set

        :default: - false
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def app(self) -> typing.Optional[builtins.str]:
        '''command-line for executing your app or a cloud assembly directory e.g. "node bin/my-app.js" or "cdk.out".

        :default: - read from cdk.json
        '''
        result = self._values.get("app")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include "aws:asset:*" CloudFormation metadata for resources that use assets.

        :default: true
        '''
        result = self._values.get("asset_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ca_bundle_path(self) -> typing.Optional[builtins.str]:
        '''Path to CA certificate to use when validating HTTPS requests.

        :default: - read from AWS_CA_BUNDLE environment variable
        '''
        result = self._values.get("ca_bundle_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.bool]:
        '''Show colors and other style from console output.

        :default: true
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional context.

        :default: - no additional context
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def debug(self) -> typing.Optional[builtins.bool]:
        '''enable emission of additional debugging information, such as creation stack traces of tokens.

        :default: false
        '''
        result = self._values.get("debug")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ec2_creds(self) -> typing.Optional[builtins.bool]:
        '''Force trying to fetch EC2 instance credentials.

        :default: - guess EC2 instance status
        '''
        result = self._values.get("ec2_creds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_errors(self) -> typing.Optional[builtins.bool]:
        '''Ignores synthesis errors, which will likely produce an invalid output.

        :default: false
        '''
        result = self._values.get("ignore_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def json(self) -> typing.Optional[builtins.bool]:
        '''Use JSON output instead of YAML when templates are printed to STDOUT.

        :default: false
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lookups(self) -> typing.Optional[builtins.bool]:
        '''Perform context lookups.

        Synthesis fails if this is disabled and context lookups need
        to be performed

        :default: true
        '''
        result = self._values.get("lookups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notices(self) -> typing.Optional[builtins.bool]:
        '''Show relevant notices.

        :default: true
        '''
        result = self._values.get("notices")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def output(self) -> typing.Optional[builtins.str]:
        '''Emits the synthesized cloud assembly into a directory.

        :default: cdk.out
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include "aws:cdk:path" CloudFormation metadata for each resource.

        :default: true
        '''
        result = self._values.get("path_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Use the indicated AWS profile as the default environment.

        :default: - no profile is used
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy(self) -> typing.Optional[builtins.str]:
        '''Use the indicated proxy.

        Will read from
        HTTPS_PROXY environment if specified

        :default: - no proxy
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Role to pass to CloudFormation for deployment.

        :default: - use the bootstrap cfn-exec role
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stacks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of stacks to deploy.

        Requried if ``all`` is not set

        :default: - []
        '''
        result = self._values.get("stacks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def staging(self) -> typing.Optional[builtins.bool]:
        '''Copy assets to the output directory.

        Needed for local debugging the source files with SAM CLI

        :default: false
        '''
        result = self._values.get("staging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def strict(self) -> typing.Optional[builtins.bool]:
        '''Do not construct stacks with warnings.

        :default: false
        '''
        result = self._values.get("strict")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def trace(self) -> typing.Optional[builtins.bool]:
        '''Print trace for stack warnings.

        :default: false
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def verbose(self) -> typing.Optional[builtins.bool]:
        '''show debug logs.

        :default: false
        '''
        result = self._values.get("verbose")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include "AWS::CDK::Metadata" resource in synthesized templates.

        :default: true
        '''
        result = self._values.get("version_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def change_set_name(self) -> typing.Optional[builtins.str]:
        '''Optional name to use for the CloudFormation change set.

        If not provided, a name will be generated automatically.

        :default: - auto generate a name
        '''
        result = self._values.get("change_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ci(self) -> typing.Optional[builtins.bool]:
        '''Whether we are on a CI system.

        :default: false
        '''
        result = self._values.get("ci")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exclusively(self) -> typing.Optional[builtins.bool]:
        '''Only perform action on the given stack.

        :default: false
        '''
        result = self._values.get("exclusively")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def execute(self) -> typing.Optional[builtins.bool]:
        '''Whether to execute the ChangeSet Not providing ``execute`` parameter will result in execution of ChangeSet.

        :default: true
        '''
        result = self._values.get("execute")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Always deploy, even if templates are identical.

        :default: false
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''ARNs of SNS topics that CloudFormation will notify with stack related events.

        :default: - no notifications
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outputs_file(self) -> typing.Optional[builtins.str]:
        '''Path to file where stack outputs will be written after a successful deploy as JSON.

        :default: - Outputs are not written to any file
        '''
        result = self._values.get("outputs_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional parameters for CloudFormation at deploy time.

        :default: {}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def require_approval(self) -> typing.Optional["RequireApproval"]:
        '''What kind of security changes require approval.

        :default: RequireApproval.Never
        '''
        result = self._values.get("require_approval")
        return typing.cast(typing.Optional["RequireApproval"], result)

    @builtins.property
    def reuse_assets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Reuse the assets with the given asset IDs.

        :default: - do not reuse assets
        '''
        result = self._values.get("reuse_assets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rollback(self) -> typing.Optional[builtins.bool]:
        '''Rollback failed deployments.

        :default: true
        '''
        result = self._values.get("rollback")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def toolkit_stack_name(self) -> typing.Optional[builtins.str]:
        '''Name of the toolkit stack to use/deploy.

        :default: CDKToolkit
        '''
        result = self._values.get("toolkit_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_previous_parameters(self) -> typing.Optional[builtins.bool]:
        '''Use previous values for unspecified parameters.

        If not set, all parameters must be specified for every deployment.

        :default: true
        '''
        result = self._values.get("use_previous_parameters")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeployOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DestroyCommand",
    jsii_struct_bases=[CdkCommand],
    name_mapping={
        "enabled": "enabled",
        "expected_message": "expectedMessage",
        "expect_error": "expectError",
        "args": "args",
    },
)
class DestroyCommand(CdkCommand):
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        expected_message: typing.Optional[builtins.str] = None,
        expect_error: typing.Optional[builtins.bool] = None,
        args: typing.Optional[typing.Union["DestroyOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Represents a cdk destroy command.

        :param enabled: Whether or not to run this command as part of the workflow This can be used if you only want to test some of the workflow for example enable ``synth`` and disable ``deploy`` & ``destroy`` in order to limit the test to synthesis. Default: true
        :param expected_message: This can be used in combination with ``expectedError`` to validate that a specific message is returned. Default: - do not validate message
        :param expect_error: If the runner should expect this command to fail. Default: false
        :param args: Additional arguments to pass to the command This can be used to test specific CLI functionality. Default: - only default args are used

        :exampleMetadata: infused

        Example::

            app = App()
            
            stack_under_test = Stack(app, "StackUnderTest")
            
            stack = Stack(app, "stack")
            
            test_case = IntegTest(app, "CustomizedDeploymentWorkflow",
                test_cases=[stack_under_test],
                diff_assets=True,
                stack_update_workflow=True,
                cdk_command_options=CdkCommands(
                    deploy=DeployCommand(
                        args=DeployOptions(
                            require_approval=RequireApproval.NEVER,
                            json=True
                        )
                    ),
                    destroy=DestroyCommand(
                        args=DestroyOptions(
                            force=True
                        )
                    )
                )
            )
        '''
        if isinstance(args, dict):
            args = DestroyOptions(**args)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d085522a7dd3e11de74ee4aabd4a610f704d28adf6c2243ef2a4196809a75cf2)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument expected_message", value=expected_message, expected_type=type_hints["expected_message"])
            check_type(argname="argument expect_error", value=expect_error, expected_type=type_hints["expect_error"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if expected_message is not None:
            self._values["expected_message"] = expected_message
        if expect_error is not None:
            self._values["expect_error"] = expect_error
        if args is not None:
            self._values["args"] = args

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to run this command as part of the workflow This can be used if you only want to test some of the workflow for example enable ``synth`` and disable ``deploy`` & ``destroy`` in order to limit the test to synthesis.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expected_message(self) -> typing.Optional[builtins.str]:
        '''This can be used in combination with ``expectedError`` to validate that a specific message is returned.

        :default: - do not validate message
        '''
        result = self._values.get("expected_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expect_error(self) -> typing.Optional[builtins.bool]:
        '''If the runner should expect this command to fail.

        :default: false
        '''
        result = self._values.get("expect_error")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def args(self) -> typing.Optional["DestroyOptions"]:
        '''Additional arguments to pass to the command This can be used to test specific CLI functionality.

        :default: - only default args are used
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional["DestroyOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestroyCommand(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DestroyOptions",
    jsii_struct_bases=[DefaultCdkOptions],
    name_mapping={
        "all": "all",
        "app": "app",
        "asset_metadata": "assetMetadata",
        "ca_bundle_path": "caBundlePath",
        "color": "color",
        "context": "context",
        "debug": "debug",
        "ec2_creds": "ec2Creds",
        "ignore_errors": "ignoreErrors",
        "json": "json",
        "lookups": "lookups",
        "notices": "notices",
        "output": "output",
        "path_metadata": "pathMetadata",
        "profile": "profile",
        "proxy": "proxy",
        "role_arn": "roleArn",
        "stacks": "stacks",
        "staging": "staging",
        "strict": "strict",
        "trace": "trace",
        "verbose": "verbose",
        "version_reporting": "versionReporting",
        "exclusively": "exclusively",
        "force": "force",
    },
)
class DestroyOptions(DefaultCdkOptions):
    def __init__(
        self,
        *,
        all: typing.Optional[builtins.bool] = None,
        app: typing.Optional[builtins.str] = None,
        asset_metadata: typing.Optional[builtins.bool] = None,
        ca_bundle_path: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        debug: typing.Optional[builtins.bool] = None,
        ec2_creds: typing.Optional[builtins.bool] = None,
        ignore_errors: typing.Optional[builtins.bool] = None,
        json: typing.Optional[builtins.bool] = None,
        lookups: typing.Optional[builtins.bool] = None,
        notices: typing.Optional[builtins.bool] = None,
        output: typing.Optional[builtins.str] = None,
        path_metadata: typing.Optional[builtins.bool] = None,
        profile: typing.Optional[builtins.str] = None,
        proxy: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        stacks: typing.Optional[typing.Sequence[builtins.str]] = None,
        staging: typing.Optional[builtins.bool] = None,
        strict: typing.Optional[builtins.bool] = None,
        trace: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
        version_reporting: typing.Optional[builtins.bool] = None,
        exclusively: typing.Optional[builtins.bool] = None,
        force: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options to use with cdk destroy.

        :param all: Deploy all stacks. Requried if ``stacks`` is not set Default: - false
        :param app: command-line for executing your app or a cloud assembly directory e.g. "node bin/my-app.js" or "cdk.out". Default: - read from cdk.json
        :param asset_metadata: Include "aws:asset:*" CloudFormation metadata for resources that use assets. Default: true
        :param ca_bundle_path: Path to CA certificate to use when validating HTTPS requests. Default: - read from AWS_CA_BUNDLE environment variable
        :param color: Show colors and other style from console output. Default: true
        :param context: Additional context. Default: - no additional context
        :param debug: enable emission of additional debugging information, such as creation stack traces of tokens. Default: false
        :param ec2_creds: Force trying to fetch EC2 instance credentials. Default: - guess EC2 instance status
        :param ignore_errors: Ignores synthesis errors, which will likely produce an invalid output. Default: false
        :param json: Use JSON output instead of YAML when templates are printed to STDOUT. Default: false
        :param lookups: Perform context lookups. Synthesis fails if this is disabled and context lookups need to be performed Default: true
        :param notices: Show relevant notices. Default: true
        :param output: Emits the synthesized cloud assembly into a directory. Default: cdk.out
        :param path_metadata: Include "aws:cdk:path" CloudFormation metadata for each resource. Default: true
        :param profile: Use the indicated AWS profile as the default environment. Default: - no profile is used
        :param proxy: Use the indicated proxy. Will read from HTTPS_PROXY environment if specified Default: - no proxy
        :param role_arn: Role to pass to CloudFormation for deployment. Default: - use the bootstrap cfn-exec role
        :param stacks: List of stacks to deploy. Requried if ``all`` is not set Default: - []
        :param staging: Copy assets to the output directory. Needed for local debugging the source files with SAM CLI Default: false
        :param strict: Do not construct stacks with warnings. Default: false
        :param trace: Print trace for stack warnings. Default: false
        :param verbose: show debug logs. Default: false
        :param version_reporting: Include "AWS::CDK::Metadata" resource in synthesized templates. Default: true
        :param exclusively: Only destroy the given stack. Default: false
        :param force: Do not ask for permission before destroying stacks. Default: false

        :exampleMetadata: infused

        Example::

            app = App()
            
            stack_under_test = Stack(app, "StackUnderTest")
            
            stack = Stack(app, "stack")
            
            test_case = IntegTest(app, "CustomizedDeploymentWorkflow",
                test_cases=[stack_under_test],
                diff_assets=True,
                stack_update_workflow=True,
                cdk_command_options=CdkCommands(
                    deploy=DeployCommand(
                        args=DeployOptions(
                            require_approval=RequireApproval.NEVER,
                            json=True
                        )
                    ),
                    destroy=DestroyCommand(
                        args=DestroyOptions(
                            force=True
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f6502d5a70ca8d3ae7dbec0f66d1e2813f2a50261460f2fd206c0533afdfabf)
            check_type(argname="argument all", value=all, expected_type=type_hints["all"])
            check_type(argname="argument app", value=app, expected_type=type_hints["app"])
            check_type(argname="argument asset_metadata", value=asset_metadata, expected_type=type_hints["asset_metadata"])
            check_type(argname="argument ca_bundle_path", value=ca_bundle_path, expected_type=type_hints["ca_bundle_path"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument debug", value=debug, expected_type=type_hints["debug"])
            check_type(argname="argument ec2_creds", value=ec2_creds, expected_type=type_hints["ec2_creds"])
            check_type(argname="argument ignore_errors", value=ignore_errors, expected_type=type_hints["ignore_errors"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
            check_type(argname="argument lookups", value=lookups, expected_type=type_hints["lookups"])
            check_type(argname="argument notices", value=notices, expected_type=type_hints["notices"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument path_metadata", value=path_metadata, expected_type=type_hints["path_metadata"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument staging", value=staging, expected_type=type_hints["staging"])
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
            check_type(argname="argument version_reporting", value=version_reporting, expected_type=type_hints["version_reporting"])
            check_type(argname="argument exclusively", value=exclusively, expected_type=type_hints["exclusively"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if all is not None:
            self._values["all"] = all
        if app is not None:
            self._values["app"] = app
        if asset_metadata is not None:
            self._values["asset_metadata"] = asset_metadata
        if ca_bundle_path is not None:
            self._values["ca_bundle_path"] = ca_bundle_path
        if color is not None:
            self._values["color"] = color
        if context is not None:
            self._values["context"] = context
        if debug is not None:
            self._values["debug"] = debug
        if ec2_creds is not None:
            self._values["ec2_creds"] = ec2_creds
        if ignore_errors is not None:
            self._values["ignore_errors"] = ignore_errors
        if json is not None:
            self._values["json"] = json
        if lookups is not None:
            self._values["lookups"] = lookups
        if notices is not None:
            self._values["notices"] = notices
        if output is not None:
            self._values["output"] = output
        if path_metadata is not None:
            self._values["path_metadata"] = path_metadata
        if profile is not None:
            self._values["profile"] = profile
        if proxy is not None:
            self._values["proxy"] = proxy
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if stacks is not None:
            self._values["stacks"] = stacks
        if staging is not None:
            self._values["staging"] = staging
        if strict is not None:
            self._values["strict"] = strict
        if trace is not None:
            self._values["trace"] = trace
        if verbose is not None:
            self._values["verbose"] = verbose
        if version_reporting is not None:
            self._values["version_reporting"] = version_reporting
        if exclusively is not None:
            self._values["exclusively"] = exclusively
        if force is not None:
            self._values["force"] = force

    @builtins.property
    def all(self) -> typing.Optional[builtins.bool]:
        '''Deploy all stacks.

        Requried if ``stacks`` is not set

        :default: - false
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def app(self) -> typing.Optional[builtins.str]:
        '''command-line for executing your app or a cloud assembly directory e.g. "node bin/my-app.js" or "cdk.out".

        :default: - read from cdk.json
        '''
        result = self._values.get("app")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include "aws:asset:*" CloudFormation metadata for resources that use assets.

        :default: true
        '''
        result = self._values.get("asset_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ca_bundle_path(self) -> typing.Optional[builtins.str]:
        '''Path to CA certificate to use when validating HTTPS requests.

        :default: - read from AWS_CA_BUNDLE environment variable
        '''
        result = self._values.get("ca_bundle_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.bool]:
        '''Show colors and other style from console output.

        :default: true
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional context.

        :default: - no additional context
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def debug(self) -> typing.Optional[builtins.bool]:
        '''enable emission of additional debugging information, such as creation stack traces of tokens.

        :default: false
        '''
        result = self._values.get("debug")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ec2_creds(self) -> typing.Optional[builtins.bool]:
        '''Force trying to fetch EC2 instance credentials.

        :default: - guess EC2 instance status
        '''
        result = self._values.get("ec2_creds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_errors(self) -> typing.Optional[builtins.bool]:
        '''Ignores synthesis errors, which will likely produce an invalid output.

        :default: false
        '''
        result = self._values.get("ignore_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def json(self) -> typing.Optional[builtins.bool]:
        '''Use JSON output instead of YAML when templates are printed to STDOUT.

        :default: false
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lookups(self) -> typing.Optional[builtins.bool]:
        '''Perform context lookups.

        Synthesis fails if this is disabled and context lookups need
        to be performed

        :default: true
        '''
        result = self._values.get("lookups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notices(self) -> typing.Optional[builtins.bool]:
        '''Show relevant notices.

        :default: true
        '''
        result = self._values.get("notices")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def output(self) -> typing.Optional[builtins.str]:
        '''Emits the synthesized cloud assembly into a directory.

        :default: cdk.out
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include "aws:cdk:path" CloudFormation metadata for each resource.

        :default: true
        '''
        result = self._values.get("path_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Use the indicated AWS profile as the default environment.

        :default: - no profile is used
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy(self) -> typing.Optional[builtins.str]:
        '''Use the indicated proxy.

        Will read from
        HTTPS_PROXY environment if specified

        :default: - no proxy
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Role to pass to CloudFormation for deployment.

        :default: - use the bootstrap cfn-exec role
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stacks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of stacks to deploy.

        Requried if ``all`` is not set

        :default: - []
        '''
        result = self._values.get("stacks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def staging(self) -> typing.Optional[builtins.bool]:
        '''Copy assets to the output directory.

        Needed for local debugging the source files with SAM CLI

        :default: false
        '''
        result = self._values.get("staging")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def strict(self) -> typing.Optional[builtins.bool]:
        '''Do not construct stacks with warnings.

        :default: false
        '''
        result = self._values.get("strict")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def trace(self) -> typing.Optional[builtins.bool]:
        '''Print trace for stack warnings.

        :default: false
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def verbose(self) -> typing.Optional[builtins.bool]:
        '''show debug logs.

        :default: false
        '''
        result = self._values.get("verbose")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include "AWS::CDK::Metadata" resource in synthesized templates.

        :default: true
        '''
        result = self._values.get("version_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exclusively(self) -> typing.Optional[builtins.bool]:
        '''Only destroy the given stack.

        :default: false
        '''
        result = self._values.get("exclusively")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Do not ask for permission before destroying stacks.

        :default: false
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestroyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DockerCacheOption",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "params": "params"},
)
class DockerCacheOption:
    def __init__(
        self,
        *,
        type: builtins.str,
        params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Options for configuring the Docker cache backend.

        :param type: The type of cache to use. Refer to https://docs.docker.com/build/cache/backends/ for full list of backends. Default: - unspecified
        :param params: Any parameters to pass into the docker cache backend configuration. Refer to https://docs.docker.com/build/cache/backends/ for cache backend configuration. Default: {} No options provided

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            docker_cache_option = cloud_assembly_schema.DockerCacheOption(
                type="type",
            
                # the properties below are optional
                params={
                    "params_key": "params"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cef84b1e278512e93714e32db5936e30b5b5b0d34a4c44fb2ed845b8cdd29792)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if params is not None:
            self._values["params"] = params

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of cache to use.

        Refer to https://docs.docker.com/build/cache/backends/ for full list of backends.

        :default: - unspecified

        Example::

            "registry"
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def params(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any parameters to pass into the docker cache backend configuration.

        Refer to https://docs.docker.com/build/cache/backends/ for cache backend configuration.

        :default: {} No options provided

        Example::

            # branch: str
            
            
            params = {
                "ref": f"12345678.dkr.ecr.us-west-2.amazonaws.com/cache:{branch}",
                "mode": "max"
            }
        '''
        result = self._values.get("params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerCacheOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DockerImageAsset",
    jsii_struct_bases=[],
    name_mapping={"destinations": "destinations", "source": "source"},
)
class DockerImageAsset:
    def __init__(
        self,
        *,
        destinations: typing.Mapping[builtins.str, typing.Union["DockerImageDestination", typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union["DockerImageSource", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''A file asset.

        :param destinations: Destinations for this file asset.
        :param source: Source description for file assets.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            docker_image_asset = cloud_assembly_schema.DockerImageAsset(
                destinations={
                    "destinations_key": cloud_assembly_schema.DockerImageDestination(
                        image_tag="imageTag",
                        repository_name="repositoryName",
            
                        # the properties below are optional
                        assume_role_arn="assumeRoleArn",
                        assume_role_external_id="assumeRoleExternalId",
                        region="region"
                    )
                },
                source=cloud_assembly_schema.DockerImageSource(
                    cache_from=[cloud_assembly_schema.DockerCacheOption(
                        type="type",
            
                        # the properties below are optional
                        params={
                            "params_key": "params"
                        }
                    )],
                    cache_to=cloud_assembly_schema.DockerCacheOption(
                        type="type",
            
                        # the properties below are optional
                        params={
                            "params_key": "params"
                        }
                    ),
                    directory="directory",
                    docker_build_args={
                        "docker_build_args_key": "dockerBuildArgs"
                    },
                    docker_build_secrets={
                        "docker_build_secrets_key": "dockerBuildSecrets"
                    },
                    docker_build_ssh="dockerBuildSsh",
                    docker_build_target="dockerBuildTarget",
                    docker_file="dockerFile",
                    docker_outputs=["dockerOutputs"],
                    executable=["executable"],
                    network_mode="networkMode",
                    platform="platform"
                )
            )
        '''
        if isinstance(source, dict):
            source = DockerImageSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18a2a085c0212f98043b6dccf8c92e1bdc5d9e20c7266a3be7bc908b8b771cd3)
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destinations": destinations,
            "source": source,
        }

    @builtins.property
    def destinations(self) -> typing.Mapping[builtins.str, "DockerImageDestination"]:
        '''Destinations for this file asset.'''
        result = self._values.get("destinations")
        assert result is not None, "Required property 'destinations' is missing"
        return typing.cast(typing.Mapping[builtins.str, "DockerImageDestination"], result)

    @builtins.property
    def source(self) -> "DockerImageSource":
        '''Source description for file assets.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("DockerImageSource", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageAsset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DockerImageDestination",
    jsii_struct_bases=[AwsDestination],
    name_mapping={
        "assume_role_arn": "assumeRoleArn",
        "assume_role_external_id": "assumeRoleExternalId",
        "region": "region",
        "image_tag": "imageTag",
        "repository_name": "repositoryName",
    },
)
class DockerImageDestination(AwsDestination):
    def __init__(
        self,
        *,
        assume_role_arn: typing.Optional[builtins.str] = None,
        assume_role_external_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        image_tag: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''Where to publish docker images.

        :param assume_role_arn: The role that needs to be assumed while publishing this asset. Default: - No role will be assumed
        :param assume_role_external_id: The ExternalId that needs to be supplied while assuming this role. Default: - No ExternalId will be supplied
        :param region: The region where this asset will need to be published. Default: - Current region
        :param image_tag: Tag of the image to publish.
        :param repository_name: Name of the ECR repository to publish to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            docker_image_destination = cloud_assembly_schema.DockerImageDestination(
                image_tag="imageTag",
                repository_name="repositoryName",
            
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01e136052f71999035d3e1605dff6c0878e98a56b1d1493de1cc03b20f38345a)
            check_type(argname="argument assume_role_arn", value=assume_role_arn, expected_type=type_hints["assume_role_arn"])
            check_type(argname="argument assume_role_external_id", value=assume_role_external_id, expected_type=type_hints["assume_role_external_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_tag": image_tag,
            "repository_name": repository_name,
        }
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if assume_role_external_id is not None:
            self._values["assume_role_external_id"] = assume_role_external_id
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that needs to be assumed while publishing this asset.

        :default: - No role will be assumed
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_external_id(self) -> typing.Optional[builtins.str]:
        '''The ExternalId that needs to be supplied while assuming this role.

        :default: - No ExternalId will be supplied
        '''
        result = self._values.get("assume_role_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where this asset will need to be published.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_tag(self) -> builtins.str:
        '''Tag of the image to publish.'''
        result = self._values.get("image_tag")
        assert result is not None, "Required property 'image_tag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''Name of the ECR repository to publish to.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.DockerImageSource",
    jsii_struct_bases=[],
    name_mapping={
        "cache_from": "cacheFrom",
        "cache_to": "cacheTo",
        "directory": "directory",
        "docker_build_args": "dockerBuildArgs",
        "docker_build_secrets": "dockerBuildSecrets",
        "docker_build_ssh": "dockerBuildSsh",
        "docker_build_target": "dockerBuildTarget",
        "docker_file": "dockerFile",
        "docker_outputs": "dockerOutputs",
        "executable": "executable",
        "network_mode": "networkMode",
        "platform": "platform",
    },
)
class DockerImageSource:
    def __init__(
        self,
        *,
        cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
        cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
        directory: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_ssh: typing.Optional[builtins.str] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        docker_outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for how to produce a Docker image from a source.

        :param cache_from: Cache from options to pass to the ``docker build`` command. Default: - no cache from options are passed to the build command
        :param cache_to: Cache to options to pass to the ``docker build`` command. Default: - no cache to options are passed to the build command
        :param directory: The directory containing the Docker image build instructions. This path is relative to the asset manifest location. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param docker_build_args: Additional build arguments. Only allowed when ``directory`` is set. Default: - No additional build arguments
        :param docker_build_secrets: Additional build secrets. Only allowed when ``directory`` is set. Default: - No additional build secrets
        :param docker_build_ssh: SSH agent socket or keys. Requires building with docker buildkit. Default: - No ssh flag is set
        :param docker_build_target: Target build stage in a Dockerfile with multiple build stages. Only allowed when ``directory`` is set. Default: - The last stage in the Dockerfile
        :param docker_file: The name of the file with build instructions. Only allowed when ``directory`` is set. Default: "Dockerfile"
        :param docker_outputs: Outputs. Default: - no outputs are passed to the build command (default outputs are used)
        :param executable: A command-line executable that returns the name of a local Docker image on stdout after being run. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param network_mode: Networking mode for the RUN commands during build. *Requires Docker Engine API v1.25+*. Specify this property to build images on a specific networking mode. Default: - no networking mode specified
        :param platform: Platform to build for. *Requires Docker Buildx*. Specify this property to build images on a specific platform/architecture. Default: - current machine platform

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            docker_image_source = cloud_assembly_schema.DockerImageSource(
                cache_from=[cloud_assembly_schema.DockerCacheOption(
                    type="type",
            
                    # the properties below are optional
                    params={
                        "params_key": "params"
                    }
                )],
                cache_to=cloud_assembly_schema.DockerCacheOption(
                    type="type",
            
                    # the properties below are optional
                    params={
                        "params_key": "params"
                    }
                ),
                directory="directory",
                docker_build_args={
                    "docker_build_args_key": "dockerBuildArgs"
                },
                docker_build_secrets={
                    "docker_build_secrets_key": "dockerBuildSecrets"
                },
                docker_build_ssh="dockerBuildSsh",
                docker_build_target="dockerBuildTarget",
                docker_file="dockerFile",
                docker_outputs=["dockerOutputs"],
                executable=["executable"],
                network_mode="networkMode",
                platform="platform"
            )
        '''
        if isinstance(cache_to, dict):
            cache_to = DockerCacheOption(**cache_to)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68b7dbb9ff110c1143ff2f04551d1b631fbf4f14a7e4b5b1fecac92324c1e63)
            check_type(argname="argument cache_from", value=cache_from, expected_type=type_hints["cache_from"])
            check_type(argname="argument cache_to", value=cache_to, expected_type=type_hints["cache_to"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument docker_build_args", value=docker_build_args, expected_type=type_hints["docker_build_args"])
            check_type(argname="argument docker_build_secrets", value=docker_build_secrets, expected_type=type_hints["docker_build_secrets"])
            check_type(argname="argument docker_build_ssh", value=docker_build_ssh, expected_type=type_hints["docker_build_ssh"])
            check_type(argname="argument docker_build_target", value=docker_build_target, expected_type=type_hints["docker_build_target"])
            check_type(argname="argument docker_file", value=docker_file, expected_type=type_hints["docker_file"])
            check_type(argname="argument docker_outputs", value=docker_outputs, expected_type=type_hints["docker_outputs"])
            check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cache_from is not None:
            self._values["cache_from"] = cache_from
        if cache_to is not None:
            self._values["cache_to"] = cache_to
        if directory is not None:
            self._values["directory"] = directory
        if docker_build_args is not None:
            self._values["docker_build_args"] = docker_build_args
        if docker_build_secrets is not None:
            self._values["docker_build_secrets"] = docker_build_secrets
        if docker_build_ssh is not None:
            self._values["docker_build_ssh"] = docker_build_ssh
        if docker_build_target is not None:
            self._values["docker_build_target"] = docker_build_target
        if docker_file is not None:
            self._values["docker_file"] = docker_file
        if docker_outputs is not None:
            self._values["docker_outputs"] = docker_outputs
        if executable is not None:
            self._values["executable"] = executable
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if platform is not None:
            self._values["platform"] = platform

    @builtins.property
    def cache_from(self) -> typing.Optional[typing.List[DockerCacheOption]]:
        '''Cache from options to pass to the ``docker build`` command.

        :default: - no cache from options are passed to the build command

        :see: https://docs.docker.com/build/cache/backends/
        '''
        result = self._values.get("cache_from")
        return typing.cast(typing.Optional[typing.List[DockerCacheOption]], result)

    @builtins.property
    def cache_to(self) -> typing.Optional[DockerCacheOption]:
        '''Cache to options to pass to the ``docker build`` command.

        :default: - no cache to options are passed to the build command

        :see: https://docs.docker.com/build/cache/backends/
        '''
        result = self._values.get("cache_to")
        return typing.cast(typing.Optional[DockerCacheOption], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''The directory containing the Docker image build instructions.

        This path is relative to the asset manifest location.

        :default: - Exactly one of ``directory`` and ``executable`` is required
        '''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_build_args(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional build arguments.

        Only allowed when ``directory`` is set.

        :default: - No additional build arguments
        '''
        result = self._values.get("docker_build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def docker_build_secrets(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional build secrets.

        Only allowed when ``directory`` is set.

        :default: - No additional build secrets
        '''
        result = self._values.get("docker_build_secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def docker_build_ssh(self) -> typing.Optional[builtins.str]:
        '''SSH agent socket or keys.

        Requires building with docker buildkit.

        :default: - No ssh flag is set
        '''
        result = self._values.get("docker_build_ssh")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_build_target(self) -> typing.Optional[builtins.str]:
        '''Target build stage in a Dockerfile with multiple build stages.

        Only allowed when ``directory`` is set.

        :default: - The last stage in the Dockerfile
        '''
        result = self._values.get("docker_build_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_file(self) -> typing.Optional[builtins.str]:
        '''The name of the file with build instructions.

        Only allowed when ``directory`` is set.

        :default: "Dockerfile"
        '''
        result = self._values.get("docker_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_outputs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Outputs.

        :default: - no outputs are passed to the build command (default outputs are used)

        :see: https://docs.docker.com/engine/reference/commandline/build/#custom-build-outputs
        '''
        result = self._values.get("docker_outputs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def executable(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A command-line executable that returns the name of a local Docker image on stdout after being run.

        :default: - Exactly one of ``directory`` and ``executable`` is required
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Networking mode for the RUN commands during build. *Requires Docker Engine API v1.25+*.

        Specify this property to build images on a specific networking mode.

        :default: - no networking mode specified
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Platform to build for. *Requires Docker Buildx*.

        Specify this property to build images on a specific platform/architecture.

        :default: - current machine platform
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.EndpointServiceAvailabilityZonesContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "region": "region",
        "service_name": "serviceName",
        "lookup_role_arn": "lookupRoleArn",
    },
)
class EndpointServiceAvailabilityZonesContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        region: builtins.str,
        service_name: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query to endpoint service context provider.

        :param account: Query account.
        :param region: Query region.
        :param service_name: Query service name.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            endpoint_service_availability_zones_context_query = cloud_assembly_schema.EndpointServiceAvailabilityZonesContextQuery(
                account="account",
                region="region",
                service_name="serviceName",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b028a59a345f6074485bae83f874fa7eca8081fea4616b491a43cfb788b0dd28)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "region": region,
            "service_name": service_name,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Query service name.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
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
    jsii_type="aws-cdk-lib.cloud_assembly_schema.FileAsset",
    jsii_struct_bases=[],
    name_mapping={"destinations": "destinations", "source": "source"},
)
class FileAsset:
    def __init__(
        self,
        *,
        destinations: typing.Mapping[builtins.str, typing.Union["FileDestination", typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union["FileSource", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''A file asset.

        :param destinations: Destinations for this file asset.
        :param source: Source description for file assets.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            file_asset = cloud_assembly_schema.FileAsset(
                destinations={
                    "destinations_key": cloud_assembly_schema.FileDestination(
                        bucket_name="bucketName",
                        object_key="objectKey",
            
                        # the properties below are optional
                        assume_role_arn="assumeRoleArn",
                        assume_role_external_id="assumeRoleExternalId",
                        region="region"
                    )
                },
                source=cloud_assembly_schema.FileSource(
                    executable=["executable"],
                    packaging=cloud_assembly_schema.FileAssetPackaging.FILE,
                    path="path"
                )
            )
        '''
        if isinstance(source, dict):
            source = FileSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a482db8874b6a4a96f9be44511cc506737e4b70dff2a99f6ee0f1566bc96c3d8)
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destinations": destinations,
            "source": source,
        }

    @builtins.property
    def destinations(self) -> typing.Mapping[builtins.str, "FileDestination"]:
        '''Destinations for this file asset.'''
        result = self._values.get("destinations")
        assert result is not None, "Required property 'destinations' is missing"
        return typing.cast(typing.Mapping[builtins.str, "FileDestination"], result)

    @builtins.property
    def source(self) -> "FileSource":
        '''Source description for file assets.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("FileSource", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileAsset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.FileAssetMetadataEntry",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_hash_parameter": "artifactHashParameter",
        "id": "id",
        "packaging": "packaging",
        "path": "path",
        "s3_bucket_parameter": "s3BucketParameter",
        "s3_key_parameter": "s3KeyParameter",
        "source_hash": "sourceHash",
    },
)
class FileAssetMetadataEntry:
    def __init__(
        self,
        *,
        artifact_hash_parameter: builtins.str,
        id: builtins.str,
        packaging: builtins.str,
        path: builtins.str,
        s3_bucket_parameter: builtins.str,
        s3_key_parameter: builtins.str,
        source_hash: builtins.str,
    ) -> None:
        '''Metadata Entry spec for files.

        :param artifact_hash_parameter: The name of the parameter where the hash of the bundled asset should be passed in.
        :param id: Logical identifier for the asset.
        :param packaging: Requested packaging style.
        :param path: Path on disk to the asset.
        :param s3_bucket_parameter: Name of parameter where S3 bucket should be passed in.
        :param s3_key_parameter: Name of parameter where S3 key should be passed in.
        :param source_hash: The hash of the asset source.

        Example::

            entry = {
                "packaging": "file",
                "s3_bucket_parameter": "bucket-parameter",
                "s3_key_paramenter": "key-parameter",
                "artifact_hash_parameter": "hash-parameter"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fbb3412647192d09586c63a100c01b6e55569ecafd8e050b7588e9edfd33f2b)
            check_type(argname="argument artifact_hash_parameter", value=artifact_hash_parameter, expected_type=type_hints["artifact_hash_parameter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument s3_bucket_parameter", value=s3_bucket_parameter, expected_type=type_hints["s3_bucket_parameter"])
            check_type(argname="argument s3_key_parameter", value=s3_key_parameter, expected_type=type_hints["s3_key_parameter"])
            check_type(argname="argument source_hash", value=source_hash, expected_type=type_hints["source_hash"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifact_hash_parameter": artifact_hash_parameter,
            "id": id,
            "packaging": packaging,
            "path": path,
            "s3_bucket_parameter": s3_bucket_parameter,
            "s3_key_parameter": s3_key_parameter,
            "source_hash": source_hash,
        }

    @builtins.property
    def artifact_hash_parameter(self) -> builtins.str:
        '''The name of the parameter where the hash of the bundled asset should be passed in.'''
        result = self._values.get("artifact_hash_parameter")
        assert result is not None, "Required property 'artifact_hash_parameter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''Logical identifier for the asset.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging(self) -> builtins.str:
        '''Requested packaging style.'''
        result = self._values.get("packaging")
        assert result is not None, "Required property 'packaging' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path on disk to the asset.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket_parameter(self) -> builtins.str:
        '''Name of parameter where S3 bucket should be passed in.'''
        result = self._values.get("s3_bucket_parameter")
        assert result is not None, "Required property 's3_bucket_parameter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_key_parameter(self) -> builtins.str:
        '''Name of parameter where S3 key should be passed in.'''
        result = self._values.get("s3_key_parameter")
        assert result is not None, "Required property 's3_key_parameter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_hash(self) -> builtins.str:
        '''The hash of the asset source.'''
        result = self._values.get("source_hash")
        assert result is not None, "Required property 'source_hash' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileAssetMetadataEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.FileAssetPackaging")
class FileAssetPackaging(enum.Enum):
    '''Packaging strategy for file assets.'''

    FILE = "FILE"
    '''Upload the given path as a file.'''
    ZIP_DIRECTORY = "ZIP_DIRECTORY"
    '''The given path is a directory, zip it and upload.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.FileDestination",
    jsii_struct_bases=[AwsDestination],
    name_mapping={
        "assume_role_arn": "assumeRoleArn",
        "assume_role_external_id": "assumeRoleExternalId",
        "region": "region",
        "bucket_name": "bucketName",
        "object_key": "objectKey",
    },
)
class FileDestination(AwsDestination):
    def __init__(
        self,
        *,
        assume_role_arn: typing.Optional[builtins.str] = None,
        assume_role_external_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        bucket_name: builtins.str,
        object_key: builtins.str,
    ) -> None:
        '''Where in S3 a file asset needs to be published.

        :param assume_role_arn: The role that needs to be assumed while publishing this asset. Default: - No role will be assumed
        :param assume_role_external_id: The ExternalId that needs to be supplied while assuming this role. Default: - No ExternalId will be supplied
        :param region: The region where this asset will need to be published. Default: - Current region
        :param bucket_name: The name of the bucket.
        :param object_key: The destination object key.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            file_destination = cloud_assembly_schema.FileDestination(
                bucket_name="bucketName",
                object_key="objectKey",
            
                # the properties below are optional
                assume_role_arn="assumeRoleArn",
                assume_role_external_id="assumeRoleExternalId",
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482362971cab2cc43f5645dc6db216e662ebd818f06c2cdcac27f66423f068f7)
            check_type(argname="argument assume_role_arn", value=assume_role_arn, expected_type=type_hints["assume_role_arn"])
            check_type(argname="argument assume_role_external_id", value=assume_role_external_id, expected_type=type_hints["assume_role_external_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "object_key": object_key,
        }
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if assume_role_external_id is not None:
            self._values["assume_role_external_id"] = assume_role_external_id
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that needs to be assumed while publishing this asset.

        :default: - No role will be assumed
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_external_id(self) -> typing.Optional[builtins.str]:
        '''The ExternalId that needs to be supplied while assuming this role.

        :default: - No ExternalId will be supplied
        '''
        result = self._values.get("assume_role_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where this asset will need to be published.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the bucket.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_key(self) -> builtins.str:
        '''The destination object key.'''
        result = self._values.get("object_key")
        assert result is not None, "Required property 'object_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.FileSource",
    jsii_struct_bases=[],
    name_mapping={
        "executable": "executable",
        "packaging": "packaging",
        "path": "path",
    },
)
class FileSource:
    def __init__(
        self,
        *,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Describe the source of a file asset.

        :param executable: External command which will produce the file asset to upload. Default: - Exactly one of ``executable`` and ``path`` is required.
        :param packaging: Packaging method. Only allowed when ``path`` is specified. Default: FILE
        :param path: The filesystem object to upload. This path is relative to the asset manifest location. Default: - Exactly one of ``executable`` and ``path`` is required.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            file_source = cloud_assembly_schema.FileSource(
                executable=["executable"],
                packaging=cloud_assembly_schema.FileAssetPackaging.FILE,
                path="path"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb32f591e1ddb63dd7deff0f14ccc9ca7747792ac0f97655b1066f5c890bf88c)
            check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if executable is not None:
            self._values["executable"] = executable
        if packaging is not None:
            self._values["packaging"] = packaging
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def executable(self) -> typing.Optional[typing.List[builtins.str]]:
        '''External command which will produce the file asset to upload.

        :default: - Exactly one of ``executable`` and ``path`` is required.
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def packaging(self) -> typing.Optional[FileAssetPackaging]:
        '''Packaging method.

        Only allowed when ``path`` is specified.

        :default: FILE
        '''
        result = self._values.get("packaging")
        return typing.cast(typing.Optional[FileAssetPackaging], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The filesystem object to upload.

        This path is relative to the asset manifest location.

        :default: - Exactly one of ``executable`` and ``path`` is required.
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.Hooks",
    jsii_struct_bases=[],
    name_mapping={
        "post_deploy": "postDeploy",
        "post_destroy": "postDestroy",
        "pre_deploy": "preDeploy",
        "pre_destroy": "preDestroy",
    },
)
class Hooks:
    def __init__(
        self,
        *,
        post_deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
        post_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
        pre_deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
        pre_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Commands to run at predefined points during the integration test workflow.

        :param post_deploy: Commands to run prior after deploying the cdk stacks in the integration test. Default: - no commands
        :param post_destroy: Commands to run after destroying the cdk stacks in the integration test. Default: - no commands
        :param pre_deploy: Commands to run prior to deploying the cdk stacks in the integration test. Default: - no commands
        :param pre_destroy: Commands to run prior to destroying the cdk stacks in the integration test. Default: - no commands

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            hooks = cloud_assembly_schema.Hooks(
                post_deploy=["postDeploy"],
                post_destroy=["postDestroy"],
                pre_deploy=["preDeploy"],
                pre_destroy=["preDestroy"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbadd14eae9eb3722ca27183992f5c2cf9e9b0bb548e5a3a0ee7ac2d146c6f59)
            check_type(argname="argument post_deploy", value=post_deploy, expected_type=type_hints["post_deploy"])
            check_type(argname="argument post_destroy", value=post_destroy, expected_type=type_hints["post_destroy"])
            check_type(argname="argument pre_deploy", value=pre_deploy, expected_type=type_hints["pre_deploy"])
            check_type(argname="argument pre_destroy", value=pre_destroy, expected_type=type_hints["pre_destroy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if post_deploy is not None:
            self._values["post_deploy"] = post_deploy
        if post_destroy is not None:
            self._values["post_destroy"] = post_destroy
        if pre_deploy is not None:
            self._values["pre_deploy"] = pre_deploy
        if pre_destroy is not None:
            self._values["pre_destroy"] = pre_destroy

    @builtins.property
    def post_deploy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Commands to run prior after deploying the cdk stacks in the integration test.

        :default: - no commands
        '''
        result = self._values.get("post_deploy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def post_destroy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Commands to run after destroying the cdk stacks in the integration test.

        :default: - no commands
        '''
        result = self._values.get("post_destroy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def pre_deploy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Commands to run prior to deploying the cdk stacks in the integration test.

        :default: - no commands
        '''
        result = self._values.get("pre_deploy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def pre_destroy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Commands to run prior to destroying the cdk stacks in the integration test.

        :default: - no commands
        '''
        result = self._values.get("pre_destroy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Hooks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.HostedZoneContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "domain_name": "domainName",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
        "private_zone": "privateZone",
        "vpc_id": "vpcId",
    },
)
class HostedZoneContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        domain_name: builtins.str,
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
        private_zone: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query to hosted zone context provider.

        :param account: Query account.
        :param domain_name: The domain name e.g. example.com to lookup.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None
        :param private_zone: True if the zone you want to find is a private hosted zone. Default: false
        :param vpc_id: The VPC ID to that the private zone must be associated with. If you provide VPC ID and privateZone is false, this will return no results and raise an error. Default: - Required if privateZone=true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            hosted_zone_context_query = cloud_assembly_schema.HostedZoneContextQuery(
                account="account",
                domain_name="domainName",
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn",
                private_zone=False,
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479c87e6b7f0a4547d04d73de1bad2d396c1e1383975038b6ca8a7ee078e9ab8)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
            check_type(argname="argument private_zone", value=private_zone, expected_type=type_hints["private_zone"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "domain_name": domain_name,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn
        if private_zone is not None:
            self._values["private_zone"] = private_zone
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name e.g. example.com to lookup.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_zone(self) -> typing.Optional[builtins.bool]:
        '''True if the zone you want to find is a private hosted zone.

        :default: false
        '''
        result = self._values.get("private_zone")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The VPC ID to that the private zone must be associated with.

        If you provide VPC ID and privateZone is false, this will return no results
        and raise an error.

        :default: - Required if privateZone=true
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.IntegManifest",
    jsii_struct_bases=[],
    name_mapping={
        "test_cases": "testCases",
        "version": "version",
        "enable_lookups": "enableLookups",
        "synth_context": "synthContext",
    },
)
class IntegManifest:
    def __init__(
        self,
        *,
        test_cases: typing.Mapping[builtins.str, typing.Union["TestCase", typing.Dict[builtins.str, typing.Any]]],
        version: builtins.str,
        enable_lookups: typing.Optional[builtins.bool] = None,
        synth_context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Definitions for the integration testing manifest.

        :param test_cases: test cases.
        :param version: Version of the manifest.
        :param enable_lookups: Enable lookups for this test. If lookups are enabled then ``stackUpdateWorkflow`` must be set to false. Lookups should only be enabled when you are explicitely testing lookups. Default: false
        :param synth_context: Additional context to use when performing a synth. Any context provided here will override any default context Default: - no additional context

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            integ_manifest = cloud_assembly_schema.IntegManifest(
                test_cases={
                    "test_cases_key": cloud_assembly_schema.TestCase(
                        stacks=["stacks"],
            
                        # the properties below are optional
                        allow_destroy=["allowDestroy"],
                        assertion_stack="assertionStack",
                        assertion_stack_name="assertionStackName",
                        cdk_command_options=cloud_assembly_schema.CdkCommands(
                            deploy=cloud_assembly_schema.DeployCommand(
                                args=cloud_assembly_schema.DeployOptions(
                                    all=False,
                                    app="app",
                                    asset_metadata=False,
                                    ca_bundle_path="caBundlePath",
                                    change_set_name="changeSetName",
                                    ci=False,
                                    color=False,
                                    context={
                                        "context_key": "context"
                                    },
                                    debug=False,
                                    ec2_creds=False,
                                    exclusively=False,
                                    execute=False,
                                    force=False,
                                    ignore_errors=False,
                                    json=False,
                                    lookups=False,
                                    notices=False,
                                    notification_arns=["notificationArns"],
                                    output="output",
                                    outputs_file="outputsFile",
                                    parameters={
                                        "parameters_key": "parameters"
                                    },
                                    path_metadata=False,
                                    profile="profile",
                                    proxy="proxy",
                                    require_approval=cloud_assembly_schema.RequireApproval.NEVER,
                                    reuse_assets=["reuseAssets"],
                                    role_arn="roleArn",
                                    rollback=False,
                                    stacks=["stacks"],
                                    staging=False,
                                    strict=False,
                                    toolkit_stack_name="toolkitStackName",
                                    trace=False,
                                    use_previous_parameters=False,
                                    verbose=False,
                                    version_reporting=False
                                ),
                                enabled=False,
                                expected_message="expectedMessage",
                                expect_error=False
                            ),
                            destroy=cloud_assembly_schema.DestroyCommand(
                                args=cloud_assembly_schema.DestroyOptions(
                                    all=False,
                                    app="app",
                                    asset_metadata=False,
                                    ca_bundle_path="caBundlePath",
                                    color=False,
                                    context={
                                        "context_key": "context"
                                    },
                                    debug=False,
                                    ec2_creds=False,
                                    exclusively=False,
                                    force=False,
                                    ignore_errors=False,
                                    json=False,
                                    lookups=False,
                                    notices=False,
                                    output="output",
                                    path_metadata=False,
                                    profile="profile",
                                    proxy="proxy",
                                    role_arn="roleArn",
                                    stacks=["stacks"],
                                    staging=False,
                                    strict=False,
                                    trace=False,
                                    verbose=False,
                                    version_reporting=False
                                ),
                                enabled=False,
                                expected_message="expectedMessage",
                                expect_error=False
                            )
                        ),
                        diff_assets=False,
                        hooks=cloud_assembly_schema.Hooks(
                            post_deploy=["postDeploy"],
                            post_destroy=["postDestroy"],
                            pre_deploy=["preDeploy"],
                            pre_destroy=["preDestroy"]
                        ),
                        regions=["regions"],
                        stack_update_workflow=False
                    )
                },
                version="version",
            
                # the properties below are optional
                enable_lookups=False,
                synth_context={
                    "synth_context_key": "synthContext"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5432524b6ab8526a1e8e021ba819e88be44f2dc6f4c9a47990f2c4936b028cf5)
            check_type(argname="argument test_cases", value=test_cases, expected_type=type_hints["test_cases"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument enable_lookups", value=enable_lookups, expected_type=type_hints["enable_lookups"])
            check_type(argname="argument synth_context", value=synth_context, expected_type=type_hints["synth_context"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "test_cases": test_cases,
            "version": version,
        }
        if enable_lookups is not None:
            self._values["enable_lookups"] = enable_lookups
        if synth_context is not None:
            self._values["synth_context"] = synth_context

    @builtins.property
    def test_cases(self) -> typing.Mapping[builtins.str, "TestCase"]:
        '''test cases.'''
        result = self._values.get("test_cases")
        assert result is not None, "Required property 'test_cases' is missing"
        return typing.cast(typing.Mapping[builtins.str, "TestCase"], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Version of the manifest.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_lookups(self) -> typing.Optional[builtins.bool]:
        '''Enable lookups for this test.

        If lookups are enabled
        then ``stackUpdateWorkflow`` must be set to false.
        Lookups should only be enabled when you are explicitely testing
        lookups.

        :default: false
        '''
        result = self._values.get("enable_lookups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def synth_context(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional context to use when performing a synth.

        Any context provided here will override
        any default context

        :default: - no additional context
        '''
        result = self._values.get("synth_context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.KeyContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "alias_name": "aliasName",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
    },
)
class KeyContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        alias_name: builtins.str,
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query input for looking up a KMS Key.

        :param account: Query account.
        :param alias_name: Alias name used to search the Key.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            key_context_query = cloud_assembly_schema.KeyContextQuery(
                account="account",
                alias_name="aliasName",
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b738d31e8937d0dc914b364457cedd3794a0911b61fec9b17eb3f8ad72e53832)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "alias_name": alias_name,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''Alias name used to search the Key.'''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.LoadBalancerFilter",
    jsii_struct_bases=[],
    name_mapping={
        "load_balancer_type": "loadBalancerType",
        "load_balancer_arn": "loadBalancerArn",
        "load_balancer_tags": "loadBalancerTags",
    },
)
class LoadBalancerFilter:
    def __init__(
        self,
        *,
        load_balancer_type: "LoadBalancerType",
        load_balancer_arn: typing.Optional[builtins.str] = None,
        load_balancer_tags: typing.Optional[typing.Sequence[typing.Union["Tag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Filters for selecting load balancers.

        :param load_balancer_type: Filter load balancers by their type.
        :param load_balancer_arn: Find by load balancer's ARN. Default: - does not search by load balancer arn
        :param load_balancer_tags: Match load balancer tags. Default: - does not match load balancers by tags

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            load_balancer_filter = cloud_assembly_schema.LoadBalancerFilter(
                load_balancer_type=cloud_assembly_schema.LoadBalancerType.NETWORK,
            
                # the properties below are optional
                load_balancer_arn="loadBalancerArn",
                load_balancer_tags=[cloud_assembly_schema.Tag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b57ff0c819ed8af3b684900df083604408f77b99e70f2dd2d12b1cc7e4a8e68c)
            check_type(argname="argument load_balancer_type", value=load_balancer_type, expected_type=type_hints["load_balancer_type"])
            check_type(argname="argument load_balancer_arn", value=load_balancer_arn, expected_type=type_hints["load_balancer_arn"])
            check_type(argname="argument load_balancer_tags", value=load_balancer_tags, expected_type=type_hints["load_balancer_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer_type": load_balancer_type,
        }
        if load_balancer_arn is not None:
            self._values["load_balancer_arn"] = load_balancer_arn
        if load_balancer_tags is not None:
            self._values["load_balancer_tags"] = load_balancer_tags

    @builtins.property
    def load_balancer_type(self) -> "LoadBalancerType":
        '''Filter load balancers by their type.'''
        result = self._values.get("load_balancer_type")
        assert result is not None, "Required property 'load_balancer_type' is missing"
        return typing.cast("LoadBalancerType", result)

    @builtins.property
    def load_balancer_arn(self) -> typing.Optional[builtins.str]:
        '''Find by load balancer's ARN.

        :default: - does not search by load balancer arn
        '''
        result = self._values.get("load_balancer_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Match load balancer tags.

        :default: - does not match load balancers by tags
        '''
        result = self._values.get("load_balancer_tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.LoadBalancerListenerContextQuery",
    jsii_struct_bases=[LoadBalancerFilter],
    name_mapping={
        "load_balancer_type": "loadBalancerType",
        "load_balancer_arn": "loadBalancerArn",
        "load_balancer_tags": "loadBalancerTags",
        "account": "account",
        "region": "region",
        "listener_arn": "listenerArn",
        "listener_port": "listenerPort",
        "listener_protocol": "listenerProtocol",
        "lookup_role_arn": "lookupRoleArn",
    },
)
class LoadBalancerListenerContextQuery(LoadBalancerFilter):
    def __init__(
        self,
        *,
        load_balancer_type: "LoadBalancerType",
        load_balancer_arn: typing.Optional[builtins.str] = None,
        load_balancer_tags: typing.Optional[typing.Sequence[typing.Union["Tag", typing.Dict[builtins.str, typing.Any]]]] = None,
        account: builtins.str,
        region: builtins.str,
        listener_arn: typing.Optional[builtins.str] = None,
        listener_port: typing.Optional[jsii.Number] = None,
        listener_protocol: typing.Optional["LoadBalancerListenerProtocol"] = None,
        lookup_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query input for looking up a load balancer listener.

        :param load_balancer_type: Filter load balancers by their type.
        :param load_balancer_arn: Find by load balancer's ARN. Default: - does not search by load balancer arn
        :param load_balancer_tags: Match load balancer tags. Default: - does not match load balancers by tags
        :param account: Query account.
        :param region: Query region.
        :param listener_arn: Find by listener's arn. Default: - does not find by listener arn
        :param listener_port: Filter listeners by listener port. Default: - does not filter by a listener port
        :param listener_protocol: Filter by listener protocol. Default: - does not filter by listener protocol
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            load_balancer_listener_context_query = cloud_assembly_schema.LoadBalancerListenerContextQuery(
                account="account",
                load_balancer_type=cloud_assembly_schema.LoadBalancerType.NETWORK,
                region="region",
            
                # the properties below are optional
                listener_arn="listenerArn",
                listener_port=123,
                listener_protocol=cloud_assembly_schema.LoadBalancerListenerProtocol.HTTP,
                load_balancer_arn="loadBalancerArn",
                load_balancer_tags=[cloud_assembly_schema.Tag(
                    key="key",
                    value="value"
                )],
                lookup_role_arn="lookupRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e0c4bf3a41978c03455699a53b8dc150feef48b4e8d1cb490e0e3cffa75ced7)
            check_type(argname="argument load_balancer_type", value=load_balancer_type, expected_type=type_hints["load_balancer_type"])
            check_type(argname="argument load_balancer_arn", value=load_balancer_arn, expected_type=type_hints["load_balancer_arn"])
            check_type(argname="argument load_balancer_tags", value=load_balancer_tags, expected_type=type_hints["load_balancer_tags"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
            check_type(argname="argument listener_port", value=listener_port, expected_type=type_hints["listener_port"])
            check_type(argname="argument listener_protocol", value=listener_protocol, expected_type=type_hints["listener_protocol"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer_type": load_balancer_type,
            "account": account,
            "region": region,
        }
        if load_balancer_arn is not None:
            self._values["load_balancer_arn"] = load_balancer_arn
        if load_balancer_tags is not None:
            self._values["load_balancer_tags"] = load_balancer_tags
        if listener_arn is not None:
            self._values["listener_arn"] = listener_arn
        if listener_port is not None:
            self._values["listener_port"] = listener_port
        if listener_protocol is not None:
            self._values["listener_protocol"] = listener_protocol
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn

    @builtins.property
    def load_balancer_type(self) -> "LoadBalancerType":
        '''Filter load balancers by their type.'''
        result = self._values.get("load_balancer_type")
        assert result is not None, "Required property 'load_balancer_type' is missing"
        return typing.cast("LoadBalancerType", result)

    @builtins.property
    def load_balancer_arn(self) -> typing.Optional[builtins.str]:
        '''Find by load balancer's ARN.

        :default: - does not search by load balancer arn
        '''
        result = self._values.get("load_balancer_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''Match load balancer tags.

        :default: - does not match load balancers by tags
        '''
        result = self._values.get("load_balancer_tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_arn(self) -> typing.Optional[builtins.str]:
        '''Find by listener's arn.

        :default: - does not find by listener arn
        '''
        result = self._values.get("listener_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def listener_port(self) -> typing.Optional[jsii.Number]:
        '''Filter listeners by listener port.

        :default: - does not filter by a listener port
        '''
        result = self._values.get("listener_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def listener_protocol(self) -> typing.Optional["LoadBalancerListenerProtocol"]:
        '''Filter by listener protocol.

        :default: - does not filter by listener protocol
        '''
        result = self._values.get("listener_protocol")
        return typing.cast(typing.Optional["LoadBalancerListenerProtocol"], result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerListenerContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.LoadBalancerListenerProtocol")
class LoadBalancerListenerProtocol(enum.Enum):
    '''The protocol for connections from clients to the load balancer.'''

    HTTP = "HTTP"
    '''HTTP protocol.'''
    HTTPS = "HTTPS"
    '''HTTPS protocol.'''
    TCP = "TCP"
    '''TCP protocol.'''
    TLS = "TLS"
    '''TLS protocol.'''
    UDP = "UDP"
    '''UDP protocol.'''
    TCP_UDP = "TCP_UDP"
    '''TCP and UDP protocol.'''


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.LoadBalancerType")
class LoadBalancerType(enum.Enum):
    '''Type of load balancer.'''

    NETWORK = "NETWORK"
    '''Network load balancer.'''
    APPLICATION = "APPLICATION"
    '''Application load balancer.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.LoadManifestOptions",
    jsii_struct_bases=[],
    name_mapping={
        "skip_enum_check": "skipEnumCheck",
        "skip_version_check": "skipVersionCheck",
        "topo_sort": "topoSort",
    },
)
class LoadManifestOptions:
    def __init__(
        self,
        *,
        skip_enum_check: typing.Optional[builtins.bool] = None,
        skip_version_check: typing.Optional[builtins.bool] = None,
        topo_sort: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for the loadManifest operation.

        :param skip_enum_check: Skip enum checks. This means you may read enum values you don't know about yet. Make sure to always check the values of enums you encounter in the manifest. Default: false
        :param skip_version_check: Skip the version check. This means you may read a newer cloud assembly than the CX API is designed to support, and your application may not be aware of all features that in use in the Cloud Assembly. Default: false
        :param topo_sort: Topologically sort all artifacts. This parameter is only respected by the constructor of ``CloudAssembly``. The property lives here for backwards compatibility reasons. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            load_manifest_options = cloud_assembly_schema.LoadManifestOptions(
                skip_enum_check=False,
                skip_version_check=False,
                topo_sort=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d4beea8990d112d9f873ed9d80c8fbeb641413dbd84d56c37eb8d74fd77448)
            check_type(argname="argument skip_enum_check", value=skip_enum_check, expected_type=type_hints["skip_enum_check"])
            check_type(argname="argument skip_version_check", value=skip_version_check, expected_type=type_hints["skip_version_check"])
            check_type(argname="argument topo_sort", value=topo_sort, expected_type=type_hints["topo_sort"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if skip_enum_check is not None:
            self._values["skip_enum_check"] = skip_enum_check
        if skip_version_check is not None:
            self._values["skip_version_check"] = skip_version_check
        if topo_sort is not None:
            self._values["topo_sort"] = topo_sort

    @builtins.property
    def skip_enum_check(self) -> typing.Optional[builtins.bool]:
        '''Skip enum checks.

        This means you may read enum values you don't know about yet. Make sure to always
        check the values of enums you encounter in the manifest.

        :default: false
        '''
        result = self._values.get("skip_enum_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def skip_version_check(self) -> typing.Optional[builtins.bool]:
        '''Skip the version check.

        This means you may read a newer cloud assembly than the CX API is designed
        to support, and your application may not be aware of all features that in use
        in the Cloud Assembly.

        :default: false
        '''
        result = self._values.get("skip_version_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def topo_sort(self) -> typing.Optional[builtins.bool]:
        '''Topologically sort all artifacts.

        This parameter is only respected by the constructor of ``CloudAssembly``. The
        property lives here for backwards compatibility reasons.

        :default: true
        '''
        result = self._values.get("topo_sort")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadManifestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Manifest(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.cloud_assembly_schema.Manifest",
):
    '''Protocol utility class.'''

    @jsii.member(jsii_name="loadAssemblyManifest")
    @builtins.classmethod
    def load_assembly_manifest(
        cls,
        file_path: builtins.str,
        *,
        skip_enum_check: typing.Optional[builtins.bool] = None,
        skip_version_check: typing.Optional[builtins.bool] = None,
        topo_sort: typing.Optional[builtins.bool] = None,
    ) -> AssemblyManifest:
        '''Load and validates the cloud assembly manifest from file.

        :param file_path: - path to the manifest file.
        :param skip_enum_check: Skip enum checks. This means you may read enum values you don't know about yet. Make sure to always check the values of enums you encounter in the manifest. Default: false
        :param skip_version_check: Skip the version check. This means you may read a newer cloud assembly than the CX API is designed to support, and your application may not be aware of all features that in use in the Cloud Assembly. Default: false
        :param topo_sort: Topologically sort all artifacts. This parameter is only respected by the constructor of ``CloudAssembly``. The property lives here for backwards compatibility reasons. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb4be78db16e194bc36707aee4bf2c1284ffddcd2ddfffe63450850c373f9bd)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = LoadManifestOptions(
            skip_enum_check=skip_enum_check,
            skip_version_check=skip_version_check,
            topo_sort=topo_sort,
        )

        return typing.cast(AssemblyManifest, jsii.sinvoke(cls, "loadAssemblyManifest", [file_path, options]))

    @jsii.member(jsii_name="loadAssetManifest")
    @builtins.classmethod
    def load_asset_manifest(cls, file_path: builtins.str) -> AssetManifest:
        '''Load and validates the asset manifest from file.

        :param file_path: - path to the manifest file.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__252134c733b52c64fcb4e76c02ca1c3c29cbd4206194764bb4ccd634bf2b350a)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast(AssetManifest, jsii.sinvoke(cls, "loadAssetManifest", [file_path]))

    @jsii.member(jsii_name="loadIntegManifest")
    @builtins.classmethod
    def load_integ_manifest(cls, file_path: builtins.str) -> IntegManifest:
        '''Load and validates the integ manifest from file.

        :param file_path: - path to the manifest file.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__633f66b76e82fdca841018e97eb59fc4ea9aa150a20d1e0b3a69fbf5085bd783)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast(IntegManifest, jsii.sinvoke(cls, "loadIntegManifest", [file_path]))

    @jsii.member(jsii_name="saveAssemblyManifest")
    @builtins.classmethod
    def save_assembly_manifest(
        cls,
        manifest: typing.Union[AssemblyManifest, typing.Dict[builtins.str, typing.Any]],
        file_path: builtins.str,
    ) -> None:
        '''Validates and saves the cloud assembly manifest to file.

        :param manifest: - manifest.
        :param file_path: - output file path.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1461b7e78a2d33c07931bce60df24a9c3db0ca9beb19b2f02d9d86e262073ffa)
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast(None, jsii.sinvoke(cls, "saveAssemblyManifest", [manifest, file_path]))

    @jsii.member(jsii_name="saveAssetManifest")
    @builtins.classmethod
    def save_asset_manifest(
        cls,
        manifest: typing.Union[AssetManifest, typing.Dict[builtins.str, typing.Any]],
        file_path: builtins.str,
    ) -> None:
        '''Validates and saves the asset manifest to file.

        :param manifest: - manifest.
        :param file_path: - output file path.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45cd3c37aac070d85d5695adc2f1e4ecf988ca34c895e29c1ececb7de61a5f67)
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast(None, jsii.sinvoke(cls, "saveAssetManifest", [manifest, file_path]))

    @jsii.member(jsii_name="saveIntegManifest")
    @builtins.classmethod
    def save_integ_manifest(
        cls,
        manifest: typing.Union[IntegManifest, typing.Dict[builtins.str, typing.Any]],
        file_path: builtins.str,
    ) -> None:
        '''Validates and saves the integ manifest to file.

        :param manifest: - manifest.
        :param file_path: - output file path.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87be211e9c3bb7ce042946888a960f69db963f2d5811832fbf0681bf94a6f450)
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast(None, jsii.sinvoke(cls, "saveIntegManifest", [manifest, file_path]))

    @jsii.member(jsii_name="version")
    @builtins.classmethod
    def version(cls) -> builtins.str:
        '''Fetch the current schema version number.'''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "version", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.MetadataEntry",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "data": "data", "trace": "trace"},
)
class MetadataEntry:
    def __init__(
        self,
        *,
        type: builtins.str,
        data: typing.Optional[typing.Union[builtins.str, typing.Union[FileAssetMetadataEntry, typing.Dict[builtins.str, typing.Any]], typing.Union[ContainerImageAssetMetadataEntry, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union["Tag", typing.Dict[builtins.str, typing.Any]]]]] = None,
        trace: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A metadata entry in a cloud assembly artifact.

        :param type: The type of the metadata entry.
        :param data: The data. Default: - no data.
        :param trace: A stack trace for when the entry was created. Default: - no trace.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            metadata_entry = cloud_assembly_schema.MetadataEntry(
                type="type",
            
                # the properties below are optional
                data="data",
                trace=["trace"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e77201bee0581d95dfd6e3150d491c958851c456cbdd8aaea71cb737197beaee)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
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
    ) -> typing.Optional[typing.Union[builtins.str, FileAssetMetadataEntry, ContainerImageAssetMetadataEntry, typing.List["Tag"]]]:
        '''The data.

        :default: - no data.
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[typing.Union[builtins.str, FileAssetMetadataEntry, ContainerImageAssetMetadataEntry, typing.List["Tag"]]], result)

    @builtins.property
    def trace(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A stack trace for when the entry was created.

        :default: - no trace.
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetadataEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.MissingContext",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "props": "props", "provider": "provider"},
)
class MissingContext:
    def __init__(
        self,
        *,
        key: builtins.str,
        props: typing.Union[typing.Union[AmiContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[AvailabilityZonesContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[HostedZoneContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union["SSMParameterContextQuery", typing.Dict[builtins.str, typing.Any]], typing.Union["VpcContextQuery", typing.Dict[builtins.str, typing.Any]], typing.Union[EndpointServiceAvailabilityZonesContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union["LoadBalancerContextQuery", typing.Dict[builtins.str, typing.Any]], typing.Union[LoadBalancerListenerContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union["SecurityGroupContextQuery", typing.Dict[builtins.str, typing.Any]], typing.Union[KeyContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union["PluginContextQuery", typing.Dict[builtins.str, typing.Any]]],
        provider: ContextProvider,
    ) -> None:
        '''Represents a missing piece of context.

        :param key: The missing context key.
        :param props: A set of provider-specific options.
        :param provider: The provider from which we expect this context key to be obtained.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            missing_context = cloud_assembly_schema.MissingContext(
                key="key",
                props=cloud_assembly_schema.AmiContextQuery(
                    account="account",
                    filters={
                        "filters_key": ["filters"]
                    },
                    region="region",
            
                    # the properties below are optional
                    lookup_role_arn="lookupRoleArn",
                    owners=["owners"]
                ),
                provider=cloud_assembly_schema.ContextProvider.AMI_PROVIDER
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af657f9f6c83e032e4811f8db352c854d88bb8d40b052424137f1bf159f9170d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "props": props,
            "provider": provider,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''The missing context key.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def props(
        self,
    ) -> typing.Union[AmiContextQuery, AvailabilityZonesContextQuery, HostedZoneContextQuery, "SSMParameterContextQuery", "VpcContextQuery", EndpointServiceAvailabilityZonesContextQuery, "LoadBalancerContextQuery", LoadBalancerListenerContextQuery, "SecurityGroupContextQuery", KeyContextQuery, "PluginContextQuery"]:
        '''A set of provider-specific options.'''
        result = self._values.get("props")
        assert result is not None, "Required property 'props' is missing"
        return typing.cast(typing.Union[AmiContextQuery, AvailabilityZonesContextQuery, HostedZoneContextQuery, "SSMParameterContextQuery", "VpcContextQuery", EndpointServiceAvailabilityZonesContextQuery, "LoadBalancerContextQuery", LoadBalancerListenerContextQuery, "SecurityGroupContextQuery", KeyContextQuery, "PluginContextQuery"], result)

    @builtins.property
    def provider(self) -> ContextProvider:
        '''The provider from which we expect this context key to be obtained.'''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast(ContextProvider, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MissingContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.NestedCloudAssemblyProperties",
    jsii_struct_bases=[],
    name_mapping={"directory_name": "directoryName", "display_name": "displayName"},
)
class NestedCloudAssemblyProperties:
    def __init__(
        self,
        *,
        directory_name: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Artifact properties for nested cloud assemblies.

        :param directory_name: Relative path to the nested cloud assembly.
        :param display_name: Display name for the cloud assembly. Default: - The artifact ID

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            nested_cloud_assembly_properties = cloud_assembly_schema.NestedCloudAssemblyProperties(
                directory_name="directoryName",
            
                # the properties below are optional
                display_name="displayName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06bd54f69162b763b33d231a80754950d41ec566c6c02535d422732a76ced29e)
            check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_name": directory_name,
        }
        if display_name is not None:
            self._values["display_name"] = display_name

    @builtins.property
    def directory_name(self) -> builtins.str:
        '''Relative path to the nested cloud assembly.'''
        result = self._values.get("directory_name")
        assert result is not None, "Required property 'directory_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Display name for the cloud assembly.

        :default: - The artifact ID
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NestedCloudAssemblyProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.PluginContextQuery",
    jsii_struct_bases=[],
    name_mapping={"plugin_name": "pluginName"},
)
class PluginContextQuery:
    def __init__(self, *, plugin_name: builtins.str) -> None:
        '''Query input for plugins.

        This alternate branch is necessary because it needs to be able to escape all type checking
        we do on on the cloud assembly -- we cannot know the properties that will be used a priori.

        :param plugin_name: The name of the plugin.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            plugin_context_query = cloud_assembly_schema.PluginContextQuery(
                plugin_name="pluginName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e904ca937e50d9783874bf1fb0d167b1784afebb80b64c89916b1427dbbc97ed)
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "plugin_name": plugin_name,
        }

    @builtins.property
    def plugin_name(self) -> builtins.str:
        '''The name of the plugin.'''
        result = self._values.get("plugin_name")
        assert result is not None, "Required property 'plugin_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PluginContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.cloud_assembly_schema.RequireApproval")
class RequireApproval(enum.Enum):
    '''In what scenarios should the CLI ask for approval.

    :exampleMetadata: infused

    Example::

        app = App()
        
        stack_under_test = Stack(app, "StackUnderTest")
        
        stack = Stack(app, "stack")
        
        test_case = IntegTest(app, "CustomizedDeploymentWorkflow",
            test_cases=[stack_under_test],
            diff_assets=True,
            stack_update_workflow=True,
            cdk_command_options=CdkCommands(
                deploy=DeployCommand(
                    args=DeployOptions(
                        require_approval=RequireApproval.NEVER,
                        json=True
                    )
                ),
                destroy=DestroyCommand(
                    args=DestroyOptions(
                        force=True
                    )
                )
            )
        )
    '''

    NEVER = "NEVER"
    '''Never ask for approval.'''
    ANYCHANGE = "ANYCHANGE"
    '''Prompt for approval for any type  of change to the stack.'''
    BROADENING = "BROADENING"
    '''Only prompt for approval if there are security related changes.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.RuntimeInfo",
    jsii_struct_bases=[],
    name_mapping={"libraries": "libraries"},
)
class RuntimeInfo:
    def __init__(
        self,
        *,
        libraries: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''Information about the application's runtime components.

        :param libraries: The list of libraries loaded in the application, associated with their versions.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            runtime_info = cloud_assembly_schema.RuntimeInfo(
                libraries={
                    "libraries_key": "libraries"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d8ff22f74ddaf52e071d67dbc65d3080f622da186b8d675c5b21733200b4c4)
            check_type(argname="argument libraries", value=libraries, expected_type=type_hints["libraries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "libraries": libraries,
        }

    @builtins.property
    def libraries(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The list of libraries loaded in the application, associated with their versions.'''
        result = self._values.get("libraries")
        assert result is not None, "Required property 'libraries' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuntimeInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.SSMParameterContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "parameter_name": "parameterName",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
    },
)
class SSMParameterContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        parameter_name: builtins.str,
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query to SSM Parameter Context Provider.

        :param account: Query account.
        :param parameter_name: Parameter name to query.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            s_sMParameter_context_query = cloud_assembly_schema.SSMParameterContextQuery(
                account="account",
                parameter_name="parameterName",
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__684d2dfddbf9de1c9120fbcee643319c13ff10fa5e3227b4959d94fdac1463d5)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "parameter_name": parameter_name,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Parameter name to query.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SSMParameterContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.SecurityGroupContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
        "security_group_id": "securityGroupId",
        "security_group_name": "securityGroupName",
        "vpc_id": "vpcId",
    },
)
class SecurityGroupContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
        security_group_id: typing.Optional[builtins.str] = None,
        security_group_name: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query input for looking up a security group.

        :param account: Query account.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None
        :param security_group_id: Security group id. Default: - None
        :param security_group_name: Security group name. Default: - None
        :param vpc_id: VPC ID. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            security_group_context_query = cloud_assembly_schema.SecurityGroupContextQuery(
                account="account",
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn",
                security_group_id="securityGroupId",
                security_group_name="securityGroupName",
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab27bdfc9deaaa99cc0b29d10214dea6da9d91e77b9d18d5a5f9a2b7f4578cb4)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
            check_type(argname="argument security_group_name", value=security_group_name, expected_type=type_hints["security_group_name"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn
        if security_group_id is not None:
            self._values["security_group_id"] = security_group_id
        if security_group_name is not None:
            self._values["security_group_name"] = security_group_name
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_id(self) -> typing.Optional[builtins.str]:
        '''Security group id.

        :default: - None
        '''
        result = self._values.get("security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_name(self) -> typing.Optional[builtins.str]:
        '''Security group name.

        :default: - None
        '''
        result = self._values.get("security_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''VPC ID.

        :default: - None
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.Tag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Tag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''Metadata Entry spec for stack tag.

        :param key: Tag key. (In the actual file on disk this will be cased as "Key", and the structure is patched to match this structure upon loading: https://github.com/aws/aws-cdk/blob/4aadaa779b48f35838cccd4e25107b2338f05547/packages/%40aws-cdk/cloud-assembly-schema/lib/manifest.ts#L137)
        :param value: Tag value. (In the actual file on disk this will be cased as "Value", and the structure is patched to match this structure upon loading: https://github.com/aws/aws-cdk/blob/4aadaa779b48f35838cccd4e25107b2338f05547/packages/%40aws-cdk/cloud-assembly-schema/lib/manifest.ts#L137)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            tag = cloud_assembly_schema.Tag(
                key="key",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dff2df53008ccb9c0c772f8e5e1040e54c1f5a0e71c6267f41bf1819e91d077)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Tag key.

        (In the actual file on disk this will be cased as "Key", and the structure is
        patched to match this structure upon loading:
        https://github.com/aws/aws-cdk/blob/4aadaa779b48f35838cccd4e25107b2338f05547/packages/%40aws-cdk/cloud-assembly-schema/lib/manifest.ts#L137)
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Tag value.

        (In the actual file on disk this will be cased as "Value", and the structure is
        patched to match this structure upon loading:
        https://github.com/aws/aws-cdk/blob/4aadaa779b48f35838cccd4e25107b2338f05547/packages/%40aws-cdk/cloud-assembly-schema/lib/manifest.ts#L137)
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.TestOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allow_destroy": "allowDestroy",
        "cdk_command_options": "cdkCommandOptions",
        "diff_assets": "diffAssets",
        "hooks": "hooks",
        "regions": "regions",
        "stack_update_workflow": "stackUpdateWorkflow",
    },
)
class TestOptions:
    def __init__(
        self,
        *,
        allow_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
        cdk_command_options: typing.Optional[typing.Union[CdkCommands, typing.Dict[builtins.str, typing.Any]]] = None,
        diff_assets: typing.Optional[builtins.bool] = None,
        hooks: typing.Optional[typing.Union[Hooks, typing.Dict[builtins.str, typing.Any]]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        stack_update_workflow: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The set of options to control the workflow of the test runner.

        :param allow_destroy: List of CloudFormation resource types in this stack that can be destroyed as part of an update without failing the test. This list should only include resources that for this specific integration test we are sure will not cause errors or an outage if destroyed. For example, maybe we know that a new resource will be created first before the old resource is destroyed which prevents any outage. e.g. ['AWS::IAM::Role'] Default: - do not allow destruction of any resources on update
        :param cdk_command_options: Additional options to use for each CDK command. Default: - runner default options
        :param diff_assets: Whether or not to include asset hashes in the diff Asset hashes can introduces a lot of unneccessary noise into tests, but there are some cases where asset hashes *should* be included. For example any tests involving custom resources or bundling Default: false
        :param hooks: Additional commands to run at predefined points in the test workflow. e.g. { postDeploy: ['yarn', 'test'] } Default: - no hooks
        :param regions: Limit deployment to these regions. Default: - can run in any region
        :param stack_update_workflow: Run update workflow on this test case This should only be set to false to test scenarios that are not possible to test as part of the update workflow. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            test_options = cloud_assembly_schema.TestOptions(
                allow_destroy=["allowDestroy"],
                cdk_command_options=cloud_assembly_schema.CdkCommands(
                    deploy=cloud_assembly_schema.DeployCommand(
                        args=cloud_assembly_schema.DeployOptions(
                            all=False,
                            app="app",
                            asset_metadata=False,
                            ca_bundle_path="caBundlePath",
                            change_set_name="changeSetName",
                            ci=False,
                            color=False,
                            context={
                                "context_key": "context"
                            },
                            debug=False,
                            ec2_creds=False,
                            exclusively=False,
                            execute=False,
                            force=False,
                            ignore_errors=False,
                            json=False,
                            lookups=False,
                            notices=False,
                            notification_arns=["notificationArns"],
                            output="output",
                            outputs_file="outputsFile",
                            parameters={
                                "parameters_key": "parameters"
                            },
                            path_metadata=False,
                            profile="profile",
                            proxy="proxy",
                            require_approval=cloud_assembly_schema.RequireApproval.NEVER,
                            reuse_assets=["reuseAssets"],
                            role_arn="roleArn",
                            rollback=False,
                            stacks=["stacks"],
                            staging=False,
                            strict=False,
                            toolkit_stack_name="toolkitStackName",
                            trace=False,
                            use_previous_parameters=False,
                            verbose=False,
                            version_reporting=False
                        ),
                        enabled=False,
                        expected_message="expectedMessage",
                        expect_error=False
                    ),
                    destroy=cloud_assembly_schema.DestroyCommand(
                        args=cloud_assembly_schema.DestroyOptions(
                            all=False,
                            app="app",
                            asset_metadata=False,
                            ca_bundle_path="caBundlePath",
                            color=False,
                            context={
                                "context_key": "context"
                            },
                            debug=False,
                            ec2_creds=False,
                            exclusively=False,
                            force=False,
                            ignore_errors=False,
                            json=False,
                            lookups=False,
                            notices=False,
                            output="output",
                            path_metadata=False,
                            profile="profile",
                            proxy="proxy",
                            role_arn="roleArn",
                            stacks=["stacks"],
                            staging=False,
                            strict=False,
                            trace=False,
                            verbose=False,
                            version_reporting=False
                        ),
                        enabled=False,
                        expected_message="expectedMessage",
                        expect_error=False
                    )
                ),
                diff_assets=False,
                hooks=cloud_assembly_schema.Hooks(
                    post_deploy=["postDeploy"],
                    post_destroy=["postDestroy"],
                    pre_deploy=["preDeploy"],
                    pre_destroy=["preDestroy"]
                ),
                regions=["regions"],
                stack_update_workflow=False
            )
        '''
        if isinstance(cdk_command_options, dict):
            cdk_command_options = CdkCommands(**cdk_command_options)
        if isinstance(hooks, dict):
            hooks = Hooks(**hooks)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87885fac73fc14075c22fe051717d21aa5da7c4113e34310cff21b849bc534d7)
            check_type(argname="argument allow_destroy", value=allow_destroy, expected_type=type_hints["allow_destroy"])
            check_type(argname="argument cdk_command_options", value=cdk_command_options, expected_type=type_hints["cdk_command_options"])
            check_type(argname="argument diff_assets", value=diff_assets, expected_type=type_hints["diff_assets"])
            check_type(argname="argument hooks", value=hooks, expected_type=type_hints["hooks"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument stack_update_workflow", value=stack_update_workflow, expected_type=type_hints["stack_update_workflow"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_destroy is not None:
            self._values["allow_destroy"] = allow_destroy
        if cdk_command_options is not None:
            self._values["cdk_command_options"] = cdk_command_options
        if diff_assets is not None:
            self._values["diff_assets"] = diff_assets
        if hooks is not None:
            self._values["hooks"] = hooks
        if regions is not None:
            self._values["regions"] = regions
        if stack_update_workflow is not None:
            self._values["stack_update_workflow"] = stack_update_workflow

    @builtins.property
    def allow_destroy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of CloudFormation resource types in this stack that can be destroyed as part of an update without failing the test.

        This list should only include resources that for this specific
        integration test we are sure will not cause errors or an outage if
        destroyed. For example, maybe we know that a new resource will be created
        first before the old resource is destroyed which prevents any outage.

        e.g. ['AWS::IAM::Role']

        :default: - do not allow destruction of any resources on update
        '''
        result = self._values.get("allow_destroy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cdk_command_options(self) -> typing.Optional[CdkCommands]:
        '''Additional options to use for each CDK command.

        :default: - runner default options
        '''
        result = self._values.get("cdk_command_options")
        return typing.cast(typing.Optional[CdkCommands], result)

    @builtins.property
    def diff_assets(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to include asset hashes in the diff Asset hashes can introduces a lot of unneccessary noise into tests, but there are some cases where asset hashes *should* be included.

        For example
        any tests involving custom resources or bundling

        :default: false
        '''
        result = self._values.get("diff_assets")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def hooks(self) -> typing.Optional[Hooks]:
        '''Additional commands to run at predefined points in the test workflow.

        e.g. { postDeploy: ['yarn', 'test'] }

        :default: - no hooks
        '''
        result = self._values.get("hooks")
        return typing.cast(typing.Optional[Hooks], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Limit deployment to these regions.

        :default: - can run in any region
        '''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def stack_update_workflow(self) -> typing.Optional[builtins.bool]:
        '''Run update workflow on this test case This should only be set to false to test scenarios that are not possible to test as part of the update workflow.

        :default: true
        '''
        result = self._values.get("stack_update_workflow")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.TreeArtifactProperties",
    jsii_struct_bases=[],
    name_mapping={"file": "file"},
)
class TreeArtifactProperties:
    def __init__(self, *, file: builtins.str) -> None:
        '''Artifact properties for the Construct Tree Artifact.

        :param file: Filename of the tree artifact.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            tree_artifact_properties = cloud_assembly_schema.TreeArtifactProperties(
                file="file"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f49fc9c74b07ac016f6f246ae2bfaa0eea6382d75f9ee62c77e3b2446eec513)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file": file,
        }

    @builtins.property
    def file(self) -> builtins.str:
        '''Filename of the tree artifact.'''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TreeArtifactProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.VpcContextQuery",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "filter": "filter",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
        "return_asymmetric_subnets": "returnAsymmetricSubnets",
        "return_vpn_gateways": "returnVpnGateways",
        "subnet_group_name_tag": "subnetGroupNameTag",
    },
)
class VpcContextQuery:
    def __init__(
        self,
        *,
        account: builtins.str,
        filter: typing.Mapping[builtins.str, builtins.str],
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
        return_asymmetric_subnets: typing.Optional[builtins.bool] = None,
        return_vpn_gateways: typing.Optional[builtins.bool] = None,
        subnet_group_name_tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query input for looking up a VPC.

        :param account: Query account.
        :param filter: Filters to apply to the VPC. Filter parameters are the same as passed to DescribeVpcs.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None
        :param return_asymmetric_subnets: Whether to populate the subnetGroups field of the ``VpcContextResponse``, which contains potentially asymmetric subnet groups. Default: false
        :param return_vpn_gateways: Whether to populate the ``vpnGatewayId`` field of the ``VpcContextResponse``, which contains the VPN Gateway ID, if one exists. You can explicitly disable this in order to avoid the lookup if you know the VPC does not have a VPN Gatway attached. Default: true
        :param subnet_group_name_tag: Optional tag for subnet group name. If not provided, we'll look at the aws-cdk:subnet-name tag. If the subnet does not have the specified tag, we'll use its type as the name. Default: 'aws-cdk:subnet-name'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            vpc_context_query = cloud_assembly_schema.VpcContextQuery(
                account="account",
                filter={
                    "filter_key": "filter"
                },
                region="region",
            
                # the properties below are optional
                lookup_role_arn="lookupRoleArn",
                return_asymmetric_subnets=False,
                return_vpn_gateways=False,
                subnet_group_name_tag="subnetGroupNameTag"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__793c311275bf258c4baaae63fe63966f0fd334129e469b7dc83e548f2cbf5318)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
            check_type(argname="argument return_asymmetric_subnets", value=return_asymmetric_subnets, expected_type=type_hints["return_asymmetric_subnets"])
            check_type(argname="argument return_vpn_gateways", value=return_vpn_gateways, expected_type=type_hints["return_vpn_gateways"])
            check_type(argname="argument subnet_group_name_tag", value=subnet_group_name_tag, expected_type=type_hints["subnet_group_name_tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "filter": filter,
            "region": region,
        }
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn
        if return_asymmetric_subnets is not None:
            self._values["return_asymmetric_subnets"] = return_asymmetric_subnets
        if return_vpn_gateways is not None:
            self._values["return_vpn_gateways"] = return_vpn_gateways
        if subnet_group_name_tag is not None:
            self._values["subnet_group_name_tag"] = subnet_group_name_tag

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Filters to apply to the VPC.

        Filter parameters are the same as passed to DescribeVpcs.

        :see: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def return_asymmetric_subnets(self) -> typing.Optional[builtins.bool]:
        '''Whether to populate the subnetGroups field of the ``VpcContextResponse``, which contains potentially asymmetric subnet groups.

        :default: false
        '''
        result = self._values.get("return_asymmetric_subnets")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def return_vpn_gateways(self) -> typing.Optional[builtins.bool]:
        '''Whether to populate the ``vpnGatewayId`` field of the ``VpcContextResponse``, which contains the VPN Gateway ID, if one exists.

        You can explicitly
        disable this in order to avoid the lookup if you know the VPC does not have
        a VPN Gatway attached.

        :default: true
        '''
        result = self._values.get("return_vpn_gateways")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_group_name_tag(self) -> typing.Optional[builtins.str]:
        '''Optional tag for subnet group name.

        If not provided, we'll look at the aws-cdk:subnet-name tag.
        If the subnet does not have the specified tag,
        we'll use its type as the name.

        :default: 'aws-cdk:subnet-name'
        '''
        result = self._values.get("subnet_group_name_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.LoadBalancerContextQuery",
    jsii_struct_bases=[LoadBalancerFilter],
    name_mapping={
        "load_balancer_type": "loadBalancerType",
        "load_balancer_arn": "loadBalancerArn",
        "load_balancer_tags": "loadBalancerTags",
        "account": "account",
        "region": "region",
        "lookup_role_arn": "lookupRoleArn",
    },
)
class LoadBalancerContextQuery(LoadBalancerFilter):
    def __init__(
        self,
        *,
        load_balancer_type: LoadBalancerType,
        load_balancer_arn: typing.Optional[builtins.str] = None,
        load_balancer_tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        account: builtins.str,
        region: builtins.str,
        lookup_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Query input for looking up a load balancer.

        :param load_balancer_type: Filter load balancers by their type.
        :param load_balancer_arn: Find by load balancer's ARN. Default: - does not search by load balancer arn
        :param load_balancer_tags: Match load balancer tags. Default: - does not match load balancers by tags
        :param account: Query account.
        :param region: Query region.
        :param lookup_role_arn: The ARN of the role that should be used to look up the missing values. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            load_balancer_context_query = cloud_assembly_schema.LoadBalancerContextQuery(
                account="account",
                load_balancer_type=cloud_assembly_schema.LoadBalancerType.NETWORK,
                region="region",
            
                # the properties below are optional
                load_balancer_arn="loadBalancerArn",
                load_balancer_tags=[cloud_assembly_schema.Tag(
                    key="key",
                    value="value"
                )],
                lookup_role_arn="lookupRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__684496ae759db19b352bca3cc225ef7242df94dfd04fc23412be9b315f601e9a)
            check_type(argname="argument load_balancer_type", value=load_balancer_type, expected_type=type_hints["load_balancer_type"])
            check_type(argname="argument load_balancer_arn", value=load_balancer_arn, expected_type=type_hints["load_balancer_arn"])
            check_type(argname="argument load_balancer_tags", value=load_balancer_tags, expected_type=type_hints["load_balancer_tags"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument lookup_role_arn", value=lookup_role_arn, expected_type=type_hints["lookup_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer_type": load_balancer_type,
            "account": account,
            "region": region,
        }
        if load_balancer_arn is not None:
            self._values["load_balancer_arn"] = load_balancer_arn
        if load_balancer_tags is not None:
            self._values["load_balancer_tags"] = load_balancer_tags
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn

    @builtins.property
    def load_balancer_type(self) -> LoadBalancerType:
        '''Filter load balancers by their type.'''
        result = self._values.get("load_balancer_type")
        assert result is not None, "Required property 'load_balancer_type' is missing"
        return typing.cast(LoadBalancerType, result)

    @builtins.property
    def load_balancer_arn(self) -> typing.Optional[builtins.str]:
        '''Find by load balancer's ARN.

        :default: - does not search by load balancer arn
        '''
        result = self._values.get("load_balancer_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_tags(self) -> typing.Optional[typing.List[Tag]]:
        '''Match load balancer tags.

        :default: - does not match load balancers by tags
        '''
        result = self._values.get("load_balancer_tags")
        return typing.cast(typing.Optional[typing.List[Tag]], result)

    @builtins.property
    def account(self) -> builtins.str:
        '''Query account.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Query region.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role that should be used to look up the missing values.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerContextQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.cloud_assembly_schema.TestCase",
    jsii_struct_bases=[TestOptions],
    name_mapping={
        "allow_destroy": "allowDestroy",
        "cdk_command_options": "cdkCommandOptions",
        "diff_assets": "diffAssets",
        "hooks": "hooks",
        "regions": "regions",
        "stack_update_workflow": "stackUpdateWorkflow",
        "stacks": "stacks",
        "assertion_stack": "assertionStack",
        "assertion_stack_name": "assertionStackName",
    },
)
class TestCase(TestOptions):
    def __init__(
        self,
        *,
        allow_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
        cdk_command_options: typing.Optional[typing.Union[CdkCommands, typing.Dict[builtins.str, typing.Any]]] = None,
        diff_assets: typing.Optional[builtins.bool] = None,
        hooks: typing.Optional[typing.Union[Hooks, typing.Dict[builtins.str, typing.Any]]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        stack_update_workflow: typing.Optional[builtins.bool] = None,
        stacks: typing.Sequence[builtins.str],
        assertion_stack: typing.Optional[builtins.str] = None,
        assertion_stack_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Represents an integration test case.

        :param allow_destroy: List of CloudFormation resource types in this stack that can be destroyed as part of an update without failing the test. This list should only include resources that for this specific integration test we are sure will not cause errors or an outage if destroyed. For example, maybe we know that a new resource will be created first before the old resource is destroyed which prevents any outage. e.g. ['AWS::IAM::Role'] Default: - do not allow destruction of any resources on update
        :param cdk_command_options: Additional options to use for each CDK command. Default: - runner default options
        :param diff_assets: Whether or not to include asset hashes in the diff Asset hashes can introduces a lot of unneccessary noise into tests, but there are some cases where asset hashes *should* be included. For example any tests involving custom resources or bundling Default: false
        :param hooks: Additional commands to run at predefined points in the test workflow. e.g. { postDeploy: ['yarn', 'test'] } Default: - no hooks
        :param regions: Limit deployment to these regions. Default: - can run in any region
        :param stack_update_workflow: Run update workflow on this test case This should only be set to false to test scenarios that are not possible to test as part of the update workflow. Default: true
        :param stacks: Stacks that should be tested as part of this test case The stackNames will be passed as args to the cdk commands so dependent stacks will be automatically deployed unless ``exclusively`` is passed.
        :param assertion_stack: The node id of the stack that contains assertions. This is the value that can be used to deploy the stack with the CDK CLI Default: - no assertion stack
        :param assertion_stack_name: The name of the stack that contains assertions. Default: - no assertion stack

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import cloud_assembly_schema
            
            test_case = cloud_assembly_schema.TestCase(
                stacks=["stacks"],
            
                # the properties below are optional
                allow_destroy=["allowDestroy"],
                assertion_stack="assertionStack",
                assertion_stack_name="assertionStackName",
                cdk_command_options=cloud_assembly_schema.CdkCommands(
                    deploy=cloud_assembly_schema.DeployCommand(
                        args=cloud_assembly_schema.DeployOptions(
                            all=False,
                            app="app",
                            asset_metadata=False,
                            ca_bundle_path="caBundlePath",
                            change_set_name="changeSetName",
                            ci=False,
                            color=False,
                            context={
                                "context_key": "context"
                            },
                            debug=False,
                            ec2_creds=False,
                            exclusively=False,
                            execute=False,
                            force=False,
                            ignore_errors=False,
                            json=False,
                            lookups=False,
                            notices=False,
                            notification_arns=["notificationArns"],
                            output="output",
                            outputs_file="outputsFile",
                            parameters={
                                "parameters_key": "parameters"
                            },
                            path_metadata=False,
                            profile="profile",
                            proxy="proxy",
                            require_approval=cloud_assembly_schema.RequireApproval.NEVER,
                            reuse_assets=["reuseAssets"],
                            role_arn="roleArn",
                            rollback=False,
                            stacks=["stacks"],
                            staging=False,
                            strict=False,
                            toolkit_stack_name="toolkitStackName",
                            trace=False,
                            use_previous_parameters=False,
                            verbose=False,
                            version_reporting=False
                        ),
                        enabled=False,
                        expected_message="expectedMessage",
                        expect_error=False
                    ),
                    destroy=cloud_assembly_schema.DestroyCommand(
                        args=cloud_assembly_schema.DestroyOptions(
                            all=False,
                            app="app",
                            asset_metadata=False,
                            ca_bundle_path="caBundlePath",
                            color=False,
                            context={
                                "context_key": "context"
                            },
                            debug=False,
                            ec2_creds=False,
                            exclusively=False,
                            force=False,
                            ignore_errors=False,
                            json=False,
                            lookups=False,
                            notices=False,
                            output="output",
                            path_metadata=False,
                            profile="profile",
                            proxy="proxy",
                            role_arn="roleArn",
                            stacks=["stacks"],
                            staging=False,
                            strict=False,
                            trace=False,
                            verbose=False,
                            version_reporting=False
                        ),
                        enabled=False,
                        expected_message="expectedMessage",
                        expect_error=False
                    )
                ),
                diff_assets=False,
                hooks=cloud_assembly_schema.Hooks(
                    post_deploy=["postDeploy"],
                    post_destroy=["postDestroy"],
                    pre_deploy=["preDeploy"],
                    pre_destroy=["preDestroy"]
                ),
                regions=["regions"],
                stack_update_workflow=False
            )
        '''
        if isinstance(cdk_command_options, dict):
            cdk_command_options = CdkCommands(**cdk_command_options)
        if isinstance(hooks, dict):
            hooks = Hooks(**hooks)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3fe7ed770cad2fbb895987d45a3a52df9ebdb3b3e8652039785a2999e6f883)
            check_type(argname="argument allow_destroy", value=allow_destroy, expected_type=type_hints["allow_destroy"])
            check_type(argname="argument cdk_command_options", value=cdk_command_options, expected_type=type_hints["cdk_command_options"])
            check_type(argname="argument diff_assets", value=diff_assets, expected_type=type_hints["diff_assets"])
            check_type(argname="argument hooks", value=hooks, expected_type=type_hints["hooks"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument stack_update_workflow", value=stack_update_workflow, expected_type=type_hints["stack_update_workflow"])
            check_type(argname="argument stacks", value=stacks, expected_type=type_hints["stacks"])
            check_type(argname="argument assertion_stack", value=assertion_stack, expected_type=type_hints["assertion_stack"])
            check_type(argname="argument assertion_stack_name", value=assertion_stack_name, expected_type=type_hints["assertion_stack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stacks": stacks,
        }
        if allow_destroy is not None:
            self._values["allow_destroy"] = allow_destroy
        if cdk_command_options is not None:
            self._values["cdk_command_options"] = cdk_command_options
        if diff_assets is not None:
            self._values["diff_assets"] = diff_assets
        if hooks is not None:
            self._values["hooks"] = hooks
        if regions is not None:
            self._values["regions"] = regions
        if stack_update_workflow is not None:
            self._values["stack_update_workflow"] = stack_update_workflow
        if assertion_stack is not None:
            self._values["assertion_stack"] = assertion_stack
        if assertion_stack_name is not None:
            self._values["assertion_stack_name"] = assertion_stack_name

    @builtins.property
    def allow_destroy(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of CloudFormation resource types in this stack that can be destroyed as part of an update without failing the test.

        This list should only include resources that for this specific
        integration test we are sure will not cause errors or an outage if
        destroyed. For example, maybe we know that a new resource will be created
        first before the old resource is destroyed which prevents any outage.

        e.g. ['AWS::IAM::Role']

        :default: - do not allow destruction of any resources on update
        '''
        result = self._values.get("allow_destroy")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cdk_command_options(self) -> typing.Optional[CdkCommands]:
        '''Additional options to use for each CDK command.

        :default: - runner default options
        '''
        result = self._values.get("cdk_command_options")
        return typing.cast(typing.Optional[CdkCommands], result)

    @builtins.property
    def diff_assets(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to include asset hashes in the diff Asset hashes can introduces a lot of unneccessary noise into tests, but there are some cases where asset hashes *should* be included.

        For example
        any tests involving custom resources or bundling

        :default: false
        '''
        result = self._values.get("diff_assets")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def hooks(self) -> typing.Optional[Hooks]:
        '''Additional commands to run at predefined points in the test workflow.

        e.g. { postDeploy: ['yarn', 'test'] }

        :default: - no hooks
        '''
        result = self._values.get("hooks")
        return typing.cast(typing.Optional[Hooks], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Limit deployment to these regions.

        :default: - can run in any region
        '''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def stack_update_workflow(self) -> typing.Optional[builtins.bool]:
        '''Run update workflow on this test case This should only be set to false to test scenarios that are not possible to test as part of the update workflow.

        :default: true
        '''
        result = self._values.get("stack_update_workflow")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stacks(self) -> typing.List[builtins.str]:
        '''Stacks that should be tested as part of this test case The stackNames will be passed as args to the cdk commands so dependent stacks will be automatically deployed unless ``exclusively`` is passed.'''
        result = self._values.get("stacks")
        assert result is not None, "Required property 'stacks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assertion_stack(self) -> typing.Optional[builtins.str]:
        '''The node id of the stack that contains assertions.

        This is the value that can be used to deploy the stack with the CDK CLI

        :default: - no assertion stack
        '''
        result = self._values.get("assertion_stack")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assertion_stack_name(self) -> typing.Optional[builtins.str]:
        '''The name of the stack that contains assertions.

        :default: - no assertion stack
        '''
        result = self._values.get("assertion_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TestCase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AmiContextQuery",
    "ArtifactManifest",
    "ArtifactMetadataEntryType",
    "ArtifactType",
    "AssemblyManifest",
    "AssetManifest",
    "AssetManifestOptions",
    "AssetManifestProperties",
    "AvailabilityZonesContextQuery",
    "AwsCloudFormationStackProperties",
    "AwsDestination",
    "BootstrapRole",
    "CdkCommand",
    "CdkCommands",
    "ContainerImageAssetCacheOption",
    "ContainerImageAssetMetadataEntry",
    "ContextProvider",
    "DefaultCdkOptions",
    "DeployCommand",
    "DeployOptions",
    "DestroyCommand",
    "DestroyOptions",
    "DockerCacheOption",
    "DockerImageAsset",
    "DockerImageDestination",
    "DockerImageSource",
    "EndpointServiceAvailabilityZonesContextQuery",
    "FileAsset",
    "FileAssetMetadataEntry",
    "FileAssetPackaging",
    "FileDestination",
    "FileSource",
    "Hooks",
    "HostedZoneContextQuery",
    "IntegManifest",
    "KeyContextQuery",
    "LoadBalancerContextQuery",
    "LoadBalancerFilter",
    "LoadBalancerListenerContextQuery",
    "LoadBalancerListenerProtocol",
    "LoadBalancerType",
    "LoadManifestOptions",
    "Manifest",
    "MetadataEntry",
    "MissingContext",
    "NestedCloudAssemblyProperties",
    "PluginContextQuery",
    "RequireApproval",
    "RuntimeInfo",
    "SSMParameterContextQuery",
    "SecurityGroupContextQuery",
    "Tag",
    "TestCase",
    "TestOptions",
    "TreeArtifactProperties",
    "VpcContextQuery",
]

publication.publish()

def _typecheckingstub__9ad6944b308c0d053938a9bf5ce1be77af5b529135dc35a4c245384840501111(
    *,
    account: builtins.str,
    filters: typing.Mapping[builtins.str, typing.Sequence[builtins.str]],
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
    owners: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0fe0dea35f8750630dc6eb16d5f979ef40079f01dc4afec1b7ebf62d6958505(
    *,
    type: ArtifactType,
    dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[MetadataEntry, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Union[AwsCloudFormationStackProperties, typing.Dict[builtins.str, typing.Any]], typing.Union[AssetManifestProperties, typing.Dict[builtins.str, typing.Any]], typing.Union[TreeArtifactProperties, typing.Dict[builtins.str, typing.Any]], typing.Union[NestedCloudAssemblyProperties, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d707328dcc86d4e43fc56bf16523e6c309819b8983de0d413e55cdeb244d4810(
    *,
    version: builtins.str,
    artifacts: typing.Optional[typing.Mapping[builtins.str, typing.Union[ArtifactManifest, typing.Dict[builtins.str, typing.Any]]]] = None,
    missing: typing.Optional[typing.Sequence[typing.Union[MissingContext, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime: typing.Optional[typing.Union[RuntimeInfo, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95123227e2e39f7b45c300f671954210a3191a5acc352a40f4cea7ba623ee015(
    *,
    version: builtins.str,
    docker_images: typing.Optional[typing.Mapping[builtins.str, typing.Union[DockerImageAsset, typing.Dict[builtins.str, typing.Any]]]] = None,
    files: typing.Optional[typing.Mapping[builtins.str, typing.Union[FileAsset, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c77da34e0417278ebaea2f325f2a5b2793410bbe22b270a09a8899516a35f5(
    *,
    bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
    requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5d2e8772dd80ce81405cd98707a3f710c439c66cd9580fecad1be8252feae38(
    *,
    bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
    requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
    file: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e23cb5710241f65fda5e65504911a7340786a62ce9cf7c60c9cfc1d4d4a05753(
    *,
    account: builtins.str,
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662c8e7475bc8ebd11512c676ac10ca4f84539770ce9a2a5d5d96a46956fe50e(
    *,
    template_file: builtins.str,
    assume_role_arn: typing.Optional[builtins.str] = None,
    assume_role_external_id: typing.Optional[builtins.str] = None,
    bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
    cloud_formation_execution_role_arn: typing.Optional[builtins.str] = None,
    lookup_role: typing.Optional[typing.Union[BootstrapRole, typing.Dict[builtins.str, typing.Any]]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
    stack_name: typing.Optional[builtins.str] = None,
    stack_template_asset_object_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    termination_protection: typing.Optional[builtins.bool] = None,
    validate_on_synth: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e91cfad0a891b03534a612d02721f5d8d6378d9951a8f62fa2272323da013b6c(
    *,
    assume_role_arn: typing.Optional[builtins.str] = None,
    assume_role_external_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a573afe6fe73a260b78458b7d6ff4d548c9379eb945ffcadd64389efe9b6e65d(
    *,
    arn: builtins.str,
    assume_role_external_id: typing.Optional[builtins.str] = None,
    bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
    requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fab42c5155b5514b7e0da3a4196cd98c96a1d3c1d1581dc4ff88dc1fb1358903(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    expected_message: typing.Optional[builtins.str] = None,
    expect_error: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95ac9609e4f4d0c031d4e642395354b784dff236227aa06f3731df5f762d0ffc(
    *,
    deploy: typing.Optional[typing.Union[DeployCommand, typing.Dict[builtins.str, typing.Any]]] = None,
    destroy: typing.Optional[typing.Union[DestroyCommand, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9c7388f9bfe95e50651a69fc2619a3384f0dac2162a8001fd626420b069e9b(
    *,
    type: builtins.str,
    params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5331a5e47b1bb2aafb851bd548f765940424af583650927b525fa39d04be4a8(
    *,
    id: builtins.str,
    packaging: builtins.str,
    path: builtins.str,
    source_hash: builtins.str,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_ssh: typing.Optional[builtins.str] = None,
    cache_from: typing.Optional[typing.Sequence[typing.Union[ContainerImageAssetCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
    cache_to: typing.Optional[typing.Union[ContainerImageAssetCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[builtins.str] = None,
    image_tag: typing.Optional[builtins.str] = None,
    network_mode: typing.Optional[builtins.str] = None,
    outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
    platform: typing.Optional[builtins.str] = None,
    repository_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594ca36867231e310239038fdad0490ae5b2dfc45ce83bd893a483d4e4b5e150(
    *,
    all: typing.Optional[builtins.bool] = None,
    app: typing.Optional[builtins.str] = None,
    asset_metadata: typing.Optional[builtins.bool] = None,
    ca_bundle_path: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.bool] = None,
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    debug: typing.Optional[builtins.bool] = None,
    ec2_creds: typing.Optional[builtins.bool] = None,
    ignore_errors: typing.Optional[builtins.bool] = None,
    json: typing.Optional[builtins.bool] = None,
    lookups: typing.Optional[builtins.bool] = None,
    notices: typing.Optional[builtins.bool] = None,
    output: typing.Optional[builtins.str] = None,
    path_metadata: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    proxy: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    stacks: typing.Optional[typing.Sequence[builtins.str]] = None,
    staging: typing.Optional[builtins.bool] = None,
    strict: typing.Optional[builtins.bool] = None,
    trace: typing.Optional[builtins.bool] = None,
    verbose: typing.Optional[builtins.bool] = None,
    version_reporting: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c759005400637b5bd106a020b90be905666b7bd21223ad43cd2dc6c3dff6d68e(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    expected_message: typing.Optional[builtins.str] = None,
    expect_error: typing.Optional[builtins.bool] = None,
    args: typing.Optional[typing.Union[DeployOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e316f5465c42282e55b82d44529c7add374f8a6fee37838b3b05b930dea1b804(
    *,
    all: typing.Optional[builtins.bool] = None,
    app: typing.Optional[builtins.str] = None,
    asset_metadata: typing.Optional[builtins.bool] = None,
    ca_bundle_path: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.bool] = None,
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    debug: typing.Optional[builtins.bool] = None,
    ec2_creds: typing.Optional[builtins.bool] = None,
    ignore_errors: typing.Optional[builtins.bool] = None,
    json: typing.Optional[builtins.bool] = None,
    lookups: typing.Optional[builtins.bool] = None,
    notices: typing.Optional[builtins.bool] = None,
    output: typing.Optional[builtins.str] = None,
    path_metadata: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    proxy: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    stacks: typing.Optional[typing.Sequence[builtins.str]] = None,
    staging: typing.Optional[builtins.bool] = None,
    strict: typing.Optional[builtins.bool] = None,
    trace: typing.Optional[builtins.bool] = None,
    verbose: typing.Optional[builtins.bool] = None,
    version_reporting: typing.Optional[builtins.bool] = None,
    change_set_name: typing.Optional[builtins.str] = None,
    ci: typing.Optional[builtins.bool] = None,
    exclusively: typing.Optional[builtins.bool] = None,
    execute: typing.Optional[builtins.bool] = None,
    force: typing.Optional[builtins.bool] = None,
    notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    outputs_file: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    require_approval: typing.Optional[RequireApproval] = None,
    reuse_assets: typing.Optional[typing.Sequence[builtins.str]] = None,
    rollback: typing.Optional[builtins.bool] = None,
    toolkit_stack_name: typing.Optional[builtins.str] = None,
    use_previous_parameters: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d085522a7dd3e11de74ee4aabd4a610f704d28adf6c2243ef2a4196809a75cf2(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    expected_message: typing.Optional[builtins.str] = None,
    expect_error: typing.Optional[builtins.bool] = None,
    args: typing.Optional[typing.Union[DestroyOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6502d5a70ca8d3ae7dbec0f66d1e2813f2a50261460f2fd206c0533afdfabf(
    *,
    all: typing.Optional[builtins.bool] = None,
    app: typing.Optional[builtins.str] = None,
    asset_metadata: typing.Optional[builtins.bool] = None,
    ca_bundle_path: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.bool] = None,
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    debug: typing.Optional[builtins.bool] = None,
    ec2_creds: typing.Optional[builtins.bool] = None,
    ignore_errors: typing.Optional[builtins.bool] = None,
    json: typing.Optional[builtins.bool] = None,
    lookups: typing.Optional[builtins.bool] = None,
    notices: typing.Optional[builtins.bool] = None,
    output: typing.Optional[builtins.str] = None,
    path_metadata: typing.Optional[builtins.bool] = None,
    profile: typing.Optional[builtins.str] = None,
    proxy: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    stacks: typing.Optional[typing.Sequence[builtins.str]] = None,
    staging: typing.Optional[builtins.bool] = None,
    strict: typing.Optional[builtins.bool] = None,
    trace: typing.Optional[builtins.bool] = None,
    verbose: typing.Optional[builtins.bool] = None,
    version_reporting: typing.Optional[builtins.bool] = None,
    exclusively: typing.Optional[builtins.bool] = None,
    force: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cef84b1e278512e93714e32db5936e30b5b5b0d34a4c44fb2ed845b8cdd29792(
    *,
    type: builtins.str,
    params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a2a085c0212f98043b6dccf8c92e1bdc5d9e20c7266a3be7bc908b8b771cd3(
    *,
    destinations: typing.Mapping[builtins.str, typing.Union[DockerImageDestination, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[DockerImageSource, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01e136052f71999035d3e1605dff6c0878e98a56b1d1493de1cc03b20f38345a(
    *,
    assume_role_arn: typing.Optional[builtins.str] = None,
    assume_role_external_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    image_tag: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68b7dbb9ff110c1143ff2f04551d1b631fbf4f14a7e4b5b1fecac92324c1e63(
    *,
    cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
    cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
    directory: typing.Optional[builtins.str] = None,
    docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    docker_build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    docker_build_ssh: typing.Optional[builtins.str] = None,
    docker_build_target: typing.Optional[builtins.str] = None,
    docker_file: typing.Optional[builtins.str] = None,
    docker_outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
    executable: typing.Optional[typing.Sequence[builtins.str]] = None,
    network_mode: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b028a59a345f6074485bae83f874fa7eca8081fea4616b491a43cfb788b0dd28(
    *,
    account: builtins.str,
    region: builtins.str,
    service_name: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a482db8874b6a4a96f9be44511cc506737e4b70dff2a99f6ee0f1566bc96c3d8(
    *,
    destinations: typing.Mapping[builtins.str, typing.Union[FileDestination, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[FileSource, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbb3412647192d09586c63a100c01b6e55569ecafd8e050b7588e9edfd33f2b(
    *,
    artifact_hash_parameter: builtins.str,
    id: builtins.str,
    packaging: builtins.str,
    path: builtins.str,
    s3_bucket_parameter: builtins.str,
    s3_key_parameter: builtins.str,
    source_hash: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482362971cab2cc43f5645dc6db216e662ebd818f06c2cdcac27f66423f068f7(
    *,
    assume_role_arn: typing.Optional[builtins.str] = None,
    assume_role_external_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    bucket_name: builtins.str,
    object_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb32f591e1ddb63dd7deff0f14ccc9ca7747792ac0f97655b1066f5c890bf88c(
    *,
    executable: typing.Optional[typing.Sequence[builtins.str]] = None,
    packaging: typing.Optional[FileAssetPackaging] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbadd14eae9eb3722ca27183992f5c2cf9e9b0bb548e5a3a0ee7ac2d146c6f59(
    *,
    post_deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
    post_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
    pre_deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
    pre_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479c87e6b7f0a4547d04d73de1bad2d396c1e1383975038b6ca8a7ee078e9ab8(
    *,
    account: builtins.str,
    domain_name: builtins.str,
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
    private_zone: typing.Optional[builtins.bool] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5432524b6ab8526a1e8e021ba819e88be44f2dc6f4c9a47990f2c4936b028cf5(
    *,
    test_cases: typing.Mapping[builtins.str, typing.Union[TestCase, typing.Dict[builtins.str, typing.Any]]],
    version: builtins.str,
    enable_lookups: typing.Optional[builtins.bool] = None,
    synth_context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b738d31e8937d0dc914b364457cedd3794a0911b61fec9b17eb3f8ad72e53832(
    *,
    account: builtins.str,
    alias_name: builtins.str,
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b57ff0c819ed8af3b684900df083604408f77b99e70f2dd2d12b1cc7e4a8e68c(
    *,
    load_balancer_type: LoadBalancerType,
    load_balancer_arn: typing.Optional[builtins.str] = None,
    load_balancer_tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e0c4bf3a41978c03455699a53b8dc150feef48b4e8d1cb490e0e3cffa75ced7(
    *,
    load_balancer_type: LoadBalancerType,
    load_balancer_arn: typing.Optional[builtins.str] = None,
    load_balancer_tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    account: builtins.str,
    region: builtins.str,
    listener_arn: typing.Optional[builtins.str] = None,
    listener_port: typing.Optional[jsii.Number] = None,
    listener_protocol: typing.Optional[LoadBalancerListenerProtocol] = None,
    lookup_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d4beea8990d112d9f873ed9d80c8fbeb641413dbd84d56c37eb8d74fd77448(
    *,
    skip_enum_check: typing.Optional[builtins.bool] = None,
    skip_version_check: typing.Optional[builtins.bool] = None,
    topo_sort: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb4be78db16e194bc36707aee4bf2c1284ffddcd2ddfffe63450850c373f9bd(
    file_path: builtins.str,
    *,
    skip_enum_check: typing.Optional[builtins.bool] = None,
    skip_version_check: typing.Optional[builtins.bool] = None,
    topo_sort: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__252134c733b52c64fcb4e76c02ca1c3c29cbd4206194764bb4ccd634bf2b350a(
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__633f66b76e82fdca841018e97eb59fc4ea9aa150a20d1e0b3a69fbf5085bd783(
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1461b7e78a2d33c07931bce60df24a9c3db0ca9beb19b2f02d9d86e262073ffa(
    manifest: typing.Union[AssemblyManifest, typing.Dict[builtins.str, typing.Any]],
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45cd3c37aac070d85d5695adc2f1e4ecf988ca34c895e29c1ececb7de61a5f67(
    manifest: typing.Union[AssetManifest, typing.Dict[builtins.str, typing.Any]],
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87be211e9c3bb7ce042946888a960f69db963f2d5811832fbf0681bf94a6f450(
    manifest: typing.Union[IntegManifest, typing.Dict[builtins.str, typing.Any]],
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e77201bee0581d95dfd6e3150d491c958851c456cbdd8aaea71cb737197beaee(
    *,
    type: builtins.str,
    data: typing.Optional[typing.Union[builtins.str, typing.Union[FileAssetMetadataEntry, typing.Dict[builtins.str, typing.Any]], typing.Union[ContainerImageAssetMetadataEntry, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]]] = None,
    trace: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af657f9f6c83e032e4811f8db352c854d88bb8d40b052424137f1bf159f9170d(
    *,
    key: builtins.str,
    props: typing.Union[typing.Union[AmiContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[AvailabilityZonesContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[HostedZoneContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[SSMParameterContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[VpcContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[EndpointServiceAvailabilityZonesContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[LoadBalancerContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[LoadBalancerListenerContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[SecurityGroupContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[KeyContextQuery, typing.Dict[builtins.str, typing.Any]], typing.Union[PluginContextQuery, typing.Dict[builtins.str, typing.Any]]],
    provider: ContextProvider,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06bd54f69162b763b33d231a80754950d41ec566c6c02535d422732a76ced29e(
    *,
    directory_name: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e904ca937e50d9783874bf1fb0d167b1784afebb80b64c89916b1427dbbc97ed(
    *,
    plugin_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d8ff22f74ddaf52e071d67dbc65d3080f622da186b8d675c5b21733200b4c4(
    *,
    libraries: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684d2dfddbf9de1c9120fbcee643319c13ff10fa5e3227b4959d94fdac1463d5(
    *,
    account: builtins.str,
    parameter_name: builtins.str,
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab27bdfc9deaaa99cc0b29d10214dea6da9d91e77b9d18d5a5f9a2b7f4578cb4(
    *,
    account: builtins.str,
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
    security_group_id: typing.Optional[builtins.str] = None,
    security_group_name: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dff2df53008ccb9c0c772f8e5e1040e54c1f5a0e71c6267f41bf1819e91d077(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87885fac73fc14075c22fe051717d21aa5da7c4113e34310cff21b849bc534d7(
    *,
    allow_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
    cdk_command_options: typing.Optional[typing.Union[CdkCommands, typing.Dict[builtins.str, typing.Any]]] = None,
    diff_assets: typing.Optional[builtins.bool] = None,
    hooks: typing.Optional[typing.Union[Hooks, typing.Dict[builtins.str, typing.Any]]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    stack_update_workflow: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f49fc9c74b07ac016f6f246ae2bfaa0eea6382d75f9ee62c77e3b2446eec513(
    *,
    file: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__793c311275bf258c4baaae63fe63966f0fd334129e469b7dc83e548f2cbf5318(
    *,
    account: builtins.str,
    filter: typing.Mapping[builtins.str, builtins.str],
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
    return_asymmetric_subnets: typing.Optional[builtins.bool] = None,
    return_vpn_gateways: typing.Optional[builtins.bool] = None,
    subnet_group_name_tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684496ae759db19b352bca3cc225ef7242df94dfd04fc23412be9b315f601e9a(
    *,
    load_balancer_type: LoadBalancerType,
    load_balancer_arn: typing.Optional[builtins.str] = None,
    load_balancer_tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    account: builtins.str,
    region: builtins.str,
    lookup_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3fe7ed770cad2fbb895987d45a3a52df9ebdb3b3e8652039785a2999e6f883(
    *,
    allow_destroy: typing.Optional[typing.Sequence[builtins.str]] = None,
    cdk_command_options: typing.Optional[typing.Union[CdkCommands, typing.Dict[builtins.str, typing.Any]]] = None,
    diff_assets: typing.Optional[builtins.bool] = None,
    hooks: typing.Optional[typing.Union[Hooks, typing.Dict[builtins.str, typing.Any]]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    stack_update_workflow: typing.Optional[builtins.bool] = None,
    stacks: typing.Sequence[builtins.str],
    assertion_stack: typing.Optional[builtins.str] = None,
    assertion_stack_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
