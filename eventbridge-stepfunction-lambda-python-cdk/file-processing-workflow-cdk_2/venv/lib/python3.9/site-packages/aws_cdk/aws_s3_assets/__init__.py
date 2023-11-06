'''
# AWS CDK Assets

Assets are local files or directories which are needed by a CDK app. A common
example is a directory which contains the handler code for a Lambda function,
but assets can represent any artifact that is needed for the app's operation.

When deploying a CDK app that includes constructs with assets, the CDK toolkit
will first upload all the assets to S3, and only then deploy the stacks. The S3
locations of the uploaded assets will be passed in as CloudFormation Parameters
to the relevant stacks.

The following JavaScript example defines a directory asset which is archived as
a .zip file and uploaded to S3 during deployment.

```python
asset = assets.Asset(self, "SampleAsset",
    path=path.join(__dirname, "sample-asset-directory")
)
```

The following JavaScript example defines a file asset, which is uploaded as-is
to an S3 bucket during deployment.

```python
asset = assets.Asset(self, "SampleAsset",
    path=path.join(__dirname, "file-asset.txt")
)
```

## Attributes

`Asset` constructs expose the following deploy-time attributes:

* `s3BucketName` - the name of the assets S3 bucket.
* `s3ObjectKey` - the S3 object key of the asset file (whether it's a file or a zip archive)
* `s3ObjectUrl` - the S3 object URL of the asset (i.e. s3://mybucket/mykey.zip)
* `httpUrl` - the S3 HTTP URL of the asset (i.e. https://s3.us-east-1.amazonaws.com/mybucket/mykey.zip)

In the following example, the various asset attributes are exported as stack outputs:

```python
asset = assets.Asset(self, "SampleAsset",
    path=path.join(__dirname, "sample-asset-directory")
)

cdk.CfnOutput(self, "S3BucketName", value=asset.s3_bucket_name)
cdk.CfnOutput(self, "S3ObjectKey", value=asset.s3_object_key)
cdk.CfnOutput(self, "S3HttpURL", value=asset.http_url)
cdk.CfnOutput(self, "S3ObjectURL", value=asset.s3_object_url)
```

## Permissions

IAM roles, users or groups which need to be able to read assets in runtime will should be
granted IAM permissions. To do that use the `asset.grantRead(principal)` method:

The following example grants an IAM group read permissions on an asset:

```python
group = iam.Group(self, "MyUserGroup")
asset.grant_read(group)
```

## How does it work

When an asset is defined in a construct, a construct metadata entry
`aws:cdk:asset` is emitted with instructions on where to find the asset and what
type of packaging to perform (`zip` or `file`). Furthermore, the synthesized
CloudFormation template will also include two CloudFormation parameters: one for
the asset's bucket and one for the asset S3 key. Those parameters are used to
reference the deploy-time values of the asset (using `{ Ref: "Param" }`).

Then, when the stack is deployed, the toolkit will package the asset (i.e. zip
the directory), calculate an MD5 hash of the contents and will render an S3 key
for this asset within the toolkit's asset store. If the file doesn't exist in
the asset store, it is uploaded during deployment.

> The toolkit's asset store is an S3 bucket created by the toolkit for each
> environment the toolkit operates in (environment = account + region).

Now, when the toolkit deploys the stack, it will set the relevant CloudFormation
Parameters to point to the actual bucket and key for each asset.

## Asset Bundling

When defining an asset, you can use the `bundling` option to specify a command
to run inside a docker container. The command can read the contents of the asset
source from `/asset-input` and is expected to write files under `/asset-output`
(directories mapped inside the container). The files under `/asset-output` will
be zipped and uploaded to S3 as the asset.

The following example uses custom asset bundling to convert a markdown file to html:

```python
asset = assets.Asset(self, "BundledAsset",
    path=path.join(__dirname, "markdown-asset"),  # /asset-input and working directory in the container
    bundling=assets.BundlingOptions(
        image=DockerImage.from_build(path.join(__dirname, "alpine-markdown")),  # Build an image
        command=["sh", "-c", """
                        markdown index.md > /asset-output/index.html
                      """
        ]
    )
)
```

The bundling docker image (`image`) can either come from a registry (`DockerImage.fromRegistry`)
or it can be built from a `Dockerfile` located inside your project (`DockerImage.fromBuild`).

You can set the `CDK_DOCKER` environment variable in order to provide a custom
docker program to execute. This may sometime be needed when building in
environments where the standard docker cannot be executed (see
https://github.com/aws/aws-cdk/issues/8460 for details).

Use `local` to specify a local bundling provider. The provider implements a
method `tryBundle()` which should return `true` if local bundling was performed.
If `false` is returned, docker bundling will be done:

```python
import aws_cdk as cdk


@jsii.implements(cdk.ILocalBundling)
class MyBundle:
    def try_bundle(self, output_dir, *, image, entrypoint=None, command=None, volumes=None, volumesFrom=None, environment=None, workingDirectory=None, user=None, local=None, outputType=None, securityOpt=None, network=None, bundlingFileAccess=None, platform=None):
        can_run_locally = True # replace with actual logic
        if can_run_locally:
            # perform local bundling here
            return True
        return False

Asset(self, "BundledAsset",
    path="/path/to/asset",
    bundling=cdk.BundlingOptions(
        local=MyBundle(),
        # Docker bundling fallback
        image=cdk.DockerImage.from_registry("alpine"),
        entrypoint=["/bin/sh", "-c"],
        command=["bundle"]
    )
)
```

Although optional, it's recommended to provide a local bundling method which can
greatly improve performance.

If the bundling output contains a single archive file (zip or jar) it will be
uploaded to S3 as-is and will not be zipped. Otherwise the contents of the
output directory will be zipped and the zip file will be uploaded to S3. This
is the default behavior for `bundling.outputType` (`BundlingOutput.AUTO_DISCOVER`).

Use `BundlingOutput.NOT_ARCHIVED` if the bundling output must always be zipped:

```python
import aws_cdk as cdk


asset = Asset(self, "BundledAsset",
    path="/path/to/asset",
    bundling=cdk.BundlingOptions(
        image=cdk.DockerImage.from_registry("alpine"),
        command=["command-that-produces-an-archive.sh"],
        output_type=cdk.BundlingOutput.NOT_ARCHIVED
    )
)
```

Use `BundlingOutput.ARCHIVED` if the bundling output contains a single archive file and
you don't want it to be zipped.

### Docker options

Depending on your build environment, you may need to pass certain docker options to the `docker run` command that bundles assets.
This can be done using [BundlingOptions](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.BundlingOptions.html) properties.

Some optional properties to pass to the docker bundling

```python
import aws_cdk.aws_lambda as lambda_


asset = Asset(self, "BundledAsset",
    path="/path/to/asset",
    bundling=BundlingOptions(
        image=lambda_.Runtime.PYTHON_3_9.bundling_image,
        command=["bash", "-c", "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
        ],
        security_opt="no-new-privileges:true",  # https://docs.docker.com/engine/reference/commandline/run/#optional-security-options---security-opt
        network="host"
    )
)
```

## CloudFormation Resource Metadata

> NOTE: This section is relevant for authors of AWS Resource Constructs.

In certain situations, it is desirable for tools to be able to know that a certain CloudFormation
resource is using a local asset. For example, SAM CLI can be used to invoke AWS Lambda functions
locally for debugging purposes.

To enable such use cases, external tools will consult a set of metadata entries on AWS CloudFormation
resources:

* `aws:asset:path` points to the local path of the asset.
* `aws:asset:property` is the name of the resource property where the asset is used

Using these two metadata entries, tools will be able to identify that assets are used
by a certain resource, and enable advanced local experiences.

To add these metadata entries to a resource, use the
`asset.addResourceMetadata(resource, property)` method.

See https://github.com/aws/aws-cdk/issues/1432 for more details
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
    AssetHashType as _AssetHashType_05b67f2d,
    AssetOptions as _AssetOptions_9cd3031e,
    BundlingOptions as _BundlingOptions_588cc936,
    CfnResource as _CfnResource_9df397a6,
    FileCopyOptions as _FileCopyOptions_e03e2a30,
    IAsset as _IAsset_03c624d8,
    IgnoreMode as _IgnoreMode_655a98e8,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
)
from ..aws_iam import IGrantable as _IGrantable_71c4f5de
from ..aws_s3 import IBucket as _IBucket_42e086fd


@jsii.implements(_IAsset_03c624d8)
class Asset(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_assets.Asset",
):
    '''An asset represents a local file or directory, which is automatically uploaded to S3 and then can be referenced within a CDK application.

    :exampleMetadata: infused

    Example::

        import aws_cdk as cdk
        
        
        asset = Asset(self, "BundledAsset",
            path="/path/to/asset",
            bundling=cdk.BundlingOptions(
                image=cdk.DockerImage.from_registry("alpine"),
                command=["command-that-produces-an-archive.sh"],
                output_type=cdk.BundlingOutput.NOT_ARCHIVED
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        path: builtins.str,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param path: The disk location of the asset. The path should refer to one of the following: - A regular file or a .zip file, in which case the file will be uploaded as-is to S3. - A directory, in which case it will be archived into a .zip file and uploaded to S3.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00df81fd3b746cf2ee52c0e7a23b6fdc1b45db97673ca7e25a9651e7e2a4976b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AssetProps(
            path=path,
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
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
        :param resource_property: The property name where this asset is referenced (e.g. "Code" for AWS::Lambda::Function).

        :see: https://github.com/aws/aws-cdk/issues/1432
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61a6eb6ec5bb9c8f9b7933979f88a1fc68820ccc4cc76a663b24d3c48e7d036)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument resource_property", value=resource_property, expected_type=type_hints["resource_property"])
        return typing.cast(None, jsii.invoke(self, "addResourceMetadata", [resource, resource_property]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> None:
        '''Grants read permissions to the principal on the assets bucket.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6425d5070c191fc82b7882c0028ef6e8289f1fb411fbbc4209d20b31eddc229)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(None, jsii.invoke(self, "grantRead", [grantee]))

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
    @jsii.member(jsii_name="assetPath")
    def asset_path(self) -> builtins.str:
        '''The path to the asset, relative to the current Cloud Assembly.

        If asset staging is disabled, this will just be the original path.
        If asset staging is enabled it will be the staged path.
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetPath"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''The S3 bucket in which this asset resides.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="httpUrl")
    def http_url(self) -> builtins.str:
        '''Attribute which represents the S3 HTTP URL of this asset.

        For example, ``https://s3.us-west-1.amazonaws.com/bucket/key``
        '''
        return typing.cast(builtins.str, jsii.get(self, "httpUrl"))

    @builtins.property
    @jsii.member(jsii_name="isFile")
    def is_file(self) -> builtins.bool:
        '''Indicates if this asset is a single file.

        Allows constructs to ensure that the
        correct file type was used.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isFile"))

    @builtins.property
    @jsii.member(jsii_name="isZipArchive")
    def is_zip_archive(self) -> builtins.bool:
        '''Indicates if this asset is a zip archive.

        Allows constructs to ensure that the
        correct file type was used.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isZipArchive"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        '''Attribute that represents the name of the bucket this asset exists in.'''
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @builtins.property
    @jsii.member(jsii_name="s3ObjectKey")
    def s3_object_key(self) -> builtins.str:
        '''Attribute which represents the S3 object key of this asset.'''
        return typing.cast(builtins.str, jsii.get(self, "s3ObjectKey"))

    @builtins.property
    @jsii.member(jsii_name="s3ObjectUrl")
    def s3_object_url(self) -> builtins.str:
        '''Attribute which represents the S3 URL of this asset.

        For example, ``s3://bucket/key``
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3ObjectUrl"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_assets.AssetOptions",
    jsii_struct_bases=[_AssetOptions_9cd3031e, _FileCopyOptions_e03e2a30],
    name_mapping={
        "asset_hash": "assetHash",
        "asset_hash_type": "assetHashType",
        "bundling": "bundling",
        "exclude": "exclude",
        "follow_symlinks": "followSymlinks",
        "ignore_mode": "ignoreMode",
        "deploy_time": "deployTime",
        "readers": "readers",
    },
)
class AssetOptions(_AssetOptions_9cd3031e, _FileCopyOptions_e03e2a30):
    def __init__(
        self,
        *,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    ) -> None:
        '''
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.

        :exampleMetadata: infused

        Example::

            lambda_.Function(self, "Function",
                code=lambda_.Code.from_asset(path.join(__dirname, "my-python-handler"),
                    bundling=BundlingOptions(
                        image=lambda_.Runtime.PYTHON_3_9.bundling_image,
                        command=["bash", "-c", "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
                        ]
                    )
                ),
                runtime=lambda_.Runtime.PYTHON_3_9,
                handler="index.handler"
            )
        '''
        if isinstance(bundling, dict):
            bundling = _BundlingOptions_588cc936(**bundling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11950fe0327642dd25ddfeb2c620bb33847718475fe489bf003d096a07e81b69)
            check_type(argname="argument asset_hash", value=asset_hash, expected_type=type_hints["asset_hash"])
            check_type(argname="argument asset_hash_type", value=asset_hash_type, expected_type=type_hints["asset_hash_type"])
            check_type(argname="argument bundling", value=bundling, expected_type=type_hints["bundling"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument follow_symlinks", value=follow_symlinks, expected_type=type_hints["follow_symlinks"])
            check_type(argname="argument ignore_mode", value=ignore_mode, expected_type=type_hints["ignore_mode"])
            check_type(argname="argument deploy_time", value=deploy_time, expected_type=type_hints["deploy_time"])
            check_type(argname="argument readers", value=readers, expected_type=type_hints["readers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if asset_hash_type is not None:
            self._values["asset_hash_type"] = asset_hash_type
        if bundling is not None:
            self._values["bundling"] = bundling
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow_symlinks is not None:
            self._values["follow_symlinks"] = follow_symlinks
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if deploy_time is not None:
            self._values["deploy_time"] = deploy_time
        if readers is not None:
            self._values["readers"] = readers

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        If ``assetHashType`` is set it must
        be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - based on ``assetHashType``
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash_type(self) -> typing.Optional[_AssetHashType_05b67f2d]:
        '''Specifies the type of hash to calculate for this asset.

        If ``assetHash`` is configured, this option must be ``undefined`` or
        ``AssetHashType.CUSTOM``.

        :default:

        - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is
        explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        '''
        result = self._values.get("asset_hash_type")
        return typing.cast(typing.Optional[_AssetHashType_05b67f2d], result)

    @builtins.property
    def bundling(self) -> typing.Optional[_BundlingOptions_588cc936]:
        '''Bundle the asset by executing a command in a Docker container or a custom bundling provider.

        The asset path will be mounted at ``/asset-input``. The Docker
        container is responsible for putting content at ``/asset-output``.
        The content at ``/asset-output`` will be zipped and used as the
        final asset.

        :default:

        - uploaded as-is to S3 if the asset is a regular file or a .zip file,
        archived into a .zip file and uploaded to S3 otherwise
        '''
        result = self._values.get("bundling")
        return typing.cast(typing.Optional[_BundlingOptions_588cc936], result)

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
    def deploy_time(self) -> typing.Optional[builtins.bool]:
        '''Whether or not the asset needs to exist beyond deployment time;

        i.e.
        are copied over to a different location and not needed afterwards.
        Setting this property to true has an impact on the lifecycle of the asset,
        because we will assume that it is safe to delete after the CloudFormation
        deployment succeeds.

        For example, Lambda Function assets are copied over to Lambda during
        deployment. Therefore, it is not necessary to store the asset in S3, so
        we consider those deployTime assets.

        :default: false
        '''
        result = self._values.get("deploy_time")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readers(self) -> typing.Optional[typing.List[_IGrantable_71c4f5de]]:
        '''A list of principals that should be able to read this asset from S3.

        You can use ``asset.grantRead(principal)`` to grant read permissions later.

        :default: - No principals that can read file asset.
        '''
        result = self._values.get("readers")
        return typing.cast(typing.Optional[typing.List[_IGrantable_71c4f5de]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_assets.AssetProps",
    jsii_struct_bases=[AssetOptions],
    name_mapping={
        "asset_hash": "assetHash",
        "asset_hash_type": "assetHashType",
        "bundling": "bundling",
        "exclude": "exclude",
        "follow_symlinks": "followSymlinks",
        "ignore_mode": "ignoreMode",
        "deploy_time": "deployTime",
        "readers": "readers",
        "path": "path",
    },
)
class AssetProps(AssetOptions):
    def __init__(
        self,
        *,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        path: builtins.str,
    ) -> None:
        '''
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param path: The disk location of the asset. The path should refer to one of the following: - A regular file or a .zip file, in which case the file will be uploaded as-is to S3. - A directory, in which case it will be archived into a .zip file and uploaded to S3.

        :exampleMetadata: infused

        Example::

            import aws_cdk as cdk
            
            
            asset = Asset(self, "BundledAsset",
                path="/path/to/asset",
                bundling=cdk.BundlingOptions(
                    image=cdk.DockerImage.from_registry("alpine"),
                    command=["command-that-produces-an-archive.sh"],
                    output_type=cdk.BundlingOutput.NOT_ARCHIVED
                )
            )
        '''
        if isinstance(bundling, dict):
            bundling = _BundlingOptions_588cc936(**bundling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f879318d3885bc2e9c71c124fac7ad5a955812e438be7c03244c3aad7bda9fbe)
            check_type(argname="argument asset_hash", value=asset_hash, expected_type=type_hints["asset_hash"])
            check_type(argname="argument asset_hash_type", value=asset_hash_type, expected_type=type_hints["asset_hash_type"])
            check_type(argname="argument bundling", value=bundling, expected_type=type_hints["bundling"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument follow_symlinks", value=follow_symlinks, expected_type=type_hints["follow_symlinks"])
            check_type(argname="argument ignore_mode", value=ignore_mode, expected_type=type_hints["ignore_mode"])
            check_type(argname="argument deploy_time", value=deploy_time, expected_type=type_hints["deploy_time"])
            check_type(argname="argument readers", value=readers, expected_type=type_hints["readers"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if asset_hash_type is not None:
            self._values["asset_hash_type"] = asset_hash_type
        if bundling is not None:
            self._values["bundling"] = bundling
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow_symlinks is not None:
            self._values["follow_symlinks"] = follow_symlinks
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if deploy_time is not None:
            self._values["deploy_time"] = deploy_time
        if readers is not None:
            self._values["readers"] = readers

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        If ``assetHashType`` is set it must
        be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - based on ``assetHashType``
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash_type(self) -> typing.Optional[_AssetHashType_05b67f2d]:
        '''Specifies the type of hash to calculate for this asset.

        If ``assetHash`` is configured, this option must be ``undefined`` or
        ``AssetHashType.CUSTOM``.

        :default:

        - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is
        explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        '''
        result = self._values.get("asset_hash_type")
        return typing.cast(typing.Optional[_AssetHashType_05b67f2d], result)

    @builtins.property
    def bundling(self) -> typing.Optional[_BundlingOptions_588cc936]:
        '''Bundle the asset by executing a command in a Docker container or a custom bundling provider.

        The asset path will be mounted at ``/asset-input``. The Docker
        container is responsible for putting content at ``/asset-output``.
        The content at ``/asset-output`` will be zipped and used as the
        final asset.

        :default:

        - uploaded as-is to S3 if the asset is a regular file or a .zip file,
        archived into a .zip file and uploaded to S3 otherwise
        '''
        result = self._values.get("bundling")
        return typing.cast(typing.Optional[_BundlingOptions_588cc936], result)

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
    def deploy_time(self) -> typing.Optional[builtins.bool]:
        '''Whether or not the asset needs to exist beyond deployment time;

        i.e.
        are copied over to a different location and not needed afterwards.
        Setting this property to true has an impact on the lifecycle of the asset,
        because we will assume that it is safe to delete after the CloudFormation
        deployment succeeds.

        For example, Lambda Function assets are copied over to Lambda during
        deployment. Therefore, it is not necessary to store the asset in S3, so
        we consider those deployTime assets.

        :default: false
        '''
        result = self._values.get("deploy_time")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readers(self) -> typing.Optional[typing.List[_IGrantable_71c4f5de]]:
        '''A list of principals that should be able to read this asset from S3.

        You can use ``asset.grantRead(principal)`` to grant read permissions later.

        :default: - No principals that can read file asset.
        '''
        result = self._values.get("readers")
        return typing.cast(typing.Optional[typing.List[_IGrantable_71c4f5de]], result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The disk location of the asset.

        The path should refer to one of the following:

        - A regular file or a .zip file, in which case the file will be uploaded as-is to S3.
        - A directory, in which case it will be archived into a .zip file and uploaded to S3.
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Asset",
    "AssetOptions",
    "AssetProps",
]

publication.publish()

def _typecheckingstub__00df81fd3b746cf2ee52c0e7a23b6fdc1b45db97673ca7e25a9651e7e2a4976b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    path: builtins.str,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f61a6eb6ec5bb9c8f9b7933979f88a1fc68820ccc4cc76a663b24d3c48e7d036(
    resource: _CfnResource_9df397a6,
    resource_property: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6425d5070c191fc82b7882c0028ef6e8289f1fb411fbbc4209d20b31eddc229(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11950fe0327642dd25ddfeb2c620bb33847718475fe489bf003d096a07e81b69(
    *,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f879318d3885bc2e9c71c124fac7ad5a955812e438be7c03244c3aad7bda9fbe(
    *,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
