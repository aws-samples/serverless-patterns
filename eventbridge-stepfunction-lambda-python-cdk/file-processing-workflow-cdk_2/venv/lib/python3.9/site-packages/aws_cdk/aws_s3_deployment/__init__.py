'''
# AWS S3 Deployment Construct Library

This library allows populating an S3 bucket with the contents of .zip files
from other S3 buckets or from local disk.

The following example defines a publicly accessible S3 bucket with web hosting
enabled and populates it from a local directory on disk.

```python
website_bucket = s3.Bucket(self, "WebsiteBucket",
    website_index_document="index.html",
    public_read_access=True
)

s3deploy.BucketDeployment(self, "DeployWebsite",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=website_bucket,
    destination_key_prefix="web/static"
)
```

This is what happens under the hood:

1. When this stack is deployed (either via `cdk deploy` or via CI/CD), the
   contents of the local `website-dist` directory will be archived and uploaded
   to an intermediary assets bucket. If there is more than one source, they will
   be individually uploaded.
2. The `BucketDeployment` construct synthesizes a custom CloudFormation resource
   of type `Custom::CDKBucketDeployment` into the template. The source bucket/key
   is set to point to the assets bucket.
3. The custom resource downloads the .zip archive, extracts it and issues `aws s3 sync --delete` against the destination bucket (in this case
   `websiteBucket`). If there is more than one source, the sources will be
   downloaded and merged pre-deployment at this step.

If you are referencing the filled bucket in another construct that depends on
the files already be there, be sure to use `deployment.deployedBucket`. This
will ensure the bucket deployment has finished before the resource that uses
the bucket is created:

```python
# website_bucket: s3.Bucket


deployment = s3deploy.BucketDeployment(self, "DeployWebsite",
    sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
    destination_bucket=website_bucket
)

ConstructThatReadsFromTheBucket(self, "Consumer", {
    # Use 'deployment.deployedBucket' instead of 'websiteBucket' here
    "bucket": deployment.deployed_bucket
})
```

It is also possible to add additional sources using the `addSource` method.

```python
# website_bucket: s3.IBucket


deployment = s3deploy.BucketDeployment(self, "DeployWebsite",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=website_bucket,
    destination_key_prefix="web/static"
)

deployment.add_source(s3deploy.Source.asset("./another-asset"))
```

## Supported sources

The following source types are supported for bucket deployments:

* Local .zip file: `s3deploy.Source.asset('/path/to/local/file.zip')`
* Local directory: `s3deploy.Source.asset('/path/to/local/directory')`
* Another bucket: `s3deploy.Source.bucket(bucket, zipObjectKey)`
* String data: `s3deploy.Source.data('object-key.txt', 'hello, world!')`
  (supports [deploy-time values](#data-with-deploy-time-values))
* JSON data: `s3deploy.Source.jsonData('object-key.json', { json: 'object' })`
  (supports [deploy-time values](#data-with-deploy-time-values))
* YAML data: `s3deploy.Source.yamlData('object-key.yaml', { yaml: 'object' })`
  (supports [deploy-time values](#data-with-deploy-time-values))

To create a source from a single file, you can pass `AssetOptions` to exclude
all but a single file:

* Single file: `s3deploy.Source.asset('/path/to/local/directory', { exclude: ['**', '!onlyThisFile.txt'] })`

**IMPORTANT** The `aws-s3-deployment` module is only intended to be used with
zip files from trusted sources. Directories bundled by the CDK CLI (by using
`Source.asset()` on a directory) are safe. If you are using `Source.asset()` or
`Source.bucket()` to reference an existing zip file, make sure you trust the
file you are referencing. Zips from untrusted sources might be able to execute
arbitrary code in the Lambda Function used by this module, and use its permissions
to read or write unexpected files in the S3 bucket.

## Retain on Delete

By default, the contents of the destination bucket will **not** be deleted when the
`BucketDeployment` resource is removed from the stack or when the destination is
changed. You can use the option `retainOnDelete: false` to disable this behavior,
in which case the contents will be deleted.

Configuring this has a few implications you should be aware of:

* **Logical ID Changes**

  Changing the logical ID of the `BucketDeployment` construct, without changing the destination
  (for example due to refactoring, or intentional ID change) **will result in the deletion of the objects**.
  This is because CloudFormation will first create the new resource, which will have no affect,
  followed by a deletion of the old resource, which will cause a deletion of the objects,
  since the destination hasn't changed, and `retainOnDelete` is `false`.
* **Destination Changes**

  When the destination bucket or prefix is changed, all files in the previous destination will **first** be
  deleted and then uploaded to the new destination location. This could have availability implications
  on your users.

### General Recommendations

#### Shared Bucket

If the destination bucket **is not** dedicated to the specific `BucketDeployment` construct (i.e shared by other entities),
we recommend to always configure the `destinationKeyPrefix` property. This will prevent the deployment from
accidentally deleting data that wasn't uploaded by it.

#### Dedicated Bucket

If the destination bucket **is** dedicated, it might be reasonable to skip the prefix configuration,
in which case, we recommend to remove `retainOnDelete: false`, and instead, configure the
[`autoDeleteObjects`](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3-readme.html#bucket-deletion)
property on the destination bucket. This will avoid the logical ID problem mentioned above.

## Prune

By default, files in the destination bucket that don't exist in the source will be deleted
when the `BucketDeployment` resource is created or updated. You can use the option `prune: false` to disable
this behavior, in which case the files will not be deleted.

```python
# destination_bucket: s3.Bucket

s3deploy.BucketDeployment(self, "DeployMeWithoutDeletingFilesOnDestination",
    sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
    destination_bucket=destination_bucket,
    prune=False
)
```

This option also enables you to
multiple bucket deployments for the same destination bucket & prefix,
each with its own characteristics. For example, you can set different cache-control headers
based on file extensions:

```python
# destination_bucket: s3.Bucket

s3deploy.BucketDeployment(self, "BucketDeployment",
    sources=[s3deploy.Source.asset("./website", exclude=["index.html"])],
    destination_bucket=destination_bucket,
    cache_control=[
        s3deploy.CacheControl.max_age(Duration.days(365)),
        s3deploy.CacheControl.immutable()
    ],
    prune=False
)

s3deploy.BucketDeployment(self, "HTMLBucketDeployment",
    sources=[s3deploy.Source.asset("./website", exclude=["*", "!index.html"])],
    destination_bucket=destination_bucket,
    cache_control=[
        s3deploy.CacheControl.max_age(Duration.seconds(0))
    ],
    prune=False
)
```

## Exclude and Include Filters

There are two points at which filters are evaluated in a deployment: asset bundling and the actual deployment. If you simply want to exclude files in the asset bundling process, you should leverage the `exclude` property of `AssetOptions` when defining your source:

```python
# destination_bucket: s3.Bucket

s3deploy.BucketDeployment(self, "HTMLBucketDeployment",
    sources=[s3deploy.Source.asset("./website", exclude=["*", "!index.html"])],
    destination_bucket=destination_bucket
)
```

If you want to specify filters to be used in the deployment process, you can use the `exclude` and `include` filters on `BucketDeployment`.  If excluded, these files will not be deployed to the destination bucket. In addition, if the file already exists in the destination bucket, it will not be deleted if you are using the `prune` option:

```python
# destination_bucket: s3.Bucket

s3deploy.BucketDeployment(self, "DeployButExcludeSpecificFiles",
    sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
    destination_bucket=destination_bucket,
    exclude=["*.txt"]
)
```

These filters follow the same format that is used for the AWS CLI.  See the CLI documentation for information on [Using Include and Exclude Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters).

## Objects metadata

You can specify metadata to be set on all the objects in your deployment.
There are 2 types of metadata in S3: system-defined metadata and user-defined metadata.
System-defined metadata have a special purpose, for example cache-control defines how long to keep an object cached.
User-defined metadata are not used by S3 and keys always begin with `x-amz-meta-` (this prefix is added automatically).

System defined metadata keys include the following:

* cache-control (`--cache-control` in `aws s3 sync`)
* content-disposition (`--content-disposition` in `aws s3 sync`)
* content-encoding (`--content-encoding` in `aws s3 sync`)
* content-language (`--content-language` in `aws s3 sync`)
* content-type (`--content-type` in `aws s3 sync`)
* expires (`--expires` in `aws s3 sync`)
* x-amz-storage-class (`--storage-class` in `aws s3 sync`)
* x-amz-website-redirect-location (`--website-redirect` in `aws s3 sync`)
* x-amz-server-side-encryption (`--sse` in `aws s3 sync`)
* x-amz-server-side-encryption-aws-kms-key-id (`--sse-kms-key-id` in `aws s3 sync`)
* x-amz-server-side-encryption-customer-algorithm (`--sse-c-copy-source` in `aws s3 sync`)
* x-amz-acl (`--acl` in `aws s3 sync`)

You can find more information about system defined metadata keys in
[S3 PutObject documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
and [`aws s3 sync` documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html).

```python
website_bucket = s3.Bucket(self, "WebsiteBucket",
    website_index_document="index.html",
    public_read_access=True
)

s3deploy.BucketDeployment(self, "DeployWebsite",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=website_bucket,
    destination_key_prefix="web/static",  # optional prefix in destination bucket
    metadata={"A": "1", "b": "2"},  # user-defined metadata

    # system-defined metadata
    content_type="text/html",
    content_language="en",
    storage_class=s3deploy.StorageClass.INTELLIGENT_TIERING,
    server_side_encryption=s3deploy.ServerSideEncryption.AES_256,
    cache_control=[
        s3deploy.CacheControl.set_public(),
        s3deploy.CacheControl.max_age(Duration.hours(1))
    ],
    access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL
)
```

## CloudFront Invalidation

You can provide a CloudFront distribution and optional paths to invalidate after the bucket deployment finishes.

```python
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as origins


bucket = s3.Bucket(self, "Destination")

# Handles buckets whether or not they are configured for website hosting.
distribution = cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(bucket))
)

s3deploy.BucketDeployment(self, "DeployWithInvalidation",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=bucket,
    distribution=distribution,
    distribution_paths=["/images/*.png"]
)
```

## Signed Content Payloads

By default, deployment uses streaming uploads which set the `x-amz-content-sha256`
request header to `UNSIGNED-PAYLOAD` (matching default behavior of the AWS CLI tool).
In cases where bucket policy restrictions require signed content payloads, you can enable
generation of a signed `x-amz-content-sha256` request header with `signContent: true`.

```python
# bucket: s3.IBucket


s3deploy.BucketDeployment(self, "DeployWithSignedPayloads",
    sources=[s3deploy.Source.asset("./website-dist")],
    destination_bucket=bucket,
    sign_content=True
)
```

## Size Limits

The default memory limit for the deployment resource is 128MiB. If you need to
copy larger files, you can use the `memoryLimit` configuration to increase the
size of the AWS Lambda resource handler.

The default ephemeral storage size for the deployment resource is 512MiB. If you
need to upload larger files, you may hit this limit. You can use the
`ephemeralStorageSize` configuration to increase the storage size of the AWS Lambda
resource handler.

> NOTE: a new AWS Lambda handler will be created in your stack for each combination
> of memory and storage size.

## EFS Support

If your workflow needs more disk space than default (512 MB) disk space, you may attach an EFS storage to underlying
lambda function. To Enable EFS support set `efs` and `vpc` props for BucketDeployment.

Check sample usage below.
Please note that creating VPC inline may cause stack deletion failures. It is shown as below for simplicity.
To avoid such condition, keep your network infra (VPC) in a separate stack and pass as props.

```python
# destination_bucket: s3.Bucket
# vpc: ec2.Vpc


s3deploy.BucketDeployment(self, "DeployMeWithEfsStorage",
    sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
    destination_bucket=destination_bucket,
    destination_key_prefix="efs/",
    use_efs=True,
    vpc=vpc,
    retain_on_delete=False
)
```

## Data with deploy-time values

The content passed to `Source.data()`, `Source.jsonData()`, or `Source.yamlData()` can include
references that will get resolved only during deployment.

For example:

```python
import aws_cdk.aws_sns as sns

# destination_bucket: s3.Bucket
# topic: sns.Topic


app_config = {
    "topic_arn": topic.topic_arn,
    "base_url": "https://my-endpoint"
}

s3deploy.BucketDeployment(self, "BucketDeployment",
    sources=[s3deploy.Source.json_data("config.json", app_config)],
    destination_bucket=destination_bucket
)
```

The value in `topic.topicArn` is a deploy-time value. It only gets resolved
during deployment by placing a marker in the generated source file and
substituting it when its deployed to the destination with the actual value.

### Substitutions from Templated Files

The `DeployTimeSubstitutedFile` construct allows you to specify substitutions
to make from placeholders in a local file which will be resolved during deployment. This
is especially useful in situations like creating an API from a spec file, where users might
want to reference other CDK resources they have created.

The syntax for template variables is `{{ variableName }}` in your local file. Then, you would
specify the substitutions in CDK like this:

```python
import aws_cdk.aws_lambda as lambda_

# my_lambda_function: lambda.Function
# destination_bucket: s3.Bucket


s3deploy.DeployTimeSubstitutedFile(self, "MyFile",
    source="my-file.yaml",
    destination_bucket=destination_bucket,
    substitutions={
        "variable_name": my_lambda_function.function_name
    }
)
```

Nested variables, like `{{ {{ foo }} }}` or `{{ foo {{ bar }} }}`, are not supported by this
construct. In the first case of a single variable being is double nested `{{ {{ foo }} }}`, only
the `{{ foo }}` would be replaced by the substitution, and the extra brackets would remain in the file.
In the second case of two nexted variables `{{ foo {{ bar }} }}`, only the `{{ bar }}` would be replaced
in the file.

## Keep Files Zipped

By default, files are zipped, then extracted into the destination bucket.

You can use the option `extract: false` to disable this behavior, in which case, files will remain in a zip file when deployed to S3. To reference the object keys, or filenames, which will be deployed to the bucket, you can use the `objectKeys` getter on the bucket deployment.

```python
import aws_cdk as cdk

# destination_bucket: s3.Bucket


my_bucket_deployment = s3deploy.BucketDeployment(self, "DeployMeWithoutExtractingFilesOnDestination",
    sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
    destination_bucket=destination_bucket,
    extract=False
)

cdk.CfnOutput(self, "ObjectKey",
    value=cdk.Fn.select(0, my_bucket_deployment.object_keys)
)
```

## Notes

* This library uses an AWS CloudFormation custom resource which is about 10MiB in
  size. The code of this resource is bundled with this library.
* AWS Lambda execution time is limited to 15min. This limits the amount of data
  which can be deployed into the bucket by this timeout.
* When the `BucketDeployment` is removed from the stack, the contents are retained
  in the destination bucket ([#952](https://github.com/aws/aws-cdk/issues/952)).
* If you are using `s3deploy.Source.bucket()` to take the file source from
  another bucket: the deployed files will only be updated if the key (file name)
  of the file in the source  bucket changes. Mutating the file in place will not
  be good enough: the custom resource will simply not run if the properties don't
  change.

  * If you use assets (`s3deploy.Source.asset()`) you don't need to worry
    about this: the asset system will make sure that if the files have changed,
    the file name is unique and the deployment will run.

## Development

The custom resource is implemented in Python 3.9 in order to be able to leverage
the AWS CLI for "aws s3 sync". The code is under [`lib/lambda`](https://github.com/aws/aws-cdk/tree/main/packages/aws-cdk-lib/aws-s3-deployment/lib/lambda) and
unit tests are under [`test/lambda`](https://github.com/aws/aws-cdk/tree/main/packages/aws-cdk-lib/aws-s3-deployment/test/lambda).

This package requires Python 3.9 during build time in order to create the custom
resource Lambda bundle and test it. It also relies on a few bash scripts, so
might be tricky to build on Windows.

## Roadmap

* [ ] Support "blue/green" deployments ([#954](https://github.com/aws/aws-cdk/issues/954))
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
    BundlingOptions as _BundlingOptions_588cc936,
    Duration as _Duration_4839e8c3,
    Expiration as _Expiration_059d47d0,
    IgnoreMode as _IgnoreMode_655a98e8,
    Size as _Size_7b441c34,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
)
from ..aws_cloudfront import IDistribution as _IDistribution_7ac752a4
from ..aws_ec2 import (
    IVpc as _IVpc_f30d5663, SubnetSelection as _SubnetSelection_e57d76df
)
from ..aws_iam import IGrantable as _IGrantable_71c4f5de, IRole as _IRole_235f5d8e
from ..aws_logs import RetentionDays as _RetentionDays_070f99f0
from ..aws_s3 import (
    BucketAccessControl as _BucketAccessControl_466c7e1b, IBucket as _IBucket_42e086fd
)
from ..aws_s3_assets import AssetOptions as _AssetOptions_2aa69621


class BucketDeployment(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_deployment.BucketDeployment",
):
    '''``BucketDeployment`` populates an S3 bucket with the contents of .zip files from other S3 buckets or from local disk.

    :exampleMetadata: infused

    Example::

        # website_bucket: s3.Bucket
        
        
        deployment = s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
            destination_bucket=website_bucket
        )
        
        ConstructThatReadsFromTheBucket(self, "Consumer", {
            # Use 'deployment.deployedBucket' instead of 'websiteBucket' here
            "bucket": deployment.deployed_bucket
        })
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_bucket: _IBucket_42e086fd,
        sources: typing.Sequence["ISource"],
        access_control: typing.Optional[_BucketAccessControl_466c7e1b] = None,
        cache_control: typing.Optional[typing.Sequence["CacheControl"]] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        destination_key_prefix: typing.Optional[builtins.str] = None,
        distribution: typing.Optional[_IDistribution_7ac752a4] = None,
        distribution_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        expires: typing.Optional[_Expiration_059d47d0] = None,
        extract: typing.Optional[builtins.bool] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        prune: typing.Optional[builtins.bool] = None,
        retain_on_delete: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        server_side_encryption: typing.Optional["ServerSideEncryption"] = None,
        server_side_encryption_aws_kms_key_id: typing.Optional[builtins.str] = None,
        server_side_encryption_customer_algorithm: typing.Optional[builtins.str] = None,
        sign_content: typing.Optional[builtins.bool] = None,
        storage_class: typing.Optional["StorageClass"] = None,
        use_efs: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        website_redirect_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param destination_bucket: The S3 bucket to sync the contents of the zip file to.
        :param sources: The sources from which to deploy the contents of this bucket.
        :param access_control: System-defined x-amz-acl metadata to be set on all objects in the deployment. Default: - Not set.
        :param cache_control: System-defined cache-control metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_disposition: System-defined cache-disposition metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_encoding: System-defined content-encoding metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_language: System-defined content-language metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_type: System-defined content-type metadata to be set on all objects in the deployment. Default: - Not set.
        :param destination_key_prefix: Key prefix in the destination bucket. Must be <=104 characters Default: "/" (unzip to root of the destination bucket)
        :param distribution: The CloudFront distribution using the destination bucket as an origin. Files in the distribution's edge caches will be invalidated after files are uploaded to the destination bucket. Default: - No invalidation occurs
        :param distribution_paths: The file paths to invalidate in the CloudFront distribution. Default: - All files under the destination bucket key prefix will be invalidated.
        :param ephemeral_storage_size: The size of the AWS Lambda function’s /tmp directory in MiB. Default: 512 MiB
        :param exclude: If this is set, matching files or objects will be excluded from the deployment's sync command. This can be used to exclude a file from being pruned in the destination bucket. If you want to just exclude files from the deployment package (which excludes these files evaluated when invalidating the asset), you should leverage the ``exclude`` property of ``AssetOptions`` when defining your source. Default: - No exclude filters are used
        :param expires: System-defined expires metadata to be set on all objects in the deployment. Default: - The objects in the distribution will not expire.
        :param extract: If this is set, the zip file will be synced to the destination S3 bucket and extracted. If false, the file will remain zipped in the destination bucket. Default: true
        :param include: If this is set, matching files or objects will be included with the deployment's sync command. Since all files from the deployment package are included by default, this property is usually leveraged alongside an ``exclude`` filter. Default: - No include filters are used and all files are included with the sync command
        :param log_retention: The number of days that the lambda function's log events are kept in CloudWatch Logs. Default: logs.RetentionDays.INFINITE
        :param memory_limit: The amount of memory (in MiB) to allocate to the AWS Lambda function which replicates the files from the CDK bucket to the destination bucket. If you are deploying large files, you will need to increase this number accordingly. Default: 128
        :param metadata: User-defined object metadata to be set on all objects in the deployment. Default: - No user metadata is set
        :param prune: If this is set to false, files in the destination bucket that do not exist in the asset, will NOT be deleted during deployment (create/update). Default: true
        :param retain_on_delete: If this is set to "false", the destination files will be deleted when the resource is deleted or the destination is updated. NOTICE: Configuring this to "false" might have operational implications. Please visit to the package documentation referred below to make sure you fully understand those implications. Default: true - when resource is deleted/updated, files are retained
        :param role: Execution role associated with this function. Default: - A role is automatically created
        :param server_side_encryption: System-defined x-amz-server-side-encryption metadata to be set on all objects in the deployment. Default: - Server side encryption is not used.
        :param server_side_encryption_aws_kms_key_id: System-defined x-amz-server-side-encryption-aws-kms-key-id metadata to be set on all objects in the deployment. Default: - Not set.
        :param server_side_encryption_customer_algorithm: System-defined x-amz-server-side-encryption-customer-algorithm metadata to be set on all objects in the deployment. Warning: This is not a useful parameter until this bug is fixed: https://github.com/aws/aws-cdk/issues/6080 Default: - Not set.
        :param sign_content: If set to true, uploads will precompute the value of ``x-amz-content-sha256`` and include it in the signed S3 request headers. Default: - ``x-amz-content-sha256`` will not be computed
        :param storage_class: System-defined x-amz-storage-class metadata to be set on all objects in the deployment. Default: - Default storage-class for the bucket is used.
        :param use_efs: Mount an EFS file system. Enable this if your assets are large and you encounter disk space errors. Enabling this option will require a VPC to be specified. Default: - No EFS. Lambda has access only to 512MB of disk space.
        :param vpc: The VPC network to place the deployment lambda handler in. This is required if ``useEfs`` is set. Default: None
        :param vpc_subnets: Where in the VPC to place the deployment lambda handler. Only used if 'vpc' is supplied. Default: - the Vpc default strategy if not specified
        :param website_redirect_location: System-defined x-amz-website-redirect-location metadata to be set on all objects in the deployment. Default: - No website redirection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2544491e92aa50a255b927ef16b9cde2961eae48803afca3b5d1105bfc3398f1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BucketDeploymentProps(
            destination_bucket=destination_bucket,
            sources=sources,
            access_control=access_control,
            cache_control=cache_control,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            destination_key_prefix=destination_key_prefix,
            distribution=distribution,
            distribution_paths=distribution_paths,
            ephemeral_storage_size=ephemeral_storage_size,
            exclude=exclude,
            expires=expires,
            extract=extract,
            include=include,
            log_retention=log_retention,
            memory_limit=memory_limit,
            metadata=metadata,
            prune=prune,
            retain_on_delete=retain_on_delete,
            role=role,
            server_side_encryption=server_side_encryption,
            server_side_encryption_aws_kms_key_id=server_side_encryption_aws_kms_key_id,
            server_side_encryption_customer_algorithm=server_side_encryption_customer_algorithm,
            sign_content=sign_content,
            storage_class=storage_class,
            use_efs=use_efs,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            website_redirect_location=website_redirect_location,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addSource")
    def add_source(self, source: "ISource") -> None:
        '''Add an additional source to the bucket deployment.

        :param source: -

        Example::

            # website_bucket: s3.IBucket
            
            deployment = s3deploy.BucketDeployment(self, "Deployment",
                sources=[s3deploy.Source.asset("./website-dist")],
                destination_bucket=website_bucket
            )
            
            deployment.add_source(s3deploy.Source.asset("./another-asset"))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc987787f1589c85fbb65eaf66aaf15684268f9d214e1a0278f52c99e907028)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        return typing.cast(None, jsii.invoke(self, "addSource", [source]))

    @builtins.property
    @jsii.member(jsii_name="deployedBucket")
    def deployed_bucket(self) -> _IBucket_42e086fd:
        '''The bucket after the deployment.

        If you want to reference the destination bucket in another construct and make sure the
        bucket deployment has happened before the next operation is started, pass the other construct
        a reference to ``deployment.deployedBucket``.

        Note that this only returns an immutable reference to the destination bucket.
        If sequenced access to the original destination bucket is required, you may add a dependency
        on the bucket deployment instead: ``otherResource.node.addDependency(deployment)``
        '''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "deployedBucket"))

    @builtins.property
    @jsii.member(jsii_name="objectKeys")
    def object_keys(self) -> typing.List[builtins.str]:
        '''The object keys for the sources deployed to the S3 bucket.

        This returns a list of tokenized object keys for source files that are deployed to the bucket.

        This can be useful when using ``BucketDeployment`` with ``extract`` set to ``false`` and you need to reference
        the object key that resides in the bucket for that zip source file somewhere else in your CDK
        application, such as in a CFN output.

        For example, use ``Fn.select(0, myBucketDeployment.objectKeys)`` to reference the object key of the
        first source file in your bucket deployment.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "objectKeys"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_deployment.BucketDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_bucket": "destinationBucket",
        "sources": "sources",
        "access_control": "accessControl",
        "cache_control": "cacheControl",
        "content_disposition": "contentDisposition",
        "content_encoding": "contentEncoding",
        "content_language": "contentLanguage",
        "content_type": "contentType",
        "destination_key_prefix": "destinationKeyPrefix",
        "distribution": "distribution",
        "distribution_paths": "distributionPaths",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "exclude": "exclude",
        "expires": "expires",
        "extract": "extract",
        "include": "include",
        "log_retention": "logRetention",
        "memory_limit": "memoryLimit",
        "metadata": "metadata",
        "prune": "prune",
        "retain_on_delete": "retainOnDelete",
        "role": "role",
        "server_side_encryption": "serverSideEncryption",
        "server_side_encryption_aws_kms_key_id": "serverSideEncryptionAwsKmsKeyId",
        "server_side_encryption_customer_algorithm": "serverSideEncryptionCustomerAlgorithm",
        "sign_content": "signContent",
        "storage_class": "storageClass",
        "use_efs": "useEfs",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "website_redirect_location": "websiteRedirectLocation",
    },
)
class BucketDeploymentProps:
    def __init__(
        self,
        *,
        destination_bucket: _IBucket_42e086fd,
        sources: typing.Sequence["ISource"],
        access_control: typing.Optional[_BucketAccessControl_466c7e1b] = None,
        cache_control: typing.Optional[typing.Sequence["CacheControl"]] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_language: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        destination_key_prefix: typing.Optional[builtins.str] = None,
        distribution: typing.Optional[_IDistribution_7ac752a4] = None,
        distribution_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        expires: typing.Optional[_Expiration_059d47d0] = None,
        extract: typing.Optional[builtins.bool] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        prune: typing.Optional[builtins.bool] = None,
        retain_on_delete: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        server_side_encryption: typing.Optional["ServerSideEncryption"] = None,
        server_side_encryption_aws_kms_key_id: typing.Optional[builtins.str] = None,
        server_side_encryption_customer_algorithm: typing.Optional[builtins.str] = None,
        sign_content: typing.Optional[builtins.bool] = None,
        storage_class: typing.Optional["StorageClass"] = None,
        use_efs: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        website_redirect_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for ``BucketDeployment``.

        :param destination_bucket: The S3 bucket to sync the contents of the zip file to.
        :param sources: The sources from which to deploy the contents of this bucket.
        :param access_control: System-defined x-amz-acl metadata to be set on all objects in the deployment. Default: - Not set.
        :param cache_control: System-defined cache-control metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_disposition: System-defined cache-disposition metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_encoding: System-defined content-encoding metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_language: System-defined content-language metadata to be set on all objects in the deployment. Default: - Not set.
        :param content_type: System-defined content-type metadata to be set on all objects in the deployment. Default: - Not set.
        :param destination_key_prefix: Key prefix in the destination bucket. Must be <=104 characters Default: "/" (unzip to root of the destination bucket)
        :param distribution: The CloudFront distribution using the destination bucket as an origin. Files in the distribution's edge caches will be invalidated after files are uploaded to the destination bucket. Default: - No invalidation occurs
        :param distribution_paths: The file paths to invalidate in the CloudFront distribution. Default: - All files under the destination bucket key prefix will be invalidated.
        :param ephemeral_storage_size: The size of the AWS Lambda function’s /tmp directory in MiB. Default: 512 MiB
        :param exclude: If this is set, matching files or objects will be excluded from the deployment's sync command. This can be used to exclude a file from being pruned in the destination bucket. If you want to just exclude files from the deployment package (which excludes these files evaluated when invalidating the asset), you should leverage the ``exclude`` property of ``AssetOptions`` when defining your source. Default: - No exclude filters are used
        :param expires: System-defined expires metadata to be set on all objects in the deployment. Default: - The objects in the distribution will not expire.
        :param extract: If this is set, the zip file will be synced to the destination S3 bucket and extracted. If false, the file will remain zipped in the destination bucket. Default: true
        :param include: If this is set, matching files or objects will be included with the deployment's sync command. Since all files from the deployment package are included by default, this property is usually leveraged alongside an ``exclude`` filter. Default: - No include filters are used and all files are included with the sync command
        :param log_retention: The number of days that the lambda function's log events are kept in CloudWatch Logs. Default: logs.RetentionDays.INFINITE
        :param memory_limit: The amount of memory (in MiB) to allocate to the AWS Lambda function which replicates the files from the CDK bucket to the destination bucket. If you are deploying large files, you will need to increase this number accordingly. Default: 128
        :param metadata: User-defined object metadata to be set on all objects in the deployment. Default: - No user metadata is set
        :param prune: If this is set to false, files in the destination bucket that do not exist in the asset, will NOT be deleted during deployment (create/update). Default: true
        :param retain_on_delete: If this is set to "false", the destination files will be deleted when the resource is deleted or the destination is updated. NOTICE: Configuring this to "false" might have operational implications. Please visit to the package documentation referred below to make sure you fully understand those implications. Default: true - when resource is deleted/updated, files are retained
        :param role: Execution role associated with this function. Default: - A role is automatically created
        :param server_side_encryption: System-defined x-amz-server-side-encryption metadata to be set on all objects in the deployment. Default: - Server side encryption is not used.
        :param server_side_encryption_aws_kms_key_id: System-defined x-amz-server-side-encryption-aws-kms-key-id metadata to be set on all objects in the deployment. Default: - Not set.
        :param server_side_encryption_customer_algorithm: System-defined x-amz-server-side-encryption-customer-algorithm metadata to be set on all objects in the deployment. Warning: This is not a useful parameter until this bug is fixed: https://github.com/aws/aws-cdk/issues/6080 Default: - Not set.
        :param sign_content: If set to true, uploads will precompute the value of ``x-amz-content-sha256`` and include it in the signed S3 request headers. Default: - ``x-amz-content-sha256`` will not be computed
        :param storage_class: System-defined x-amz-storage-class metadata to be set on all objects in the deployment. Default: - Default storage-class for the bucket is used.
        :param use_efs: Mount an EFS file system. Enable this if your assets are large and you encounter disk space errors. Enabling this option will require a VPC to be specified. Default: - No EFS. Lambda has access only to 512MB of disk space.
        :param vpc: The VPC network to place the deployment lambda handler in. This is required if ``useEfs`` is set. Default: None
        :param vpc_subnets: Where in the VPC to place the deployment lambda handler. Only used if 'vpc' is supplied. Default: - the Vpc default strategy if not specified
        :param website_redirect_location: System-defined x-amz-website-redirect-location metadata to be set on all objects in the deployment. Default: - No website redirection.

        :exampleMetadata: infused

        Example::

            # website_bucket: s3.Bucket
            
            
            deployment = s3deploy.BucketDeployment(self, "DeployWebsite",
                sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
                destination_bucket=website_bucket
            )
            
            ConstructThatReadsFromTheBucket(self, "Consumer", {
                # Use 'deployment.deployedBucket' instead of 'websiteBucket' here
                "bucket": deployment.deployed_bucket
            })
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbabf07e8b4adfb2b2058c075c4f35512ebc580f80a6db9bf13e905898822551)
            check_type(argname="argument destination_bucket", value=destination_bucket, expected_type=type_hints["destination_bucket"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument access_control", value=access_control, expected_type=type_hints["access_control"])
            check_type(argname="argument cache_control", value=cache_control, expected_type=type_hints["cache_control"])
            check_type(argname="argument content_disposition", value=content_disposition, expected_type=type_hints["content_disposition"])
            check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
            check_type(argname="argument content_language", value=content_language, expected_type=type_hints["content_language"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument destination_key_prefix", value=destination_key_prefix, expected_type=type_hints["destination_key_prefix"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument distribution_paths", value=distribution_paths, expected_type=type_hints["distribution_paths"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument expires", value=expires, expected_type=type_hints["expires"])
            check_type(argname="argument extract", value=extract, expected_type=type_hints["extract"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument memory_limit", value=memory_limit, expected_type=type_hints["memory_limit"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument prune", value=prune, expected_type=type_hints["prune"])
            check_type(argname="argument retain_on_delete", value=retain_on_delete, expected_type=type_hints["retain_on_delete"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument server_side_encryption", value=server_side_encryption, expected_type=type_hints["server_side_encryption"])
            check_type(argname="argument server_side_encryption_aws_kms_key_id", value=server_side_encryption_aws_kms_key_id, expected_type=type_hints["server_side_encryption_aws_kms_key_id"])
            check_type(argname="argument server_side_encryption_customer_algorithm", value=server_side_encryption_customer_algorithm, expected_type=type_hints["server_side_encryption_customer_algorithm"])
            check_type(argname="argument sign_content", value=sign_content, expected_type=type_hints["sign_content"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument use_efs", value=use_efs, expected_type=type_hints["use_efs"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument website_redirect_location", value=website_redirect_location, expected_type=type_hints["website_redirect_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_bucket": destination_bucket,
            "sources": sources,
        }
        if access_control is not None:
            self._values["access_control"] = access_control
        if cache_control is not None:
            self._values["cache_control"] = cache_control
        if content_disposition is not None:
            self._values["content_disposition"] = content_disposition
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding
        if content_language is not None:
            self._values["content_language"] = content_language
        if content_type is not None:
            self._values["content_type"] = content_type
        if destination_key_prefix is not None:
            self._values["destination_key_prefix"] = destination_key_prefix
        if distribution is not None:
            self._values["distribution"] = distribution
        if distribution_paths is not None:
            self._values["distribution_paths"] = distribution_paths
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if exclude is not None:
            self._values["exclude"] = exclude
        if expires is not None:
            self._values["expires"] = expires
        if extract is not None:
            self._values["extract"] = extract
        if include is not None:
            self._values["include"] = include
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if metadata is not None:
            self._values["metadata"] = metadata
        if prune is not None:
            self._values["prune"] = prune
        if retain_on_delete is not None:
            self._values["retain_on_delete"] = retain_on_delete
        if role is not None:
            self._values["role"] = role
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if server_side_encryption_aws_kms_key_id is not None:
            self._values["server_side_encryption_aws_kms_key_id"] = server_side_encryption_aws_kms_key_id
        if server_side_encryption_customer_algorithm is not None:
            self._values["server_side_encryption_customer_algorithm"] = server_side_encryption_customer_algorithm
        if sign_content is not None:
            self._values["sign_content"] = sign_content
        if storage_class is not None:
            self._values["storage_class"] = storage_class
        if use_efs is not None:
            self._values["use_efs"] = use_efs
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if website_redirect_location is not None:
            self._values["website_redirect_location"] = website_redirect_location

    @builtins.property
    def destination_bucket(self) -> _IBucket_42e086fd:
        '''The S3 bucket to sync the contents of the zip file to.'''
        result = self._values.get("destination_bucket")
        assert result is not None, "Required property 'destination_bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def sources(self) -> typing.List["ISource"]:
        '''The sources from which to deploy the contents of this bucket.'''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.List["ISource"], result)

    @builtins.property
    def access_control(self) -> typing.Optional[_BucketAccessControl_466c7e1b]:
        '''System-defined x-amz-acl metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
        '''
        result = self._values.get("access_control")
        return typing.cast(typing.Optional[_BucketAccessControl_466c7e1b], result)

    @builtins.property
    def cache_control(self) -> typing.Optional[typing.List["CacheControl"]]:
        '''System-defined cache-control metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("cache_control")
        return typing.cast(typing.Optional[typing.List["CacheControl"]], result)

    @builtins.property
    def content_disposition(self) -> typing.Optional[builtins.str]:
        '''System-defined cache-disposition metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("content_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''System-defined content-encoding metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_language(self) -> typing.Optional[builtins.str]:
        '''System-defined content-language metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("content_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''System-defined content-type metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Key prefix in the destination bucket.

        Must be <=104 characters

        :default: "/" (unzip to root of the destination bucket)
        '''
        result = self._values.get("destination_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution(self) -> typing.Optional[_IDistribution_7ac752a4]:
        '''The CloudFront distribution using the destination bucket as an origin.

        Files in the distribution's edge caches will be invalidated after
        files are uploaded to the destination bucket.

        :default: - No invalidation occurs
        '''
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[_IDistribution_7ac752a4], result)

    @builtins.property
    def distribution_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The file paths to invalidate in the CloudFront distribution.

        :default: - All files under the destination bucket key prefix will be invalidated.
        '''
        result = self._values.get("distribution_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The size of the AWS Lambda function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If this is set, matching files or objects will be excluded from the deployment's sync command.

        This can be used to exclude a file from being pruned in the destination bucket.

        If you want to just exclude files from the deployment package (which excludes these files
        evaluated when invalidating the asset), you should leverage the ``exclude`` property of
        ``AssetOptions`` when defining your source.

        :default: - No exclude filters are used

        :see: https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expires(self) -> typing.Optional[_Expiration_059d47d0]:
        '''System-defined expires metadata to be set on all objects in the deployment.

        :default: - The objects in the distribution will not expire.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[_Expiration_059d47d0], result)

    @builtins.property
    def extract(self) -> typing.Optional[builtins.bool]:
        '''If this is set, the zip file will be synced to the destination S3 bucket and extracted.

        If false, the file will remain zipped in the destination bucket.

        :default: true
        '''
        result = self._values.get("extract")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If this is set, matching files or objects will be included with the deployment's sync command.

        Since all files from the deployment package are included by default, this property
        is usually leveraged alongside an ``exclude`` filter.

        :default: - No include filters are used and all files are included with the sync command

        :see: https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days that the lambda function's log events are kept in CloudWatch Logs.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory (in MiB) to allocate to the AWS Lambda function which replicates the files from the CDK bucket to the destination bucket.

        If you are deploying large files, you will need to increase this number
        accordingly.

        :default: 128
        '''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-defined object metadata to be set on all objects in the deployment.

        :default: - No user metadata is set

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def prune(self) -> typing.Optional[builtins.bool]:
        '''If this is set to false, files in the destination bucket that do not exist in the asset, will NOT be deleted during deployment (create/update).

        :default: true

        :see: https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html
        '''
        result = self._values.get("prune")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def retain_on_delete(self) -> typing.Optional[builtins.bool]:
        '''If this is set to "false", the destination files will be deleted when the resource is deleted or the destination is updated.

        NOTICE: Configuring this to "false" might have operational implications. Please
        visit to the package documentation referred below to make sure you fully understand those implications.

        :default: true - when resource is deleted/updated, files are retained

        :see: https://github.com/aws/aws-cdk/tree/main/packages/aws-cdk-lib/aws-s3-deployment#retain-on-delete
        '''
        result = self._values.get("retain_on_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Execution role associated with this function.

        :default: - A role is automatically created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def server_side_encryption(self) -> typing.Optional["ServerSideEncryption"]:
        '''System-defined x-amz-server-side-encryption metadata to be set on all objects in the deployment.

        :default: - Server side encryption is not used.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional["ServerSideEncryption"], result)

    @builtins.property
    def server_side_encryption_aws_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''System-defined x-amz-server-side-encryption-aws-kms-key-id metadata to be set on all objects in the deployment.

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("server_side_encryption_aws_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_customer_algorithm(
        self,
    ) -> typing.Optional[builtins.str]:
        '''System-defined x-amz-server-side-encryption-customer-algorithm metadata to be set on all objects in the deployment.

        Warning: This is not a useful parameter until this bug is fixed: https://github.com/aws/aws-cdk/issues/6080

        :default: - Not set.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html#sse-c-how-to-programmatically-intro
        '''
        result = self._values.get("server_side_encryption_customer_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sign_content(self) -> typing.Optional[builtins.bool]:
        '''If set to true, uploads will precompute the value of ``x-amz-content-sha256`` and include it in the signed S3 request headers.

        :default: - ``x-amz-content-sha256`` will not be computed
        '''
        result = self._values.get("sign_content")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def storage_class(self) -> typing.Optional["StorageClass"]:
        '''System-defined x-amz-storage-class metadata to be set on all objects in the deployment.

        :default: - Default storage-class for the bucket is used.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional["StorageClass"], result)

    @builtins.property
    def use_efs(self) -> typing.Optional[builtins.bool]:
        '''Mount an EFS file system.

        Enable this if your assets are large and you encounter disk space errors.
        Enabling this option will require a VPC to be specified.

        :default: - No EFS. Lambda has access only to 512MB of disk space.
        '''
        result = self._values.get("use_efs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The VPC network to place the deployment lambda handler in.

        This is required if ``useEfs`` is set.

        :default: None
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Where in the VPC to place the deployment lambda handler.

        Only used if 'vpc' is supplied.

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def website_redirect_location(self) -> typing.Optional[builtins.str]:
        '''System-defined x-amz-website-redirect-location metadata to be set on all objects in the deployment.

        :default: - No website redirection.

        :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
        '''
        result = self._values.get("website_redirect_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BucketDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CacheControl(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_deployment.CacheControl",
):
    '''Used for HTTP cache-control header, which influences downstream caches.

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :exampleMetadata: infused

    Example::

        # destination_bucket: s3.Bucket
        
        s3deploy.BucketDeployment(self, "BucketDeployment",
            sources=[s3deploy.Source.asset("./website", exclude=["index.html"])],
            destination_bucket=destination_bucket,
            cache_control=[
                s3deploy.CacheControl.max_age(Duration.days(365)),
                s3deploy.CacheControl.immutable()
            ],
            prune=False
        )
        
        s3deploy.BucketDeployment(self, "HTMLBucketDeployment",
            sources=[s3deploy.Source.asset("./website", exclude=["*", "!index.html"])],
            destination_bucket=destination_bucket,
            cache_control=[
                s3deploy.CacheControl.max_age(Duration.seconds(0))
            ],
            prune=False
        )
    '''

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, s: builtins.str) -> "CacheControl":
        '''Constructs a custom cache control key from the literal value.

        :param s: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5378bf4b640b7a16c7706bd09f00794879ed5887b573039696c2f987de8de56d)
            check_type(argname="argument s", value=s, expected_type=type_hints["s"])
        return typing.cast("CacheControl", jsii.sinvoke(cls, "fromString", [s]))

    @jsii.member(jsii_name="immutable")
    @builtins.classmethod
    def immutable(cls) -> "CacheControl":
        '''Sets 'immutable'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "immutable", []))

    @jsii.member(jsii_name="maxAge")
    @builtins.classmethod
    def max_age(cls, t: _Duration_4839e8c3) -> "CacheControl":
        '''Sets 'max-age='.

        :param t: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14f79d30bb247c06b3cb4a2320993bccd612f49f73aaef2c26c0ebedc35f9fb8)
            check_type(argname="argument t", value=t, expected_type=type_hints["t"])
        return typing.cast("CacheControl", jsii.sinvoke(cls, "maxAge", [t]))

    @jsii.member(jsii_name="mustRevalidate")
    @builtins.classmethod
    def must_revalidate(cls) -> "CacheControl":
        '''Sets 'must-revalidate'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "mustRevalidate", []))

    @jsii.member(jsii_name="mustUnderstand")
    @builtins.classmethod
    def must_understand(cls) -> "CacheControl":
        '''Sets 'must-understand'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "mustUnderstand", []))

    @jsii.member(jsii_name="noCache")
    @builtins.classmethod
    def no_cache(cls) -> "CacheControl":
        '''Sets 'no-cache'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noCache", []))

    @jsii.member(jsii_name="noStore")
    @builtins.classmethod
    def no_store(cls) -> "CacheControl":
        '''Sets 'no-store'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noStore", []))

    @jsii.member(jsii_name="noTransform")
    @builtins.classmethod
    def no_transform(cls) -> "CacheControl":
        '''Sets 'no-transform'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "noTransform", []))

    @jsii.member(jsii_name="proxyRevalidate")
    @builtins.classmethod
    def proxy_revalidate(cls) -> "CacheControl":
        '''Sets 'proxy-revalidate'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "proxyRevalidate", []))

    @jsii.member(jsii_name="setPrivate")
    @builtins.classmethod
    def set_private(cls) -> "CacheControl":
        '''Sets 'private'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "setPrivate", []))

    @jsii.member(jsii_name="setPublic")
    @builtins.classmethod
    def set_public(cls) -> "CacheControl":
        '''Sets 'public'.'''
        return typing.cast("CacheControl", jsii.sinvoke(cls, "setPublic", []))

    @jsii.member(jsii_name="sMaxAge")
    @builtins.classmethod
    def s_max_age(cls, t: _Duration_4839e8c3) -> "CacheControl":
        '''Sets 's-maxage='.

        :param t: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96c203ed36a911c67a4356f7768a4928e9a7464835e49835710be73dc668b3d)
            check_type(argname="argument t", value=t, expected_type=type_hints["t"])
        return typing.cast("CacheControl", jsii.sinvoke(cls, "sMaxAge", [t]))

    @jsii.member(jsii_name="staleIfError")
    @builtins.classmethod
    def stale_if_error(cls, t: _Duration_4839e8c3) -> "CacheControl":
        '''Sets 'stale-if-error='.

        :param t: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d48c4dcfd62f99fb0645aaf9ca6fcca8bfc43722d85da78361dcbbfacd8fdf9)
            check_type(argname="argument t", value=t, expected_type=type_hints["t"])
        return typing.cast("CacheControl", jsii.sinvoke(cls, "staleIfError", [t]))

    @jsii.member(jsii_name="staleWhileRevalidate")
    @builtins.classmethod
    def stale_while_revalidate(cls, t: _Duration_4839e8c3) -> "CacheControl":
        '''Sets 'stale-while-revalidate='.

        :param t: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aaa953e1322a312b836e3d02a57efce71331179075d841c94b6509acc78c127)
            check_type(argname="argument t", value=t, expected_type=type_hints["t"])
        return typing.cast("CacheControl", jsii.sinvoke(cls, "staleWhileRevalidate", [t]))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''The raw cache control setting.'''
        return typing.cast(typing.Any, jsii.get(self, "value"))


class DeployTimeSubstitutedFile(
    BucketDeployment,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_deployment.DeployTimeSubstitutedFile",
):
    '''``DeployTimeSubstitutedFile`` is an extension of ``BucketDeployment`` that allows users to upload individual files and specify to make substitutions in the file.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        
        # my_lambda_function: lambda.Function
        # destination_bucket: s3.Bucket
        
        
        s3deploy.DeployTimeSubstitutedFile(self, "MyFile",
            source="my-file.yaml",
            destination_bucket=destination_bucket,
            substitutions={
                "variable_name": my_lambda_function.function_name
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_bucket: _IBucket_42e086fd,
        source: builtins.str,
        substitutions: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param destination_bucket: The S3 bucket to sync the contents of the zip file to.
        :param source: Path to the user's local file.
        :param substitutions: User-defined substitutions to make in the file. Placeholders in the user's local file must be specified with double curly brackets and spaces. For example, if you use the key 'xxxx' in the file, it must be written as: {{ xxxx }} to be recognized by the construct as a substitution.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__949c9855e9b54e6de98791d11d29d611c30d018ab383262c46e50c147e4f0c3a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DeployTimeSubstitutedFileProps(
            destination_bucket=destination_bucket,
            source=source,
            substitutions=substitutions,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="objectKey")
    def object_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_deployment.DeployTimeSubstitutedFileProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_bucket": "destinationBucket",
        "source": "source",
        "substitutions": "substitutions",
    },
)
class DeployTimeSubstitutedFileProps:
    def __init__(
        self,
        *,
        destination_bucket: _IBucket_42e086fd,
        source: builtins.str,
        substitutions: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param destination_bucket: The S3 bucket to sync the contents of the zip file to.
        :param source: Path to the user's local file.
        :param substitutions: User-defined substitutions to make in the file. Placeholders in the user's local file must be specified with double curly brackets and spaces. For example, if you use the key 'xxxx' in the file, it must be written as: {{ xxxx }} to be recognized by the construct as a substitution.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            
            # my_lambda_function: lambda.Function
            # destination_bucket: s3.Bucket
            
            
            s3deploy.DeployTimeSubstitutedFile(self, "MyFile",
                source="my-file.yaml",
                destination_bucket=destination_bucket,
                substitutions={
                    "variable_name": my_lambda_function.function_name
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f4f8459d8085fcf9b16b599923964d327352dc55d826fafc9ee9b97a6b50856)
            check_type(argname="argument destination_bucket", value=destination_bucket, expected_type=type_hints["destination_bucket"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument substitutions", value=substitutions, expected_type=type_hints["substitutions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_bucket": destination_bucket,
            "source": source,
            "substitutions": substitutions,
        }

    @builtins.property
    def destination_bucket(self) -> _IBucket_42e086fd:
        '''The S3 bucket to sync the contents of the zip file to.'''
        result = self._values.get("destination_bucket")
        assert result is not None, "Required property 'destination_bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Path to the user's local file.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def substitutions(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''User-defined substitutions to make in the file.

        Placeholders in the user's local file must be specified with double curly
        brackets and spaces. For example, if you use the key 'xxxx' in the file,
        it must be written as: {{ xxxx }} to be recognized by the construct as a
        substitution.
        '''
        result = self._values.get("substitutions")
        assert result is not None, "Required property 'substitutions' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeployTimeSubstitutedFileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_deployment.DeploymentSourceContext",
    jsii_struct_bases=[],
    name_mapping={"handler_role": "handlerRole"},
)
class DeploymentSourceContext:
    def __init__(self, *, handler_role: _IRole_235f5d8e) -> None:
        '''Bind context for ISources.

        :param handler_role: The role for the handler.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_s3_deployment as s3_deployment
            
            # role: iam.Role
            
            deployment_source_context = s3_deployment.DeploymentSourceContext(
                handler_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ffd3edc16757379a6161515d1c48008f74a9a937f09669c10cbcda3758a5a2)
            check_type(argname="argument handler_role", value=handler_role, expected_type=type_hints["handler_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "handler_role": handler_role,
        }

    @builtins.property
    def handler_role(self) -> _IRole_235f5d8e:
        '''The role for the handler.'''
        result = self._values.get("handler_role")
        assert result is not None, "Required property 'handler_role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentSourceContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_s3_deployment.ISource")
class ISource(typing_extensions.Protocol):
    '''Represents a source for bucket deployments.'''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        handler_role: _IRole_235f5d8e,
    ) -> "SourceConfig":
        '''Binds the source to a bucket deployment.

        :param scope: The construct tree context.
        :param handler_role: The role for the handler.
        '''
        ...


class _ISourceProxy:
    '''Represents a source for bucket deployments.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_s3_deployment.ISource"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        handler_role: _IRole_235f5d8e,
    ) -> "SourceConfig":
        '''Binds the source to a bucket deployment.

        :param scope: The construct tree context.
        :param handler_role: The role for the handler.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09970416699f317cf422c30f785da12ff6ed72f1358bc0e3e4adcf6e613fc748)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        context = DeploymentSourceContext(handler_role=handler_role)

        return typing.cast("SourceConfig", jsii.invoke(self, "bind", [scope, context]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISource).__jsii_proxy_class__ = lambda : _ISourceProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_s3_deployment.ServerSideEncryption")
class ServerSideEncryption(enum.Enum):
    '''Indicates whether server-side encryption is enabled for the object, and whether that encryption is from the AWS Key Management Service (AWS KMS) or from Amazon S3 managed encryption (SSE-S3).

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :exampleMetadata: infused

    Example::

        website_bucket = s3.Bucket(self, "WebsiteBucket",
            website_index_document="index.html",
            public_read_access=True
        )
        
        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./website-dist")],
            destination_bucket=website_bucket,
            destination_key_prefix="web/static",  # optional prefix in destination bucket
            metadata={"A": "1", "b": "2"},  # user-defined metadata
        
            # system-defined metadata
            content_type="text/html",
            content_language="en",
            storage_class=s3deploy.StorageClass.INTELLIGENT_TIERING,
            server_side_encryption=s3deploy.ServerSideEncryption.AES_256,
            cache_control=[
                s3deploy.CacheControl.set_public(),
                s3deploy.CacheControl.max_age(Duration.hours(1))
            ],
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL
        )
    '''

    AES_256 = "AES_256"
    ''''AES256'.'''
    AWS_KMS = "AWS_KMS"
    ''''aws:kms'.'''


class Source(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_s3_deployment.Source"):
    '''Specifies bucket deployment source.

    Usage::

       Source.bucket(bucket, key)
       Source.asset('/local/path/to/directory')
       Source.asset('/local/path/to/a/file.zip')
       Source.data('hello/world/file.txt', 'Hello, world!')
       Source.dataJson('config.json', { baz: topic.topicArn })
       Source.dataYaml('config.yaml', { baz: topic.topicArn })

    :exampleMetadata: infused

    Example::

        # website_bucket: s3.Bucket
        
        
        deployment = s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset(path.join(__dirname, "my-website"))],
            destination_bucket=website_bucket
        )
        
        ConstructThatReadsFromTheBucket(self, "Consumer", {
            # Use 'deployment.deployedBucket' instead of 'websiteBucket' here
            "bucket": deployment.deployed_bucket
        })
    '''

    @jsii.member(jsii_name="asset")
    @builtins.classmethod
    def asset(
        cls,
        path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> ISource:
        '''Uses a local asset as the deployment source.

        If the local asset is a .zip archive, make sure you trust the
        producer of the archive.

        :param path: The path to a local .zip file or a directory.
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc877c69568cee7364ec77003356fc6818118602dda64adf3dbf38ff7eec10b2)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = _AssetOptions_2aa69621(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast(ISource, jsii.sinvoke(cls, "asset", [path, options]))

    @jsii.member(jsii_name="bucket")
    @builtins.classmethod
    def bucket(cls, bucket: _IBucket_42e086fd, zip_object_key: builtins.str) -> ISource:
        '''Uses a .zip file stored in an S3 bucket as the source for the destination bucket contents.

        Make sure you trust the producer of the archive.

        :param bucket: The S3 Bucket.
        :param zip_object_key: The S3 object key of the zip file with contents.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcaba123a95f1aa9d99f9f5af319da23dd5f345454e757ba9257364325b3efb5)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument zip_object_key", value=zip_object_key, expected_type=type_hints["zip_object_key"])
        return typing.cast(ISource, jsii.sinvoke(cls, "bucket", [bucket, zip_object_key]))

    @jsii.member(jsii_name="data")
    @builtins.classmethod
    def data(cls, object_key: builtins.str, data: builtins.str) -> ISource:
        '''Deploys an object with the specified string contents into the bucket.

        The
        content can include deploy-time values (such as ``snsTopic.topicArn``) that
        will get resolved only during deployment.

        To store a JSON object use ``Source.jsonData()``.
        To store YAML content use ``Source.yamlData()``.

        :param object_key: The destination S3 object key (relative to the root of the S3 deployment).
        :param data: The data to be stored in the object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__798b55b643d389adf599acde4d214b0b843e07f8c7984ea0e848f2da7c62822c)
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        return typing.cast(ISource, jsii.sinvoke(cls, "data", [object_key, data]))

    @jsii.member(jsii_name="jsonData")
    @builtins.classmethod
    def json_data(cls, object_key: builtins.str, obj: typing.Any) -> ISource:
        '''Deploys an object with the specified JSON object into the bucket.

        The
        object can include deploy-time values (such as ``snsTopic.topicArn``) that
        will get resolved only during deployment.

        :param object_key: The destination S3 object key (relative to the root of the S3 deployment).
        :param obj: A JSON object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34bf47f9cf16464b2d85173fbce8786a1afe889c23001b8c7575c49e0bf93ff9)
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(ISource, jsii.sinvoke(cls, "jsonData", [object_key, obj]))

    @jsii.member(jsii_name="yamlData")
    @builtins.classmethod
    def yaml_data(cls, object_key: builtins.str, obj: typing.Any) -> ISource:
        '''Deploys an object with the specified JSON object formatted as YAML into the bucket.

        The object can include deploy-time values (such as ``snsTopic.topicArn``) that
        will get resolved only during deployment.

        :param object_key: The destination S3 object key (relative to the root of the S3 deployment).
        :param obj: A JSON object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0fa5367aafa7b8db0300fa69edeca060cb4ca66d1517ccc855345cc9bfe37e)
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(ISource, jsii.sinvoke(cls, "yamlData", [object_key, obj]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_deployment.SourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "zip_object_key": "zipObjectKey",
        "markers": "markers",
    },
)
class SourceConfig:
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        zip_object_key: builtins.str,
        markers: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''Source information.

        :param bucket: The source bucket to deploy from.
        :param zip_object_key: An S3 object key in the source bucket that points to a zip file.
        :param markers: A set of markers to substitute in the source content. Default: - no markers

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3 as s3
            from aws_cdk import aws_s3_deployment as s3_deployment
            
            # bucket: s3.Bucket
            # markers: Any
            
            source_config = s3_deployment.SourceConfig(
                bucket=bucket,
                zip_object_key="zipObjectKey",
            
                # the properties below are optional
                markers={
                    "markers_key": markers
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dafa1619bb92595ec0ff7aa95e55221719ed81eb6d2f7d44a84193d810c4265c)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument zip_object_key", value=zip_object_key, expected_type=type_hints["zip_object_key"])
            check_type(argname="argument markers", value=markers, expected_type=type_hints["markers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "zip_object_key": zip_object_key,
        }
        if markers is not None:
            self._values["markers"] = markers

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''The source bucket to deploy from.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def zip_object_key(self) -> builtins.str:
        '''An S3 object key in the source bucket that points to a zip file.'''
        result = self._values.get("zip_object_key")
        assert result is not None, "Required property 'zip_object_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def markers(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''A set of markers to substitute in the source content.

        :default: - no markers
        '''
        result = self._values.get("markers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_s3_deployment.StorageClass")
class StorageClass(enum.Enum):
    '''Storage class used for storing the object.

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :exampleMetadata: infused

    Example::

        website_bucket = s3.Bucket(self, "WebsiteBucket",
            website_index_document="index.html",
            public_read_access=True
        )
        
        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./website-dist")],
            destination_bucket=website_bucket,
            destination_key_prefix="web/static",  # optional prefix in destination bucket
            metadata={"A": "1", "b": "2"},  # user-defined metadata
        
            # system-defined metadata
            content_type="text/html",
            content_language="en",
            storage_class=s3deploy.StorageClass.INTELLIGENT_TIERING,
            server_side_encryption=s3deploy.ServerSideEncryption.AES_256,
            cache_control=[
                s3deploy.CacheControl.set_public(),
                s3deploy.CacheControl.max_age(Duration.hours(1))
            ],
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL
        )
    '''

    STANDARD = "STANDARD"
    ''''STANDARD'.'''
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    ''''REDUCED_REDUNDANCY'.'''
    STANDARD_IA = "STANDARD_IA"
    ''''STANDARD_IA'.'''
    ONEZONE_IA = "ONEZONE_IA"
    ''''ONEZONE_IA'.'''
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    ''''INTELLIGENT_TIERING'.'''
    GLACIER = "GLACIER"
    ''''GLACIER'.'''
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    ''''DEEP_ARCHIVE'.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3_deployment.UserDefinedObjectMetadata",
    jsii_struct_bases=[],
    name_mapping={},
)
class UserDefinedObjectMetadata:
    def __init__(self) -> None:
        '''(deprecated) Custom user defined metadata.

        :deprecated: Use raw property bags instead (object literals, ``Map<String,Object>``, etc... )

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3_deployment as s3_deployment
            
            user_defined_object_metadata = s3_deployment.UserDefinedObjectMetadata()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserDefinedObjectMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BucketDeployment",
    "BucketDeploymentProps",
    "CacheControl",
    "DeployTimeSubstitutedFile",
    "DeployTimeSubstitutedFileProps",
    "DeploymentSourceContext",
    "ISource",
    "ServerSideEncryption",
    "Source",
    "SourceConfig",
    "StorageClass",
    "UserDefinedObjectMetadata",
]

publication.publish()

def _typecheckingstub__2544491e92aa50a255b927ef16b9cde2961eae48803afca3b5d1105bfc3398f1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_bucket: _IBucket_42e086fd,
    sources: typing.Sequence[ISource],
    access_control: typing.Optional[_BucketAccessControl_466c7e1b] = None,
    cache_control: typing.Optional[typing.Sequence[CacheControl]] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_language: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    destination_key_prefix: typing.Optional[builtins.str] = None,
    distribution: typing.Optional[_IDistribution_7ac752a4] = None,
    distribution_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    expires: typing.Optional[_Expiration_059d47d0] = None,
    extract: typing.Optional[builtins.bool] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    memory_limit: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    prune: typing.Optional[builtins.bool] = None,
    retain_on_delete: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    server_side_encryption: typing.Optional[ServerSideEncryption] = None,
    server_side_encryption_aws_kms_key_id: typing.Optional[builtins.str] = None,
    server_side_encryption_customer_algorithm: typing.Optional[builtins.str] = None,
    sign_content: typing.Optional[builtins.bool] = None,
    storage_class: typing.Optional[StorageClass] = None,
    use_efs: typing.Optional[builtins.bool] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    website_redirect_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc987787f1589c85fbb65eaf66aaf15684268f9d214e1a0278f52c99e907028(
    source: ISource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbabf07e8b4adfb2b2058c075c4f35512ebc580f80a6db9bf13e905898822551(
    *,
    destination_bucket: _IBucket_42e086fd,
    sources: typing.Sequence[ISource],
    access_control: typing.Optional[_BucketAccessControl_466c7e1b] = None,
    cache_control: typing.Optional[typing.Sequence[CacheControl]] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_language: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    destination_key_prefix: typing.Optional[builtins.str] = None,
    distribution: typing.Optional[_IDistribution_7ac752a4] = None,
    distribution_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    expires: typing.Optional[_Expiration_059d47d0] = None,
    extract: typing.Optional[builtins.bool] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    memory_limit: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    prune: typing.Optional[builtins.bool] = None,
    retain_on_delete: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    server_side_encryption: typing.Optional[ServerSideEncryption] = None,
    server_side_encryption_aws_kms_key_id: typing.Optional[builtins.str] = None,
    server_side_encryption_customer_algorithm: typing.Optional[builtins.str] = None,
    sign_content: typing.Optional[builtins.bool] = None,
    storage_class: typing.Optional[StorageClass] = None,
    use_efs: typing.Optional[builtins.bool] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    website_redirect_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5378bf4b640b7a16c7706bd09f00794879ed5887b573039696c2f987de8de56d(
    s: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f79d30bb247c06b3cb4a2320993bccd612f49f73aaef2c26c0ebedc35f9fb8(
    t: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96c203ed36a911c67a4356f7768a4928e9a7464835e49835710be73dc668b3d(
    t: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d48c4dcfd62f99fb0645aaf9ca6fcca8bfc43722d85da78361dcbbfacd8fdf9(
    t: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aaa953e1322a312b836e3d02a57efce71331179075d841c94b6509acc78c127(
    t: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__949c9855e9b54e6de98791d11d29d611c30d018ab383262c46e50c147e4f0c3a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_bucket: _IBucket_42e086fd,
    source: builtins.str,
    substitutions: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4f8459d8085fcf9b16b599923964d327352dc55d826fafc9ee9b97a6b50856(
    *,
    destination_bucket: _IBucket_42e086fd,
    source: builtins.str,
    substitutions: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ffd3edc16757379a6161515d1c48008f74a9a937f09669c10cbcda3758a5a2(
    *,
    handler_role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09970416699f317cf422c30f785da12ff6ed72f1358bc0e3e4adcf6e613fc748(
    scope: _constructs_77d1e7e8.Construct,
    *,
    handler_role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc877c69568cee7364ec77003356fc6818118602dda64adf3dbf38ff7eec10b2(
    path: builtins.str,
    *,
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

def _typecheckingstub__bcaba123a95f1aa9d99f9f5af319da23dd5f345454e757ba9257364325b3efb5(
    bucket: _IBucket_42e086fd,
    zip_object_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798b55b643d389adf599acde4d214b0b843e07f8c7984ea0e848f2da7c62822c(
    object_key: builtins.str,
    data: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34bf47f9cf16464b2d85173fbce8786a1afe889c23001b8c7575c49e0bf93ff9(
    object_key: builtins.str,
    obj: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0fa5367aafa7b8db0300fa69edeca060cb4ca66d1517ccc855345cc9bfe37e(
    object_key: builtins.str,
    obj: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafa1619bb92595ec0ff7aa95e55221719ed81eb6d2f7d44a84193d810c4265c(
    *,
    bucket: _IBucket_42e086fd,
    zip_object_key: builtins.str,
    markers: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass
