'''
# AWS CDK Docker Image Assets

This module allows bundling Docker images as assets.

## Images from Dockerfile

Images are built from a local Docker context directory (with a `Dockerfile`),
uploaded to Amazon Elastic Container Registry (ECR) by the CDK toolkit
and/or your app's CI/CD pipeline, and can be naturally referenced in your CDK app.

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image")
)
```

The directory `my-image` must include a `Dockerfile`.

This will instruct the toolkit to build a Docker image from `my-image`, push it
to an Amazon ECR repository and wire the name of the repository as CloudFormation
parameters to your stack.

By default, all files in the given directory will be copied into the docker
*build context*. If there is a large directory that you know you definitely
don't need in the build context you can improve the performance by adding the
names of files and directories to ignore to a file called `.dockerignore`, or
pass them via the `exclude` property. If both are available, the patterns
found in `exclude` are appended to the patterns found in `.dockerignore`.

The `ignoreMode` property controls how the set of ignore patterns is
interpreted. The recommended setting for Docker image assets is
`IgnoreMode.DOCKER`. If the context flag
`@aws-cdk/aws-ecr-assets:dockerIgnoreSupport` is set to `true` in your
`cdk.json` (this is by default for new projects, but must be set manually for
old projects) then `IgnoreMode.DOCKER` is the default and you don't need to
configure it on the asset itself.

Use `asset.imageUri` to reference the image. It includes both the ECR image URL
and tag.

Use `asset.imageTag` to reference only the image tag.

You can optionally pass build args to the `docker build` command by specifying
the `buildArgs` property. It is recommended to skip hashing of `buildArgs` for
values that can change between different machines to maintain a consistent
asset hash.

Additionally, you can supply `buildSecrets`. Your system must have Buildkit
enabled, see https://docs.docker.com/build/buildkit/.

SSH agent sockets or keys may be passed to docker build via `buildSsh`.

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image"),
    build_args={
        "HTTP_PROXY": "http://10.20.30.2:1234"
    },
    invalidation=ecr_assets.DockerImageAssetInvalidationOptions(
        build_args=False
    )
)
```

You can optionally pass a target to the `docker build` command by specifying
the `target` property:

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image"),
    target="a-target"
)
```

You can optionally pass networking mode to the `docker build` command by specifying
the `networkMode` property:

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image"),
    network_mode=NetworkMode.HOST
)
```

You can optionally pass an alternate platform to the `docker build` command by specifying
the `platform` property:

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset, Platform


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image"),
    platform=Platform.LINUX_ARM64
)
```

You can optionally pass an array of outputs to the `docker build` command by specifying
the `outputs` property:

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset, Platform


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image"),
    outputs=["type=local,dest=out"]
)
```

You can optionally pass cache from and cache to options to cache images:

```python
from aws_cdk.aws_ecr_assets import DockerImageAsset, Platform


asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image"),
    cache_from=[ecr_assets.DockerCacheOption(type="registry", params={"ref": "ghcr.io/myorg/myimage:cache"})],
    cache_to=ecr_assets.DockerCacheOption(type="registry", params={"ref": "ghcr.io/myorg/myimage:cache", "mode": "max", "compression": "zstd"})
)
```

## Images from Tarball

Images are loaded from a local tarball, uploaded to ECR by the CDK toolkit and/or your app's CI-CD pipeline, and can be
naturally referenced in your CDK app.

```python
from aws_cdk.aws_ecr_assets import TarballImageAsset


asset = TarballImageAsset(self, "MyBuildImage",
    tarball_file="local-image.tar"
)
```

This will instruct the toolkit to add the tarball as a file asset. During deployment it will load the container image
from `local-image.tar`, push it to an Amazon ECR repository and wire the name of the repository as CloudFormation parameters
to your stack.

## Publishing images to ECR repositories

`DockerImageAsset` is designed for seamless build & consumption of image assets by CDK code deployed to multiple environments
through the CDK CLI or through CI/CD workflows. To that end, the ECR repository behind this construct is controlled by the AWS CDK.
The mechanics of where these images are published and how are intentionally kept as an implementation detail, and the construct
does not support customizations such as specifying the ECR repository name or tags.

If you are looking for a way to *publish* image assets to an ECR repository in your control, you should consider using
[cdklabs/cdk-ecr-deployment](https://github.com/cdklabs/cdk-ecr-deployment), which is able to replicate an image asset from the CDK-controlled ECR repository to a repository of
your choice.

Here an example from the [cdklabs/cdk-ecr-deployment](https://github.com/cdklabs/cdk-ecr-deployment) project:

```text
// This example available in TypeScript only

import { DockerImageAsset } from 'aws-cdk-lib/aws-ecr-assets';
import * as ecrdeploy from 'cdk-ecr-deployment';

const image = new DockerImageAsset(this, 'CDKDockerImage', {
  directory: path.join(__dirname, 'docker'),
});

new ecrdeploy.ECRDeployment(this, 'DeployDockerImage', {
  src: new ecrdeploy.DockerImageName(image.imageUri),
  dest: new ecrdeploy.DockerImageName(`${cdk.Aws.ACCOUNT_ID}.dkr.ecr.us-west-2.amazonaws.com/test:nginx`),
});
```

⚠️ Please note that this is a 3rd-party construct library and is not officially supported by AWS.
You are welcome to +1 [this GitHub issue](https://github.com/aws/aws-cdk/issues/12597) if you would like to see
native support for this use-case in the AWS CDK.

## Pull Permissions

Depending on the consumer of your image asset, you will need to make sure
the principal has permissions to pull the image.

In most cases, you should use the `asset.repository.grantPull(principal)`
method. This will modify the IAM policy of the principal to allow it to
pull images from this repository.

If the pulling principal is not in the same account or is an AWS service that
doesn't assume a role in your account (e.g. AWS CodeBuild), pull permissions
must be granted on the **resource policy** (and not on the principal's policy).
To do that, you can use `asset.repository.addToResourcePolicy(statement)` to
grant the desired principal the following permissions: "ecr:GetDownloadUrlForLayer",
"ecr:BatchGetImage" and "ecr:BatchCheckLayerAvailability".
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
    FileFingerprintOptions as _FileFingerprintOptions_115b8b51,
    IgnoreMode as _IgnoreMode_655a98e8,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
)
from ..aws_ecr import IRepository as _IRepository_e6004aa6


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr_assets.DockerCacheOption",
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

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_ecr_assets import DockerImageAsset, Platform
            
            
            asset = DockerImageAsset(self, "MyBuildImage",
                directory=path.join(__dirname, "my-image"),
                cache_from=[ecr_assets.DockerCacheOption(type="registry", params={"ref": "ghcr.io/myorg/myimage:cache"})],
                cache_to=ecr_assets.DockerCacheOption(type="registry", params={"ref": "ghcr.io/myorg/myimage:cache", "mode": "max", "compression": "zstd"})
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad9419c3da81effe8638841dcb5d0fc89a048d78025f5679f399689b950f5256)
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


class DockerImageAsset(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr_assets.DockerImageAsset",
):
    '''An asset that represents a Docker image.

    The image will be created in build time and uploaded to an ECR repository.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_ecr_assets import DockerImageAsset
        
        
        asset = DockerImageAsset(self, "MyBuildImage",
            directory=path.join(__dirname, "my-image"),
            build_args={
                "HTTP_PROXY": "http://10.20.30.2:1234"
            },
            invalidation=ecr_assets.DockerImageAssetInvalidationOptions(
                build_args=False
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        directory: builtins.str,
        asset_name: typing.Optional[builtins.str] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_ssh: typing.Optional[builtins.str] = None,
        cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
        cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[builtins.str] = None,
        invalidation: typing.Optional[typing.Union["DockerImageAssetInvalidationOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        network_mode: typing.Optional["NetworkMode"] = None,
        outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
        platform: typing.Optional["Platform"] = None,
        target: typing.Optional[builtins.str] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param directory: The directory where the Dockerfile is stored. Any directory inside with a name that matches the CDK output folder (cdk.out by default) will be excluded from the asset
        :param asset_name: Unique identifier of the docker image asset and its potential revisions. Required if using AppScopedStagingSynthesizer. Default: - no asset name
        :param build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param build_secrets: Build secrets. Docker BuildKit must be enabled to use build secrets. Default: - no build secrets
        :param build_ssh: SSH agent socket or keys to pass to the ``docker build`` command. Docker BuildKit must be enabled to use the ssh flag Default: - no --ssh flag
        :param cache_from: Cache from options to pass to the ``docker build`` command. Default: - no cache from options are passed to the build command
        :param cache_to: Cache to options to pass to the ``docker build`` command. Default: - no cache to options are passed to the build command
        :param file: Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param invalidation: Options to control which parameters are used to invalidate the asset hash. Default: - hash all parameters
        :param network_mode: Networking mode for the RUN commands during build. Support docker API 1.25+. Default: - no networking mode specified (the default networking mode ``NetworkMode.DEFAULT`` will be used)
        :param outputs: Outputs to pass to the ``docker build`` command. Default: - no outputs are passed to the build command (default outputs are used)
        :param platform: Platform to build for. *Requires Docker Buildx*. Default: - no platform specified (the current machine architecture will be used)
        :param target: Docker target to build to. Default: - no target
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__797fbc31925afd247c6567a5b5c30dcdc13a3d9b17aba80ece42c86bd04216a7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DockerImageAssetProps(
            directory=directory,
            asset_name=asset_name,
            build_args=build_args,
            build_secrets=build_secrets,
            build_ssh=build_ssh,
            cache_from=cache_from,
            cache_to=cache_to,
            file=file,
            invalidation=invalidation,
            network_mode=network_mode,
            outputs=outputs,
            platform=platform,
            target=target,
            extra_hash=extra_hash,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addResourceMetadata")
    def add_resource_metadata(
        self,
        resource: _CfnResource_9df397a6,
        resource_property: builtins.str,
    ) -> None:
        '''Adds CloudFormation template metadata to the specified resource with information that indicates which resource property is mapped to this local asset.

        This can be used by tools such as SAM CLI to provide local
        experience such as local invocation and debugging of Lambda functions.

        Asset metadata will only be included if the stack is synthesized with the
        "aws:cdk:enable-asset-metadata" context key defined, which is the default
        behavior when synthesizing via the CDK Toolkit.

        :param resource: The CloudFormation resource which is using this asset [disable-awslint:ref-via-interface].
        :param resource_property: The property name where this asset is referenced.

        :see: https://github.com/aws/aws-cdk/issues/1432
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c4a1c0cfa93309b38627e98ca811fbe0fe946fcef54da4d678fbbb020869aa9)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument resource_property", value=resource_property, expected_type=type_hints["resource_property"])
        return typing.cast(None, jsii.invoke(self, "addResourceMetadata", [resource, resource_property]))

    @builtins.property
    @jsii.member(jsii_name="assetHash")
    def asset_hash(self) -> builtins.str:
        '''A hash of this asset, which is available at construction time.

        As this is a plain string, it
        can be used in construct IDs in order to enforce creation of a new resource when the content
        hash has changed.
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetHash"))

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> builtins.str:
        '''The tag of this asset when it is uploaded to ECR.

        The tag may differ from the assetHash if a stack synthesizer adds a dockerTagPrefix.
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageTag"))

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> builtins.str:
        '''The full URI of the image (including a tag).

        Use this reference to pull
        the asset.
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a2eae0bc05bbae9216a5746bc31160fa3e0fb1dfb204b05e8b4460c1d592652)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> _IRepository_e6004aa6:
        '''Repository where the image is stored.'''
        return typing.cast(_IRepository_e6004aa6, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: _IRepository_e6004aa6) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec71b1b90f7f6ec2ffd8b6786f94c82f25f01c9dd8e87f97fb3e6ceab41a9ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr_assets.DockerImageAssetInvalidationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "build_args": "buildArgs",
        "build_secrets": "buildSecrets",
        "build_ssh": "buildSsh",
        "extra_hash": "extraHash",
        "file": "file",
        "network_mode": "networkMode",
        "outputs": "outputs",
        "platform": "platform",
        "repository_name": "repositoryName",
        "target": "target",
    },
)
class DockerImageAssetInvalidationOptions:
    def __init__(
        self,
        *,
        build_args: typing.Optional[builtins.bool] = None,
        build_secrets: typing.Optional[builtins.bool] = None,
        build_ssh: typing.Optional[builtins.bool] = None,
        extra_hash: typing.Optional[builtins.bool] = None,
        file: typing.Optional[builtins.bool] = None,
        network_mode: typing.Optional[builtins.bool] = None,
        outputs: typing.Optional[builtins.bool] = None,
        platform: typing.Optional[builtins.bool] = None,
        repository_name: typing.Optional[builtins.bool] = None,
        target: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options to control invalidation of ``DockerImageAsset`` asset hashes.

        :param build_args: Use ``buildArgs`` while calculating the asset hash. Default: true
        :param build_secrets: Use ``buildSecrets`` while calculating the asset hash. Default: true
        :param build_ssh: Use ``buildSsh`` while calculating the asset hash. Default: true
        :param extra_hash: Use ``extraHash`` while calculating the asset hash. Default: true
        :param file: Use ``file`` while calculating the asset hash. Default: true
        :param network_mode: Use ``networkMode`` while calculating the asset hash. Default: true
        :param outputs: Use ``outputs`` while calculating the asset hash. Default: true
        :param platform: Use ``platform`` while calculating the asset hash. Default: true
        :param repository_name: Use ``repositoryName`` while calculating the asset hash. Default: true
        :param target: Use ``target`` while calculating the asset hash. Default: true

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_ecr_assets import DockerImageAsset
            
            
            asset = DockerImageAsset(self, "MyBuildImage",
                directory=path.join(__dirname, "my-image"),
                build_args={
                    "HTTP_PROXY": "http://10.20.30.2:1234"
                },
                invalidation=ecr_assets.DockerImageAssetInvalidationOptions(
                    build_args=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81627cbb76e02c4366e7249ba22ecc8384c24639f62db324ccde3c3dd90d6d80)
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument build_secrets", value=build_secrets, expected_type=type_hints["build_secrets"])
            check_type(argname="argument build_ssh", value=build_ssh, expected_type=type_hints["build_ssh"])
            check_type(argname="argument extra_hash", value=extra_hash, expected_type=type_hints["extra_hash"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if build_args is not None:
            self._values["build_args"] = build_args
        if build_secrets is not None:
            self._values["build_secrets"] = build_secrets
        if build_ssh is not None:
            self._values["build_ssh"] = build_ssh
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash
        if file is not None:
            self._values["file"] = file
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
    def build_args(self) -> typing.Optional[builtins.bool]:
        '''Use ``buildArgs`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def build_secrets(self) -> typing.Optional[builtins.bool]:
        '''Use ``buildSecrets`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("build_secrets")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def build_ssh(self) -> typing.Optional[builtins.bool]:
        '''Use ``buildSsh`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("build_ssh")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.bool]:
        '''Use ``extraHash`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("extra_hash")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def file(self) -> typing.Optional[builtins.bool]:
        '''Use ``file`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.bool]:
        '''Use ``networkMode`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outputs(self) -> typing.Optional[builtins.bool]:
        '''Use ``outputs`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.bool]:
        '''Use ``platform`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.bool]:
        '''Use ``repositoryName`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.bool]:
        '''Use ``target`` while calculating the asset hash.

        :default: true
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageAssetInvalidationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr_assets.DockerImageAssetOptions",
    jsii_struct_bases=[_FileFingerprintOptions_115b8b51],
    name_mapping={
        "exclude": "exclude",
        "follow_symlinks": "followSymlinks",
        "ignore_mode": "ignoreMode",
        "extra_hash": "extraHash",
        "asset_name": "assetName",
        "build_args": "buildArgs",
        "build_secrets": "buildSecrets",
        "build_ssh": "buildSsh",
        "cache_from": "cacheFrom",
        "cache_to": "cacheTo",
        "file": "file",
        "invalidation": "invalidation",
        "network_mode": "networkMode",
        "outputs": "outputs",
        "platform": "platform",
        "target": "target",
    },
)
class DockerImageAssetOptions(_FileFingerprintOptions_115b8b51):
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        asset_name: typing.Optional[builtins.str] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_ssh: typing.Optional[builtins.str] = None,
        cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
        cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[builtins.str] = None,
        invalidation: typing.Optional[typing.Union[DockerImageAssetInvalidationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        network_mode: typing.Optional["NetworkMode"] = None,
        outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
        platform: typing.Optional["Platform"] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for DockerImageAsset.

        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param asset_name: Unique identifier of the docker image asset and its potential revisions. Required if using AppScopedStagingSynthesizer. Default: - no asset name
        :param build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param build_secrets: Build secrets. Docker BuildKit must be enabled to use build secrets. Default: - no build secrets
        :param build_ssh: SSH agent socket or keys to pass to the ``docker build`` command. Docker BuildKit must be enabled to use the ssh flag Default: - no --ssh flag
        :param cache_from: Cache from options to pass to the ``docker build`` command. Default: - no cache from options are passed to the build command
        :param cache_to: Cache to options to pass to the ``docker build`` command. Default: - no cache to options are passed to the build command
        :param file: Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param invalidation: Options to control which parameters are used to invalidate the asset hash. Default: - hash all parameters
        :param network_mode: Networking mode for the RUN commands during build. Support docker API 1.25+. Default: - no networking mode specified (the default networking mode ``NetworkMode.DEFAULT`` will be used)
        :param outputs: Outputs to pass to the ``docker build`` command. Default: - no outputs are passed to the build command (default outputs are used)
        :param platform: Platform to build for. *Requires Docker Buildx*. Default: - no platform specified (the current machine architecture will be used)
        :param target: Docker target to build to. Default: - no target

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ecr_assets as ecr_assets
            
            # network_mode: ecr_assets.NetworkMode
            # platform: ecr_assets.Platform
            
            docker_image_asset_options = ecr_assets.DockerImageAssetOptions(
                asset_name="assetName",
                build_args={
                    "build_args_key": "buildArgs"
                },
                build_secrets={
                    "build_secrets_key": "buildSecrets"
                },
                build_ssh="buildSsh",
                cache_from=[ecr_assets.DockerCacheOption(
                    type="type",
            
                    # the properties below are optional
                    params={
                        "params_key": "params"
                    }
                )],
                cache_to=ecr_assets.DockerCacheOption(
                    type="type",
            
                    # the properties below are optional
                    params={
                        "params_key": "params"
                    }
                ),
                exclude=["exclude"],
                extra_hash="extraHash",
                file="file",
                follow_symlinks=cdk.SymlinkFollowMode.NEVER,
                ignore_mode=cdk.IgnoreMode.GLOB,
                invalidation=ecr_assets.DockerImageAssetInvalidationOptions(
                    build_args=False,
                    build_secrets=False,
                    build_ssh=False,
                    extra_hash=False,
                    file=False,
                    network_mode=False,
                    outputs=False,
                    platform=False,
                    repository_name=False,
                    target=False
                ),
                network_mode=network_mode,
                outputs=["outputs"],
                platform=platform,
                target="target"
            )
        '''
        if isinstance(cache_to, dict):
            cache_to = DockerCacheOption(**cache_to)
        if isinstance(invalidation, dict):
            invalidation = DockerImageAssetInvalidationOptions(**invalidation)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be58b9ab6157641d31b553709d8decad6c9801460bec8e3ff07aadc336f83bff)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument follow_symlinks", value=follow_symlinks, expected_type=type_hints["follow_symlinks"])
            check_type(argname="argument ignore_mode", value=ignore_mode, expected_type=type_hints["ignore_mode"])
            check_type(argname="argument extra_hash", value=extra_hash, expected_type=type_hints["extra_hash"])
            check_type(argname="argument asset_name", value=asset_name, expected_type=type_hints["asset_name"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument build_secrets", value=build_secrets, expected_type=type_hints["build_secrets"])
            check_type(argname="argument build_ssh", value=build_ssh, expected_type=type_hints["build_ssh"])
            check_type(argname="argument cache_from", value=cache_from, expected_type=type_hints["cache_from"])
            check_type(argname="argument cache_to", value=cache_to, expected_type=type_hints["cache_to"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument invalidation", value=invalidation, expected_type=type_hints["invalidation"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow_symlinks is not None:
            self._values["follow_symlinks"] = follow_symlinks
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash
        if asset_name is not None:
            self._values["asset_name"] = asset_name
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
        if invalidation is not None:
            self._values["invalidation"] = invalidation
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if outputs is not None:
            self._values["outputs"] = outputs
        if platform is not None:
            self._values["platform"] = platform
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''File paths matching the patterns will be excluded.

        See ``ignoreMode`` to set the matching behavior.
        Has no effect on Assets bundled using the ``bundling`` property.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow_symlinks(self) -> typing.Optional[_SymlinkFollowMode_047ec1f6]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow_symlinks")
        return typing.cast(typing.Optional[_SymlinkFollowMode_047ec1f6], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional[_IgnoreMode_655a98e8]:
        '''The ignore behavior to use for ``exclude`` patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional[_IgnoreMode_655a98e8], result)

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.str]:
        '''Extra information to encode into the fingerprint (e.g. build instructions and other inputs).

        :default: - hash is only based on source content
        '''
        result = self._values.get("extra_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_name(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the docker image asset and its potential revisions.

        Required if using AppScopedStagingSynthesizer.

        :default: - no asset name
        '''
        result = self._values.get("asset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build args to pass to the ``docker build`` command.

        Since Docker build arguments are resolved before deployment, keys and
        values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or
        ``queue.queueUrl``).

        :default: - no build args are passed
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_secrets(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build secrets.

        Docker BuildKit must be enabled to use build secrets.

        :default: - no build secrets

        :see: https://docs.docker.com/build/buildkit/

        Example::

            from aws_cdk import DockerBuildSecret
            
            
            build_secrets = {
                "MY_SECRET": DockerBuildSecret.from_src("file.txt")
            }
        '''
        result = self._values.get("build_secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_ssh(self) -> typing.Optional[builtins.str]:
        '''SSH agent socket or keys to pass to the ``docker build`` command.

        Docker BuildKit must be enabled to use the ssh flag

        :default: - no --ssh flag

        :see: https://docs.docker.com/build/buildkit/
        '''
        result = self._values.get("build_ssh")
        return typing.cast(typing.Optional[builtins.str], result)

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
    def file(self) -> typing.Optional[builtins.str]:
        '''Path to the Dockerfile (relative to the directory).

        :default: 'Dockerfile'
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invalidation(self) -> typing.Optional[DockerImageAssetInvalidationOptions]:
        '''Options to control which parameters are used to invalidate the asset hash.

        :default: - hash all parameters
        '''
        result = self._values.get("invalidation")
        return typing.cast(typing.Optional[DockerImageAssetInvalidationOptions], result)

    @builtins.property
    def network_mode(self) -> typing.Optional["NetworkMode"]:
        '''Networking mode for the RUN commands during build.

        Support docker API 1.25+.

        :default: - no networking mode specified (the default networking mode ``NetworkMode.DEFAULT`` will be used)
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional["NetworkMode"], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Outputs to pass to the ``docker build`` command.

        :default: - no outputs are passed to the build command (default outputs are used)

        :see: https://docs.docker.com/engine/reference/commandline/build/#custom-build-outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def platform(self) -> typing.Optional["Platform"]:
        '''Platform to build for.

        *Requires Docker Buildx*.

        :default: - no platform specified (the current machine architecture will be used)
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional["Platform"], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docker target to build to.

        :default: - no target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageAssetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr_assets.DockerImageAssetProps",
    jsii_struct_bases=[DockerImageAssetOptions],
    name_mapping={
        "exclude": "exclude",
        "follow_symlinks": "followSymlinks",
        "ignore_mode": "ignoreMode",
        "extra_hash": "extraHash",
        "asset_name": "assetName",
        "build_args": "buildArgs",
        "build_secrets": "buildSecrets",
        "build_ssh": "buildSsh",
        "cache_from": "cacheFrom",
        "cache_to": "cacheTo",
        "file": "file",
        "invalidation": "invalidation",
        "network_mode": "networkMode",
        "outputs": "outputs",
        "platform": "platform",
        "target": "target",
        "directory": "directory",
    },
)
class DockerImageAssetProps(DockerImageAssetOptions):
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        asset_name: typing.Optional[builtins.str] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_ssh: typing.Optional[builtins.str] = None,
        cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
        cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[builtins.str] = None,
        invalidation: typing.Optional[typing.Union[DockerImageAssetInvalidationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        network_mode: typing.Optional["NetworkMode"] = None,
        outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
        platform: typing.Optional["Platform"] = None,
        target: typing.Optional[builtins.str] = None,
        directory: builtins.str,
    ) -> None:
        '''Props for DockerImageAssets.

        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param asset_name: Unique identifier of the docker image asset and its potential revisions. Required if using AppScopedStagingSynthesizer. Default: - no asset name
        :param build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param build_secrets: Build secrets. Docker BuildKit must be enabled to use build secrets. Default: - no build secrets
        :param build_ssh: SSH agent socket or keys to pass to the ``docker build`` command. Docker BuildKit must be enabled to use the ssh flag Default: - no --ssh flag
        :param cache_from: Cache from options to pass to the ``docker build`` command. Default: - no cache from options are passed to the build command
        :param cache_to: Cache to options to pass to the ``docker build`` command. Default: - no cache to options are passed to the build command
        :param file: Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param invalidation: Options to control which parameters are used to invalidate the asset hash. Default: - hash all parameters
        :param network_mode: Networking mode for the RUN commands during build. Support docker API 1.25+. Default: - no networking mode specified (the default networking mode ``NetworkMode.DEFAULT`` will be used)
        :param outputs: Outputs to pass to the ``docker build`` command. Default: - no outputs are passed to the build command (default outputs are used)
        :param platform: Platform to build for. *Requires Docker Buildx*. Default: - no platform specified (the current machine architecture will be used)
        :param target: Docker target to build to. Default: - no target
        :param directory: The directory where the Dockerfile is stored. Any directory inside with a name that matches the CDK output folder (cdk.out by default) will be excluded from the asset

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_ecr_assets import DockerImageAsset
            
            
            asset = DockerImageAsset(self, "MyBuildImage",
                directory=path.join(__dirname, "my-image"),
                build_args={
                    "HTTP_PROXY": "http://10.20.30.2:1234"
                },
                invalidation=ecr_assets.DockerImageAssetInvalidationOptions(
                    build_args=False
                )
            )
        '''
        if isinstance(cache_to, dict):
            cache_to = DockerCacheOption(**cache_to)
        if isinstance(invalidation, dict):
            invalidation = DockerImageAssetInvalidationOptions(**invalidation)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1abde6bc94231492c7b40171b32143e7c5533e907120fe3e3c2ebeca225cefd9)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument follow_symlinks", value=follow_symlinks, expected_type=type_hints["follow_symlinks"])
            check_type(argname="argument ignore_mode", value=ignore_mode, expected_type=type_hints["ignore_mode"])
            check_type(argname="argument extra_hash", value=extra_hash, expected_type=type_hints["extra_hash"])
            check_type(argname="argument asset_name", value=asset_name, expected_type=type_hints["asset_name"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument build_secrets", value=build_secrets, expected_type=type_hints["build_secrets"])
            check_type(argname="argument build_ssh", value=build_ssh, expected_type=type_hints["build_ssh"])
            check_type(argname="argument cache_from", value=cache_from, expected_type=type_hints["cache_from"])
            check_type(argname="argument cache_to", value=cache_to, expected_type=type_hints["cache_to"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument invalidation", value=invalidation, expected_type=type_hints["invalidation"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory": directory,
        }
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow_symlinks is not None:
            self._values["follow_symlinks"] = follow_symlinks
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash
        if asset_name is not None:
            self._values["asset_name"] = asset_name
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
        if invalidation is not None:
            self._values["invalidation"] = invalidation
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if outputs is not None:
            self._values["outputs"] = outputs
        if platform is not None:
            self._values["platform"] = platform
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''File paths matching the patterns will be excluded.

        See ``ignoreMode`` to set the matching behavior.
        Has no effect on Assets bundled using the ``bundling`` property.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow_symlinks(self) -> typing.Optional[_SymlinkFollowMode_047ec1f6]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow_symlinks")
        return typing.cast(typing.Optional[_SymlinkFollowMode_047ec1f6], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional[_IgnoreMode_655a98e8]:
        '''The ignore behavior to use for ``exclude`` patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional[_IgnoreMode_655a98e8], result)

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.str]:
        '''Extra information to encode into the fingerprint (e.g. build instructions and other inputs).

        :default: - hash is only based on source content
        '''
        result = self._values.get("extra_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_name(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the docker image asset and its potential revisions.

        Required if using AppScopedStagingSynthesizer.

        :default: - no asset name
        '''
        result = self._values.get("asset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build args to pass to the ``docker build`` command.

        Since Docker build arguments are resolved before deployment, keys and
        values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or
        ``queue.queueUrl``).

        :default: - no build args are passed
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_secrets(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build secrets.

        Docker BuildKit must be enabled to use build secrets.

        :default: - no build secrets

        :see: https://docs.docker.com/build/buildkit/

        Example::

            from aws_cdk import DockerBuildSecret
            
            
            build_secrets = {
                "MY_SECRET": DockerBuildSecret.from_src("file.txt")
            }
        '''
        result = self._values.get("build_secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_ssh(self) -> typing.Optional[builtins.str]:
        '''SSH agent socket or keys to pass to the ``docker build`` command.

        Docker BuildKit must be enabled to use the ssh flag

        :default: - no --ssh flag

        :see: https://docs.docker.com/build/buildkit/
        '''
        result = self._values.get("build_ssh")
        return typing.cast(typing.Optional[builtins.str], result)

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
    def file(self) -> typing.Optional[builtins.str]:
        '''Path to the Dockerfile (relative to the directory).

        :default: 'Dockerfile'
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invalidation(self) -> typing.Optional[DockerImageAssetInvalidationOptions]:
        '''Options to control which parameters are used to invalidate the asset hash.

        :default: - hash all parameters
        '''
        result = self._values.get("invalidation")
        return typing.cast(typing.Optional[DockerImageAssetInvalidationOptions], result)

    @builtins.property
    def network_mode(self) -> typing.Optional["NetworkMode"]:
        '''Networking mode for the RUN commands during build.

        Support docker API 1.25+.

        :default: - no networking mode specified (the default networking mode ``NetworkMode.DEFAULT`` will be used)
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional["NetworkMode"], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Outputs to pass to the ``docker build`` command.

        :default: - no outputs are passed to the build command (default outputs are used)

        :see: https://docs.docker.com/engine/reference/commandline/build/#custom-build-outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def platform(self) -> typing.Optional["Platform"]:
        '''Platform to build for.

        *Requires Docker Buildx*.

        :default: - no platform specified (the current machine architecture will be used)
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional["Platform"], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docker target to build to.

        :default: - no target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> builtins.str:
        '''The directory where the Dockerfile is stored.

        Any directory inside with a name that matches the CDK output folder (cdk.out by default) will be excluded from the asset
        '''
        result = self._values.get("directory")
        assert result is not None, "Required property 'directory' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageAssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkMode(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr_assets.NetworkMode",
):
    '''networking mode on build time supported by docker.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode
        
        
        asset = DockerImageAsset(self, "MyBuildImage",
            directory=path.join(__dirname, "my-image"),
            network_mode=NetworkMode.HOST
        )
    '''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, mode: builtins.str) -> "NetworkMode":
        '''Used to specify a custom networking mode Use this if the networking mode name is not yet supported by the CDK.

        :param mode: The networking mode to use for docker build.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f8d8c6403f901d8551692a871bf90e61484d2689a91a2d4657cfbb8fbc027ef)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        return typing.cast("NetworkMode", jsii.sinvoke(cls, "custom", [mode]))

    @jsii.member(jsii_name="fromContainer")
    @builtins.classmethod
    def from_container(cls, container_id: builtins.str) -> "NetworkMode":
        '''Reuse another container's network stack.

        :param container_id: The target container's id or name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a508fd6d847e45dec0e540f453d59e2c2ff0115f17e6ce130b364d3bd85feb)
            check_type(argname="argument container_id", value=container_id, expected_type=type_hints["container_id"])
        return typing.cast("NetworkMode", jsii.sinvoke(cls, "fromContainer", [container_id]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT")
    def DEFAULT(cls) -> "NetworkMode":
        '''The default networking mode if omitted, create a network stack on the default Docker bridge.'''
        return typing.cast("NetworkMode", jsii.sget(cls, "DEFAULT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HOST")
    def HOST(cls) -> "NetworkMode":
        '''Use the Docker host network stack.'''
        return typing.cast("NetworkMode", jsii.sget(cls, "HOST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NONE")
    def NONE(cls) -> "NetworkMode":
        '''Disable the network stack, only the loopback device will be created.'''
        return typing.cast("NetworkMode", jsii.sget(cls, "NONE"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        '''The networking mode to use for docker build.'''
        return typing.cast(builtins.str, jsii.get(self, "mode"))


class Platform(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr_assets.Platform",
):
    '''platform supported by docker.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_ecr_assets import DockerImageAsset, Platform
        
        
        asset = DockerImageAsset(self, "MyBuildImage",
            directory=path.join(__dirname, "my-image"),
            platform=Platform.LINUX_ARM64
        )
    '''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, platform: builtins.str) -> "Platform":
        '''Used to specify a custom platform Use this if the platform name is not yet supported by the CDK.

        :param platform: The platform to use for docker build.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cca0d33972ff79dfe541d669145958c23cec6650e40df29cd7caec618b0cd7e)
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
        return typing.cast("Platform", jsii.sinvoke(cls, "custom", [platform]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_AMD64")
    def LINUX_AMD64(cls) -> "Platform":
        '''Build for linux/amd64.'''
        return typing.cast("Platform", jsii.sget(cls, "LINUX_AMD64"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64")
    def LINUX_ARM64(cls) -> "Platform":
        '''Build for linux/arm64.'''
        return typing.cast("Platform", jsii.sget(cls, "LINUX_ARM64"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''The platform to use for docker build.'''
        return typing.cast(builtins.str, jsii.get(self, "platform"))


class TarballImageAsset(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr_assets.TarballImageAsset",
):
    '''An asset that represents a Docker image.

    The image will loaded from an existing tarball and uploaded to an ECR repository.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_ecr_assets import TarballImageAsset
        
        
        asset = TarballImageAsset(self, "MyBuildImage",
            tarball_file="local-image.tar"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        tarball_file: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param tarball_file: Absolute path to the tarball. It is recommended to to use the script running directory (e.g. ``__dirname`` in Node.js projects or dirname of ``__file__`` in Python) if your tarball is located as a resource inside your project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e0eaaf11f2e3e296d6157cf12d477a55316a9aefb390c2f9de1711f911d5450)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TarballImageAssetProps(tarball_file=tarball_file)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="assetHash")
    def asset_hash(self) -> builtins.str:
        '''A hash of this asset, which is available at construction time.

        As this is a plain string, it
        can be used in construct IDs in order to enforce creation of a new resource when the content
        hash has changed.
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetHash"))

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> builtins.str:
        '''The tag of this asset when it is uploaded to ECR.

        The tag may differ from the assetHash if a stack synthesizer adds a dockerTagPrefix.
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageTag"))

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> builtins.str:
        '''The full URI of the image (including a tag).

        Use this reference to pull
        the asset.
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e5be1a7955548e99522c60499ad4723f8d659920228401ac7006d323cd4ee2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> _IRepository_e6004aa6:
        '''Repository where the image is stored.'''
        return typing.cast(_IRepository_e6004aa6, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: _IRepository_e6004aa6) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb91ed092745a33fafd3df8d94f545ae143be6b4949103c115bc71350c947bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr_assets.TarballImageAssetProps",
    jsii_struct_bases=[],
    name_mapping={"tarball_file": "tarballFile"},
)
class TarballImageAssetProps:
    def __init__(self, *, tarball_file: builtins.str) -> None:
        '''Options for TarballImageAsset.

        :param tarball_file: Absolute path to the tarball. It is recommended to to use the script running directory (e.g. ``__dirname`` in Node.js projects or dirname of ``__file__`` in Python) if your tarball is located as a resource inside your project.

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_ecr_assets import TarballImageAsset
            
            
            asset = TarballImageAsset(self, "MyBuildImage",
                tarball_file="local-image.tar"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1555ea2241a0a5236409111ebbad425ecc370ebc8987c4a7871719d32389658b)
            check_type(argname="argument tarball_file", value=tarball_file, expected_type=type_hints["tarball_file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tarball_file": tarball_file,
        }

    @builtins.property
    def tarball_file(self) -> builtins.str:
        '''Absolute path to the tarball.

        It is recommended to to use the script running directory (e.g. ``__dirname``
        in Node.js projects or dirname of ``__file__`` in Python) if your tarball
        is located as a resource inside your project.
        '''
        result = self._values.get("tarball_file")
        assert result is not None, "Required property 'tarball_file' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TarballImageAssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DockerCacheOption",
    "DockerImageAsset",
    "DockerImageAssetInvalidationOptions",
    "DockerImageAssetOptions",
    "DockerImageAssetProps",
    "NetworkMode",
    "Platform",
    "TarballImageAsset",
    "TarballImageAssetProps",
]

publication.publish()

def _typecheckingstub__ad9419c3da81effe8638841dcb5d0fc89a048d78025f5679f399689b950f5256(
    *,
    type: builtins.str,
    params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797fbc31925afd247c6567a5b5c30dcdc13a3d9b17aba80ece42c86bd04216a7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    directory: builtins.str,
    asset_name: typing.Optional[builtins.str] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_ssh: typing.Optional[builtins.str] = None,
    cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
    cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[builtins.str] = None,
    invalidation: typing.Optional[typing.Union[DockerImageAssetInvalidationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    network_mode: typing.Optional[NetworkMode] = None,
    outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
    platform: typing.Optional[Platform] = None,
    target: typing.Optional[builtins.str] = None,
    extra_hash: typing.Optional[builtins.str] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c4a1c0cfa93309b38627e98ca811fbe0fe946fcef54da4d678fbbb020869aa9(
    resource: _CfnResource_9df397a6,
    resource_property: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2eae0bc05bbae9216a5746bc31160fa3e0fb1dfb204b05e8b4460c1d592652(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec71b1b90f7f6ec2ffd8b6786f94c82f25f01c9dd8e87f97fb3e6ceab41a9ba(
    value: _IRepository_e6004aa6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81627cbb76e02c4366e7249ba22ecc8384c24639f62db324ccde3c3dd90d6d80(
    *,
    build_args: typing.Optional[builtins.bool] = None,
    build_secrets: typing.Optional[builtins.bool] = None,
    build_ssh: typing.Optional[builtins.bool] = None,
    extra_hash: typing.Optional[builtins.bool] = None,
    file: typing.Optional[builtins.bool] = None,
    network_mode: typing.Optional[builtins.bool] = None,
    outputs: typing.Optional[builtins.bool] = None,
    platform: typing.Optional[builtins.bool] = None,
    repository_name: typing.Optional[builtins.bool] = None,
    target: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be58b9ab6157641d31b553709d8decad6c9801460bec8e3ff07aadc336f83bff(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    extra_hash: typing.Optional[builtins.str] = None,
    asset_name: typing.Optional[builtins.str] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_ssh: typing.Optional[builtins.str] = None,
    cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
    cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[builtins.str] = None,
    invalidation: typing.Optional[typing.Union[DockerImageAssetInvalidationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    network_mode: typing.Optional[NetworkMode] = None,
    outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
    platform: typing.Optional[Platform] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1abde6bc94231492c7b40171b32143e7c5533e907120fe3e3c2ebeca225cefd9(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    extra_hash: typing.Optional[builtins.str] = None,
    asset_name: typing.Optional[builtins.str] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_ssh: typing.Optional[builtins.str] = None,
    cache_from: typing.Optional[typing.Sequence[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]]] = None,
    cache_to: typing.Optional[typing.Union[DockerCacheOption, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[builtins.str] = None,
    invalidation: typing.Optional[typing.Union[DockerImageAssetInvalidationOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    network_mode: typing.Optional[NetworkMode] = None,
    outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
    platform: typing.Optional[Platform] = None,
    target: typing.Optional[builtins.str] = None,
    directory: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f8d8c6403f901d8551692a871bf90e61484d2689a91a2d4657cfbb8fbc027ef(
    mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a508fd6d847e45dec0e540f453d59e2c2ff0115f17e6ce130b364d3bd85feb(
    container_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cca0d33972ff79dfe541d669145958c23cec6650e40df29cd7caec618b0cd7e(
    platform: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0eaaf11f2e3e296d6157cf12d477a55316a9aefb390c2f9de1711f911d5450(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    tarball_file: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5be1a7955548e99522c60499ad4723f8d659920228401ac7006d323cd4ee2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb91ed092745a33fafd3df8d94f545ae143be6b4949103c115bc71350c947bb(
    value: _IRepository_e6004aa6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1555ea2241a0a5236409111ebbad425ecc370ebc8987c4a7871719d32389658b(
    *,
    tarball_file: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
