'''
# Amazon Lambda Node.js Library

This library provides constructs for Node.js Lambda functions.

## Node.js Function

The `NodejsFunction` construct creates a Lambda function with automatic transpiling and bundling
of TypeScript or Javascript code. This results in smaller Lambda packages that contain only the
code and dependencies needed to run the function.

It uses [esbuild](https://esbuild.github.io/) under the hood.

## Reference project architecture

The `NodejsFunction` allows you to define your CDK and runtime dependencies in a single
package.json and to collocate your runtime code with your infrastructure code:

```plaintext
.
├── lib
│   ├── my-construct.api.ts # Lambda handler for API
│   ├── my-construct.auth.ts # Lambda handler for Auth
│   └── my-construct.ts # CDK construct with two Lambda functions
├── package-lock.json # single lock file
├── package.json # CDK and runtime dependencies defined in a single package.json
└── tsconfig.json
```

By default, the construct will use the name of the defining file and the construct's
id to look up the entry file. In `my-construct.ts` above we have:

```python
# automatic entry look up
api_handler = nodejs.NodejsFunction(self, "api")
auth_handler = nodejs.NodejsFunction(self, "auth")
```

Alternatively, an entry file and handler can be specified:

```python
nodejs.NodejsFunction(self, "MyFunction",
    entry="/path/to/my/file.ts",  # accepts .js, .jsx, .cjs, .mjs, .ts, .tsx, .cts and .mts files
    handler="myExportedFunc"
)
```

The handler value will be automatically prefixed with the bundled output file name, `index.`,
unless the handler value contains a `.` character, in which case the handler value is used as-is to
allow for values needed by some Lambda extensions.

For monorepos, the reference architecture becomes:

```plaintext
.
├── packages
│   ├── cool-package
│   │   ├── lib
│   │   │   ├── cool-construct.api.ts
│   │   │   ├── cool-construct.auth.ts
│   │   │   └── cool-construct.ts
│   │   ├── package.json # CDK and runtime dependencies for cool-package
│   │   └── tsconfig.json
│   └── super-package
│       ├── lib
│       │   ├── super-construct.handler.ts
│       │   └── super-construct.ts
│       ├── package.json # CDK and runtime dependencies for super-package
│       └── tsconfig.json
├── package-lock.json # single lock file
├── package.json # root dependencies
└── tsconfig.json
```

## Customizing the underlying Lambda function

All properties of `lambda.Function` can be used to customize the underlying `lambda.Function`.

See also the [AWS Lambda construct library](https://github.com/aws/aws-cdk/tree/main/packages/aws-cdk-lib/aws-lambda).

The `NodejsFunction` construct automatically [reuses existing connections](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/node-reusing-connections.html)
when working with the AWS SDK v2 for JavaScript. Set the `awsSdkConnectionReuse` prop to `false` to disable it.

The AWS SDK v3 for JavaScript does not include the environment variable set by `awsSdkConnectionReuse`. See [this guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-reusing-connections.html) for information about reusing connections. Therefore, for runtimes >= Node 18, which include SDK v3, the prop defaults to `false`, and must be explicitly set to `true` in order for the environment variable to be set.

## Runtime

When the `@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion` feature flag is enabled, the `NODEJS_LATEST` runtime
will be used by default. This runtime will be updated to use the latest Node.js version currently available in lambda.
Since this runtime can change from version to version, you should ensure that all of your dependencies are included
during packaging and avoid relying on depdendencies being globally installed. See [externals](#externals) for details.

**When using `NODEJS_LATEST` runtime make sure that all of your dependencies are included during bundling, or as layers.
Usage of globally installed packages in the lambda environment may cause your function to break in future versions. If
you need to rely on packages pre-installed in the lambda environment, you must explicitly set your runtime.**

This can be set via `lambda.Runtime`:

```python
from aws_cdk.aws_lambda import Runtime


nodejs.NodejsFunction(self, "my-function",
    runtime=Runtime.NODEJS_18_X
)
```

With the `@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion` disabled, the runtime will default to `NODEJ_16_X`.

## Lock file

The `NodejsFunction` requires a dependencies lock file (`yarn.lock`, `pnpm-lock.yaml` or
`package-lock.json`). When bundling in a Docker container, the path containing this lock file is
used as the source (`/asset-input`) for the volume mounted in the container.

By default, the construct will try to automatically determine your project lock file.
Alternatively, you can specify the `depsLockFilePath` prop manually. In this
case you need to ensure that this path includes `entry` and any module/dependencies
used by your function. Otherwise bundling will fail.

## Local bundling

If `esbuild` is available it will be used to bundle your code in your environment. Otherwise,
bundling will happen in a [Lambda compatible Docker container](https://gallery.ecr.aws/sam/build-nodejs18.x)
with the Docker platform based on the target architecture of the Lambda function.

For macOS the recommended approach is to install `esbuild` as Docker volume performance is really poor.

`esbuild` can be installed with:

```console
$ npm install --save-dev esbuild@0
```

OR

```console
$ yarn add --dev esbuild@0
```

If you're using a monorepo layout, the `esbuild` dependency needs to be installed in the "root" `package.json` file,
not in the workspace. From the reference architecture described [above](#reference-project-architecture), the `esbuild`
dev dependency needs to be in `./package.json`, not `packages/cool-package/package.json` or
`packages/super-package/package.json`.

To force bundling in a Docker container even if `esbuild` is available in your environment,
set `bundling.forceDockerBundling` to `true`. This is useful if your function relies on node
modules that should be installed (`nodeModules` prop, see [below](#install-modules)) in a Lambda
compatible environment. This is usually the case with modules using native dependencies.

## Working with modules

### Externals

When the `NODEJS_LATEST` runtime is used, no modules are excluded from bundling by default. This is because the runtime
will change as new NodeJs versions become available in lambda, which may change what packages are vended as part of the
environment.

When passing a runtime that is known to include a version of the aws sdk, it will be excluded by default. For example, when
passing `NODEJS_16_X`, `aws-sdk` is excluded. When passing `NODEJS_18_X`,  all `@aws-sdk/*` packages are excluded.

> [!WARNING]
> The NodeJS runtime of Node 16 will be deprecated by Lambda on June 12, 2024. Lambda runtimes Node 18 and higher include SDKv3 and not SDKv2. Updating your Lambda runtime from <=Node 16 to any newer version will require bundling the SDK with your handler code, or updating all SDK calls in your handler code to use SDKv3 (which is not a trivial update). Please account for this added complexity and update as soon as possible.

This can be configured by specifying `bundling.externalModules`:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        external_modules=["@aws-sdk/*", "cool-module"
        ]
    )
)
```

Includes AWS SDK in the bundle asset by setting `bundleAwsSDK` to `true`. This will be essentially exclude sdk from the external
module and not be resolved to the Lambda provided sdk.

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        bundle_aws_sDK=True
    )
)
```

### Install modules

By default, all node modules referenced in your Lambda code will be bundled by `esbuild`.
Use the `nodeModules` prop under `bundling` to specify a list of modules that should not be
bundled but instead included in the `node_modules` folder of the Lambda package. This is useful
when working with native dependencies or when `esbuild` fails to bundle a module.

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        node_modules=["native-module", "other-module"]
    )
)
```

The modules listed in `nodeModules` must be present in the `package.json`'s dependencies or
installed. The same version will be used for installation. The lock file (`yarn.lock`,
`pnpm-lock.yaml` or `package-lock.json`) will be used along with the right installer (`yarn`,
`pnpm` or `npm`).

When working with `nodeModules` using native dependencies, you might want to force bundling in a
Docker container even if `esbuild` is available in your environment. This can be done by setting
`bundling.forceDockerBundling` to `true`.

## Configuring `esbuild`

The `NodejsFunction` construct exposes [esbuild options](https://esbuild.github.io/api/#build-api)
via properties under `bundling`:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        minify=True,  # minify code, defaults to false
        source_map=True,  # include source map, defaults to false
        source_map_mode=nodejs.SourceMapMode.INLINE,  # defaults to SourceMapMode.DEFAULT
        sources_content=False,  # do not include original source into source map, defaults to true
        target="es2020",  # target environment for the generated JavaScript code
        loader={ # Use the 'dataurl' loader for '.png' files
            ".png": "dataurl"},
        define={ # Replace strings during build time
            "process.env.API_KEY": JSON.stringify("xxx-xxxx-xxx"),
            "process.env.PRODUCTION": JSON.stringify(True),
            "process.env.NUMBER": JSON.stringify(123)},
        log_level=nodejs.LogLevel.ERROR,  # defaults to LogLevel.WARNING
        keep_names=True,  # defaults to false
        tsconfig="custom-tsconfig.json",  # use custom-tsconfig.json instead of default,
        metafile=True,  # include meta file, defaults to false
        banner="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
        footer="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
        charset=nodejs.Charset.UTF8,  # do not escape non-ASCII characters, defaults to Charset.ASCII
        format=nodejs.OutputFormat.ESM,  # ECMAScript module output format, defaults to OutputFormat.CJS (OutputFormat.ESM requires Node.js >= 14)
        main_fields=["module", "main"],  # prefer ECMAScript versions of dependencies
        inject=["./my-shim.js", "./other-shim.js"],  # allows to automatically replace a global variable with an import from another file
        esbuild_args={ # Pass additional arguments to esbuild
            "--log-limit": "0",
            "--splitting": True}
    )
)
```

## Command hooks

It is possible to run additional commands by specifying the `commandHooks` prop:

```text
// This example only available in TypeScript
// Run additional props via `commandHooks`
new nodejs.NodejsFunction(this, 'my-handler-with-commands', {
  bundling: {
    commandHooks: {
      beforeBundling(inputDir: string, outputDir: string): string[] {
        return [
          `echo hello > ${inputDir}/a.txt`,
          `cp ${inputDir}/a.txt ${outputDir}`,
        ];
      },
      afterBundling(inputDir: string, outputDir: string): string[] {
        return [`cp ${inputDir}/b.txt ${outputDir}/txt`];
      },
      beforeInstall() {
        return [];
      },
      // ...
    },
    // ...
  },
});
```

The following hooks are available:

* `beforeBundling`: runs before all bundling commands
* `beforeInstall`: runs before node modules installation
* `afterBundling`: runs after all bundling commands

They all receive the directory containing the lock file (`inputDir`) and the
directory where the bundled asset will be output (`outputDir`). They must return
an array of commands to run. Commands are chained with `&&`.

The commands will run in the environment in which bundling occurs: inside the
container for Docker bundling or on the host OS for local bundling.

## Pre Compilation with TSC

In some cases, `esbuild` may not yet support some newer features of the typescript language, such as,
[`emitDecoratorMetadata`](https://www.typescriptlang.org/tsconfig#emitDecoratorMetadata).
In such cases, it is possible to run pre-compilation using `tsc` by setting the `preCompilation` flag.

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        pre_compilation=True
    )
)
```

Note: A [`tsconfig.json` file](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) is required

## Customizing Docker bundling

Use `bundling.environment` to define environments variables when `esbuild` runs:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        environment={
            "NODE_ENV": "production"
        }
    )
)
```

Use `bundling.buildArgs` to pass build arguments when building the Docker bundling image:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        build_args={
            "HTTPS_PROXY": "https://127.0.0.1:3001"
        }
    )
)
```

Use `bundling.dockerImage` to use a custom Docker bundling image:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        docker_image=DockerImage.from_build("/path/to/Dockerfile")
    )
)
```

This image should have `esbuild` installed **globally**. If you plan to use `nodeModules` it
should also have `npm`, `yarn` or `pnpm` depending on the lock file you're using.

Use the [default image provided by `aws-cdk-lib/aws-lambda-nodejs`](https://github.com/aws/aws-cdk/blob/main/packages/aws-cdk-lib/aws-lambda-nodejs/lib/Dockerfile)
as a source of inspiration.

You can set additional Docker options to configure the build environment:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        network="host",
        security_opt="no-new-privileges",
        user="user:group",
        volumes_from=["777f7dc92da7"],
        volumes=[DockerVolume(host_path="/host-path", container_path="/container-path")]
    )
)
```

## Asset hash

By default the asset hash will be calculated based on the bundled output (`AssetHashType.OUTPUT`).

Use the `assetHash` prop to pass a custom hash:

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        asset_hash="my-custom-hash"
    )
)
```

If you chose to customize the hash, you will need to make sure it is updated every time the asset
changes, or otherwise it is possible that some deployments will not be invalidated.

## Docker based bundling in complex Docker configurations

By default the input and output of Docker based bundling is handled via bind mounts.
In situtations where this does not work, like Docker-in-Docker setups or when using a remote Docker socket, you can configure an alternative, but slower, variant that also works in these situations.

```python
nodejs.NodejsFunction(self, "my-handler",
    bundling=nodejs.BundlingOptions(
        bundling_file_access=BundlingFileAccess.VOLUME_COPY
    )
)
```

## Running a custom build script as part of cdk synthesis

If you need more control over bundling -- or the build process in general -- then we include the ability to invoke your own build script. For example, if you have the following `build.mjs` file:

```
import * as path from 'path';
import { fileURLToPath } from 'url';
import esbuild from "esbuild";
import { cache } from "esbuild-plugin-cache";
import time from "esbuild-plugin-time";

const __filename = fileURLToPath(import.meta.url); // get the resolved path to the file
const __dirname = path.dirname(__filename); // get the name of the directory

await esbuild
  .build({
    entryPoints: [path.join(__dirname, 'handler', 'index.ts')],
    outfile: path.join(__dirname, 'build-output', 'index.js'),
    external: ['@aws-sdk/*', 'aws-sdk'],
    format: 'cjs',
    platform: 'node',
    target: 'node18',
    bundle: true,
    minify: true,
    plugins: [time(), cache({ directory: ".cache" })],
  })
  .catch((error) => {
    console.log(error);
    process.exit(1)
  });
```

then you could use `build.mjs` in a cdk construct as follows:

```
export class ExampleStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const pathToBuildFile = path.join(__dirname, 'build.mjs');

    // assuming the `handler` property is specified as 'index.handler' (as in this example), then
    // this 'build-output' directory must contain an index.js file with an exported `handler` function.
    const pathToOutputFile = path.join(__dirname, 'build-output');
    const handler = 'index.handler';

    const commandThatIsRanDuringCdkSynth = ['node', pathToBuildFile];
    const code = lambda.Code.fromCustomCommand(
      pathToOutputFile,
      commandThatIsRanDuringCdkSynth,
    );

    new nodejs.NodejsFunction(this, 'NodejsFunctionBuild', {
      code,
      handler,
    });
  }
}
```

where the `build-output` would be a directory that contains an `index.js` file with an exported `handler` function.
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
    BundlingFileAccess as _BundlingFileAccess_281370cc,
    DockerImage as _DockerImage_f97a0c12,
    DockerRunOptions as _DockerRunOptions_81583d32,
    DockerVolume as _DockerVolume_849485b7,
    Duration as _Duration_4839e8c3,
    Size as _Size_7b441c34,
)
from ..aws_codeguruprofiler import IProfilingGroup as _IProfilingGroup_0bba72c4
from ..aws_ec2 import (
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import (
    IRole as _IRole_235f5d8e, PolicyStatement as _PolicyStatement_0fe33853
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import (
    AdotInstrumentationConfig as _AdotInstrumentationConfig_7c38d65d,
    ApplicationLogLevel as _ApplicationLogLevel_cd92660a,
    Architecture as _Architecture_12d5a53f,
    Code as _Code_7848f942,
    FileSystem as _FileSystem_a5fa005d,
    Function as _Function_244f85d8,
    FunctionOptions as _FunctionOptions_328f4d39,
    ICodeSigningConfig as _ICodeSigningConfig_edb41d1f,
    IDestination as _IDestination_40f19de4,
    IEventSource as _IEventSource_3686b3f8,
    ILayerVersion as _ILayerVersion_5ac127c8,
    LambdaInsightsVersion as _LambdaInsightsVersion_9dfbfef9,
    LogRetentionRetryOptions as _LogRetentionRetryOptions_ad797a7a,
    LoggingFormat as _LoggingFormat_30be8e01,
    ParamsAndSecretsLayerVersion as _ParamsAndSecretsLayerVersion_dce97f06,
    Runtime as _Runtime_b4eaa844,
    RuntimeManagementMode as _RuntimeManagementMode_688c173b,
    SnapStartConf as _SnapStartConf_2ffaa769,
    SystemLogLevel as _SystemLogLevel_aea49dc2,
    Tracing as _Tracing_9fe8e2bb,
    VersionOptions as _VersionOptions_981bb3c0,
)
from ..aws_logs import (
    ILogGroup as _ILogGroup_3c4fa718, RetentionDays as _RetentionDays_070f99f0
)
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_sqs import IQueue as _IQueue_7ed6f679


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lambda_nodejs.BundlingOptions",
    jsii_struct_bases=[_DockerRunOptions_81583d32],
    name_mapping={
        "command": "command",
        "entrypoint": "entrypoint",
        "environment": "environment",
        "network": "network",
        "platform": "platform",
        "security_opt": "securityOpt",
        "user": "user",
        "volumes": "volumes",
        "volumes_from": "volumesFrom",
        "working_directory": "workingDirectory",
        "asset_hash": "assetHash",
        "banner": "banner",
        "build_args": "buildArgs",
        "bundle_aws_sdk": "bundleAwsSDK",
        "bundling_file_access": "bundlingFileAccess",
        "charset": "charset",
        "command_hooks": "commandHooks",
        "define": "define",
        "docker_image": "dockerImage",
        "esbuild_args": "esbuildArgs",
        "esbuild_version": "esbuildVersion",
        "external_modules": "externalModules",
        "footer": "footer",
        "force_docker_bundling": "forceDockerBundling",
        "format": "format",
        "inject": "inject",
        "keep_names": "keepNames",
        "loader": "loader",
        "log_level": "logLevel",
        "main_fields": "mainFields",
        "metafile": "metafile",
        "minify": "minify",
        "node_modules": "nodeModules",
        "pre_compilation": "preCompilation",
        "source_map": "sourceMap",
        "source_map_mode": "sourceMapMode",
        "sources_content": "sourcesContent",
        "target": "target",
        "tsconfig": "tsconfig",
    },
)
class BundlingOptions(_DockerRunOptions_81583d32):
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_DockerVolume_849485b7, typing.Dict[builtins.str, typing.Any]]]] = None,
        volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        banner: typing.Optional[builtins.str] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        bundle_aws_sdk: typing.Optional[builtins.bool] = None,
        bundling_file_access: typing.Optional[_BundlingFileAccess_281370cc] = None,
        charset: typing.Optional["Charset"] = None,
        command_hooks: typing.Optional["ICommandHooks"] = None,
        define: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_image: typing.Optional[_DockerImage_f97a0c12] = None,
        esbuild_args: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]] = None,
        esbuild_version: typing.Optional[builtins.str] = None,
        external_modules: typing.Optional[typing.Sequence[builtins.str]] = None,
        footer: typing.Optional[builtins.str] = None,
        force_docker_bundling: typing.Optional[builtins.bool] = None,
        format: typing.Optional["OutputFormat"] = None,
        inject: typing.Optional[typing.Sequence[builtins.str]] = None,
        keep_names: typing.Optional[builtins.bool] = None,
        loader: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        log_level: typing.Optional["LogLevel"] = None,
        main_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        metafile: typing.Optional[builtins.bool] = None,
        minify: typing.Optional[builtins.bool] = None,
        node_modules: typing.Optional[typing.Sequence[builtins.str]] = None,
        pre_compilation: typing.Optional[builtins.bool] = None,
        source_map: typing.Optional[builtins.bool] = None,
        source_map_mode: typing.Optional["SourceMapMode"] = None,
        sources_content: typing.Optional[builtins.bool] = None,
        target: typing.Optional[builtins.str] = None,
        tsconfig: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Bundling options.

        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param network: Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_. Default: - no networking options
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Example value: ``linux/amd64`` Default: - no platform specified
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param volumes_from: Where to mount the specified volumes from. Default: - no containers are specified to mount volumes from
        :param working_directory: Working directory inside the container. Default: - image default
        :param asset_hash: Specify a custom hash for this asset. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - asset hash is calculated based on the bundled output
        :param banner: Use this to insert an arbitrary string at the beginning of generated JavaScript files. This is similar to footer which inserts at the end instead of the beginning. This is commonly used to insert comments: Default: - no comments are passed
        :param build_args: Build arguments to pass when building the bundling image. Default: - no build arguments are passed
        :param bundle_aws_sdk: Includes AWS SDK in the bundle asset. Default: - false if ``true`` the ``aws-sdk`` will be included in the asset bundle and not be resolved to the Lambda provided sdk.
        :param bundling_file_access: Which option to use to copy the source files to the docker container and output files back. Default: - BundlingFileAccess.BIND_MOUNT
        :param charset: The charset to use for esbuild's output. By default esbuild's output is ASCII-only. Any non-ASCII characters are escaped using backslash escape sequences. Using escape sequences makes the generated output slightly bigger, and also makes it harder to read. If you would like for esbuild to print the original characters without using escape sequences, use ``Charset.UTF8``. Default: Charset.ASCII
        :param command_hooks: Command hooks. Default: - do not run additional commands
        :param define: Replace global identifiers with constant expressions. For example, ``{ 'process.env.DEBUG': 'true' }``. Another example, ``{ 'process.env.API_KEY': JSON.stringify('xxx-xxxx-xxx') }``. Default: - no replacements are made
        :param docker_image: A custom bundling Docker image. This image should have esbuild installed globally. If you plan to use ``nodeModules`` it should also have ``npm``, ``yarn`` or ``pnpm`` depending on the lock file you're using. See https://github.com/aws/aws-cdk/blob/main/packages/aws-cdk-lib/aws-lambda-nodejs/lib/Dockerfile for the default image provided by aws-cdk-lib/aws-lambda-nodejs. Default: - use the Docker image provided by aws-cdk-lib/aws-lambda-nodejs
        :param esbuild_args: Build arguments to pass into esbuild. For example, to add the `--log-limit <https://esbuild.github.io/api/#log-limit>`_ flag:: new NodejsFunction(scope, id, { ... bundling: { esbuildArgs: { "--log-limit": "0", } } }); Default: - no additional esbuild arguments are passed
        :param esbuild_version: The version of esbuild to use when running in a Docker container. Default: - latest v0
        :param external_modules: A list of modules that should be considered as externals (already available in the runtime). Default: - no replacements are made
        :param footer: Use this to insert an arbitrary string at the end of generated JavaScript files. This is similar to banner which inserts at the beginning instead of the end. This is commonly used to insert comments Default: - no comments are passed
        :param force_docker_bundling: Force bundling in a Docker container even if local bundling is possible. This is useful if your function relies on node modules that should be installed (``nodeModules``) in a Lambda compatible environment. Default: false
        :param format: Output format for the generated JavaScript files. Default: OutputFormat.CJS
        :param inject: This option allows you to automatically replace a global variable with an import from another file. Default: - no code is injected
        :param keep_names: Whether to preserve the original ``name`` values even in minified code. In JavaScript the ``name`` property on functions and classes defaults to a nearby identifier in the source code. However, minification renames symbols to reduce code size and bundling sometimes need to rename symbols to avoid collisions. That changes value of the ``name`` property for many of these cases. This is usually fine because the ``name`` property is normally only used for debugging. However, some frameworks rely on the ``name`` property for registration and binding purposes. If this is the case, you can enable this option to preserve the original ``name`` values even in minified code. Default: false
        :param loader: Use loaders to change how a given input file is interpreted. Configuring a loader for a given file type lets you load that file type with an ``import`` statement or a ``require`` call. For example, ``{ '.png': 'dataurl' }``. Default: - use esbuild default loaders
        :param log_level: Log level for esbuild. This is also propagated to the package manager and applies to its specific install command. Default: LogLevel.WARNING
        :param main_fields: How to determine the entry point for modules. Try ['module', 'main'] to default to ES module versions. Default: []
        :param metafile: This option tells esbuild to write out a JSON file relative to output directory with metadata about the build. The metadata in this JSON file follows this schema (specified using TypeScript syntax):: { outputs: { [path: string]: { bytes: number inputs: { [path: string]: { bytesInOutput: number } } imports: { path: string }[] exports: string[] } } } This data can then be analyzed by other tools. For example, bundle buddy can consume esbuild's metadata format and generates a treemap visualization of the modules in your bundle and how much space each one takes up. Default: false
        :param minify: Whether to minify files when bundling. Default: false
        :param node_modules: A list of modules that should be installed instead of bundled. Modules are installed in a Lambda compatible environment only when bundling runs in Docker. Default: - all modules are bundled
        :param pre_compilation: Run compilation using tsc before running file through bundling step. This usually is not required unless you are using new experimental features that are only supported by typescript's ``tsc`` compiler. One example of such feature is ``emitDecoratorMetadata``. Default: false
        :param source_map: Whether to include source maps when bundling. Default: false
        :param source_map_mode: Source map mode to be used when bundling. Default: SourceMapMode.DEFAULT
        :param sources_content: Whether to include original source code in source maps when bundling. Default: true
        :param target: Target environment for the generated JavaScript code. Default: - the node version of the runtime
        :param tsconfig: Normally the esbuild automatically discovers ``tsconfig.json`` files and reads their contents during a build. However, you can also configure a custom ``tsconfig.json`` file to use instead. This is similar to entry path, you need to provide path to your custom ``tsconfig.json``. This can be useful if you need to do multiple builds of the same code with different settings. For example, ``{ 'tsconfig': 'path/custom.tsconfig.json' }``. Default: - automatically discovered by ``esbuild``

        :exampleMetadata: infused

        Example::

            nodejs.NodejsFunction(self, "my-handler",
                bundling=nodejs.BundlingOptions(
                    docker_image=DockerImage.from_build("/path/to/Dockerfile")
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8049cd6c8eb3542b1c20a2677da2bd64b4125320c114432030729ac28f71df41)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument security_opt", value=security_opt, expected_type=type_hints["security_opt"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument volumes_from", value=volumes_from, expected_type=type_hints["volumes_from"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
            check_type(argname="argument asset_hash", value=asset_hash, expected_type=type_hints["asset_hash"])
            check_type(argname="argument banner", value=banner, expected_type=type_hints["banner"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument bundle_aws_sdk", value=bundle_aws_sdk, expected_type=type_hints["bundle_aws_sdk"])
            check_type(argname="argument bundling_file_access", value=bundling_file_access, expected_type=type_hints["bundling_file_access"])
            check_type(argname="argument charset", value=charset, expected_type=type_hints["charset"])
            check_type(argname="argument command_hooks", value=command_hooks, expected_type=type_hints["command_hooks"])
            check_type(argname="argument define", value=define, expected_type=type_hints["define"])
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument esbuild_args", value=esbuild_args, expected_type=type_hints["esbuild_args"])
            check_type(argname="argument esbuild_version", value=esbuild_version, expected_type=type_hints["esbuild_version"])
            check_type(argname="argument external_modules", value=external_modules, expected_type=type_hints["external_modules"])
            check_type(argname="argument footer", value=footer, expected_type=type_hints["footer"])
            check_type(argname="argument force_docker_bundling", value=force_docker_bundling, expected_type=type_hints["force_docker_bundling"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument inject", value=inject, expected_type=type_hints["inject"])
            check_type(argname="argument keep_names", value=keep_names, expected_type=type_hints["keep_names"])
            check_type(argname="argument loader", value=loader, expected_type=type_hints["loader"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument main_fields", value=main_fields, expected_type=type_hints["main_fields"])
            check_type(argname="argument metafile", value=metafile, expected_type=type_hints["metafile"])
            check_type(argname="argument minify", value=minify, expected_type=type_hints["minify"])
            check_type(argname="argument node_modules", value=node_modules, expected_type=type_hints["node_modules"])
            check_type(argname="argument pre_compilation", value=pre_compilation, expected_type=type_hints["pre_compilation"])
            check_type(argname="argument source_map", value=source_map, expected_type=type_hints["source_map"])
            check_type(argname="argument source_map_mode", value=source_map_mode, expected_type=type_hints["source_map_mode"])
            check_type(argname="argument sources_content", value=sources_content, expected_type=type_hints["sources_content"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument tsconfig", value=tsconfig, expected_type=type_hints["tsconfig"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if environment is not None:
            self._values["environment"] = environment
        if network is not None:
            self._values["network"] = network
        if platform is not None:
            self._values["platform"] = platform
        if security_opt is not None:
            self._values["security_opt"] = security_opt
        if user is not None:
            self._values["user"] = user
        if volumes is not None:
            self._values["volumes"] = volumes
        if volumes_from is not None:
            self._values["volumes_from"] = volumes_from
        if working_directory is not None:
            self._values["working_directory"] = working_directory
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if banner is not None:
            self._values["banner"] = banner
        if build_args is not None:
            self._values["build_args"] = build_args
        if bundle_aws_sdk is not None:
            self._values["bundle_aws_sdk"] = bundle_aws_sdk
        if bundling_file_access is not None:
            self._values["bundling_file_access"] = bundling_file_access
        if charset is not None:
            self._values["charset"] = charset
        if command_hooks is not None:
            self._values["command_hooks"] = command_hooks
        if define is not None:
            self._values["define"] = define
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if esbuild_args is not None:
            self._values["esbuild_args"] = esbuild_args
        if esbuild_version is not None:
            self._values["esbuild_version"] = esbuild_version
        if external_modules is not None:
            self._values["external_modules"] = external_modules
        if footer is not None:
            self._values["footer"] = footer
        if force_docker_bundling is not None:
            self._values["force_docker_bundling"] = force_docker_bundling
        if format is not None:
            self._values["format"] = format
        if inject is not None:
            self._values["inject"] = inject
        if keep_names is not None:
            self._values["keep_names"] = keep_names
        if loader is not None:
            self._values["loader"] = loader
        if log_level is not None:
            self._values["log_level"] = log_level
        if main_fields is not None:
            self._values["main_fields"] = main_fields
        if metafile is not None:
            self._values["metafile"] = metafile
        if minify is not None:
            self._values["minify"] = minify
        if node_modules is not None:
            self._values["node_modules"] = node_modules
        if pre_compilation is not None:
            self._values["pre_compilation"] = pre_compilation
        if source_map is not None:
            self._values["source_map"] = source_map
        if source_map_mode is not None:
            self._values["source_map_mode"] = source_map_mode
        if sources_content is not None:
            self._values["sources_content"] = sources_content
        if target is not None:
            self._values["target"] = target
        if tsconfig is not None:
            self._values["tsconfig"] = tsconfig

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to run in the container.

        :default: - run the command defined in the image
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The entrypoint to run in the container.

        :default: - run the entrypoint defined in the image
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The environment variables to pass to the container.

        :default: - no environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_.

        :default: - no networking options
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*.

        Example value: ``linux/amd64``

        :default: - no platform specified
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_opt(self) -> typing.Optional[builtins.str]:
        '''`Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container.

        :default: - no security options
        '''
        result = self._values.get("security_opt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The user to use when running the container.

        :default: - root or image default
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[_DockerVolume_849485b7]]:
        '''Docker volumes to mount.

        :default: - no volumes are mounted
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[_DockerVolume_849485b7]], result)

    @builtins.property
    def volumes_from(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Where to mount the specified volumes from.

        :default: - no containers are specified to mount volumes from

        :see: https://docs.docker.com/engine/reference/commandline/run/#mount-volumes-from-container---volumes-from
        '''
        result = self._values.get("volumes_from")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Working directory inside the container.

        :default: - image default
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - asset hash is calculated based on the bundled output
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def banner(self) -> typing.Optional[builtins.str]:
        '''Use this to insert an arbitrary string at the beginning of generated JavaScript files.

        This is similar to footer which inserts at the end instead of the beginning.

        This is commonly used to insert comments:

        :default: - no comments are passed
        '''
        result = self._values.get("banner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build arguments to pass when building the bundling image.

        :default: - no build arguments are passed
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def bundle_aws_sdk(self) -> typing.Optional[builtins.bool]:
        '''Includes AWS SDK in the bundle asset.

        :default:

        - false
        if ``true`` the ``aws-sdk`` will be included in the asset bundle and not be
        resolved to the Lambda provided sdk.
        '''
        result = self._values.get("bundle_aws_sdk")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bundling_file_access(self) -> typing.Optional[_BundlingFileAccess_281370cc]:
        '''Which option to use to copy the source files to the docker container and output files back.

        :default: - BundlingFileAccess.BIND_MOUNT
        '''
        result = self._values.get("bundling_file_access")
        return typing.cast(typing.Optional[_BundlingFileAccess_281370cc], result)

    @builtins.property
    def charset(self) -> typing.Optional["Charset"]:
        '''The charset to use for esbuild's output.

        By default esbuild's output is ASCII-only. Any non-ASCII characters are escaped
        using backslash escape sequences. Using escape sequences makes the generated output
        slightly bigger, and also makes it harder to read. If you would like for esbuild to print
        the original characters without using escape sequences, use ``Charset.UTF8``.

        :default: Charset.ASCII

        :see: https://esbuild.github.io/api/#charset
        '''
        result = self._values.get("charset")
        return typing.cast(typing.Optional["Charset"], result)

    @builtins.property
    def command_hooks(self) -> typing.Optional["ICommandHooks"]:
        '''Command hooks.

        :default: - do not run additional commands
        '''
        result = self._values.get("command_hooks")
        return typing.cast(typing.Optional["ICommandHooks"], result)

    @builtins.property
    def define(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Replace global identifiers with constant expressions.

        For example, ``{ 'process.env.DEBUG': 'true' }``.

        Another example, ``{ 'process.env.API_KEY': JSON.stringify('xxx-xxxx-xxx') }``.

        :default: - no replacements are made
        '''
        result = self._values.get("define")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def docker_image(self) -> typing.Optional[_DockerImage_f97a0c12]:
        '''A custom bundling Docker image.

        This image should have esbuild installed globally. If you plan to use ``nodeModules``
        it should also have ``npm``, ``yarn`` or ``pnpm`` depending on the lock file you're using.

        See https://github.com/aws/aws-cdk/blob/main/packages/aws-cdk-lib/aws-lambda-nodejs/lib/Dockerfile
        for the default image provided by aws-cdk-lib/aws-lambda-nodejs.

        :default: - use the Docker image provided by aws-cdk-lib/aws-lambda-nodejs
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional[_DockerImage_f97a0c12], result)

    @builtins.property
    def esbuild_args(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]]:
        '''Build arguments to pass into esbuild.

        For example, to add the `--log-limit <https://esbuild.github.io/api/#log-limit>`_ flag::

           new NodejsFunction(scope, id, {
             ...
             bundling: {
               esbuildArgs: {
                 "--log-limit": "0",
               }
             }
           });

        :default: - no additional esbuild arguments are passed
        '''
        result = self._values.get("esbuild_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]], result)

    @builtins.property
    def esbuild_version(self) -> typing.Optional[builtins.str]:
        '''The version of esbuild to use when running in a Docker container.

        :default: - latest v0
        '''
        result = self._values.get("esbuild_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_modules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of modules that should be considered as externals (already available in the runtime).

        :default: - no replacements are made
        '''
        result = self._values.get("external_modules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def footer(self) -> typing.Optional[builtins.str]:
        '''Use this to insert an arbitrary string at the end of generated JavaScript files.

        This is similar to banner which inserts at the beginning instead of the end.

        This is commonly used to insert comments

        :default: - no comments are passed
        '''
        result = self._values.get("footer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_docker_bundling(self) -> typing.Optional[builtins.bool]:
        '''Force bundling in a Docker container even if local bundling is possible.

        This is useful if your function relies on node modules
        that should be installed (``nodeModules``) in a Lambda compatible
        environment.

        :default: false
        '''
        result = self._values.get("force_docker_bundling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def format(self) -> typing.Optional["OutputFormat"]:
        '''Output format for the generated JavaScript files.

        :default: OutputFormat.CJS
        '''
        result = self._values.get("format")
        return typing.cast(typing.Optional["OutputFormat"], result)

    @builtins.property
    def inject(self) -> typing.Optional[typing.List[builtins.str]]:
        '''This option allows you to automatically replace a global variable with an import from another file.

        :default: - no code is injected

        :see: https://esbuild.github.io/api/#inject
        '''
        result = self._values.get("inject")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def keep_names(self) -> typing.Optional[builtins.bool]:
        '''Whether to preserve the original ``name`` values even in minified code.

        In JavaScript the ``name`` property on functions and classes defaults to a
        nearby identifier in the source code.

        However, minification renames symbols to reduce code size and bundling
        sometimes need to rename symbols to avoid collisions. That changes value of
        the ``name`` property for many of these cases. This is usually fine because
        the ``name`` property is normally only used for debugging. However, some
        frameworks rely on the ``name`` property for registration and binding purposes.
        If this is the case, you can enable this option to preserve the original
        ``name`` values even in minified code.

        :default: false
        '''
        result = self._values.get("keep_names")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def loader(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Use loaders to change how a given input file is interpreted.

        Configuring a loader for a given file type lets you load that file type with
        an ``import`` statement or a ``require`` call.

        For example, ``{ '.png': 'dataurl' }``.

        :default: - use esbuild default loaders

        :see: https://esbuild.github.io/api/#loader
        '''
        result = self._values.get("loader")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def log_level(self) -> typing.Optional["LogLevel"]:
        '''Log level for esbuild.

        This is also propagated to the package manager and
        applies to its specific install command.

        :default: LogLevel.WARNING
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional["LogLevel"], result)

    @builtins.property
    def main_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''How to determine the entry point for modules.

        Try ['module', 'main'] to default to ES module versions.

        :default: []
        '''
        result = self._values.get("main_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metafile(self) -> typing.Optional[builtins.bool]:
        '''This option tells esbuild to write out a JSON file relative to output directory with metadata about the build.

        The metadata in this JSON file follows this schema (specified using TypeScript syntax)::

           {
             outputs: {
               [path: string]: {
                 bytes: number
                 inputs: {
                   [path: string]: { bytesInOutput: number }
                 }
                 imports: { path: string }[]
                 exports: string[]
               }
             }
           }

        This data can then be analyzed by other tools. For example,
        bundle buddy can consume esbuild's metadata format and generates a treemap visualization
        of the modules in your bundle and how much space each one takes up.

        :default: false

        :see: https://esbuild.github.io/api/#metafile
        '''
        result = self._values.get("metafile")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minify(self) -> typing.Optional[builtins.bool]:
        '''Whether to minify files when bundling.

        :default: false
        '''
        result = self._values.get("minify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def node_modules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of modules that should be installed instead of bundled.

        Modules are
        installed in a Lambda compatible environment only when bundling runs in
        Docker.

        :default: - all modules are bundled
        '''
        result = self._values.get("node_modules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def pre_compilation(self) -> typing.Optional[builtins.bool]:
        '''Run compilation using tsc before running file through bundling step.

        This usually is not required unless you are using new experimental features that
        are only supported by typescript's ``tsc`` compiler.
        One example of such feature is ``emitDecoratorMetadata``.

        :default: false
        '''
        result = self._values.get("pre_compilation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def source_map(self) -> typing.Optional[builtins.bool]:
        '''Whether to include source maps when bundling.

        :default: false
        '''
        result = self._values.get("source_map")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def source_map_mode(self) -> typing.Optional["SourceMapMode"]:
        '''Source map mode to be used when bundling.

        :default: SourceMapMode.DEFAULT

        :see: https://esbuild.github.io/api/#sourcemap
        '''
        result = self._values.get("source_map_mode")
        return typing.cast(typing.Optional["SourceMapMode"], result)

    @builtins.property
    def sources_content(self) -> typing.Optional[builtins.bool]:
        '''Whether to include original source code in source maps when bundling.

        :default: true

        :see: https://esbuild.github.io/api/#sources-content
        '''
        result = self._values.get("sources_content")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Target environment for the generated JavaScript code.

        :default: - the node version of the runtime

        :see: https://esbuild.github.io/api/#target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tsconfig(self) -> typing.Optional[builtins.str]:
        '''Normally the esbuild automatically discovers ``tsconfig.json`` files and reads their contents during a build.

        However, you can also configure a custom ``tsconfig.json`` file to use instead.

        This is similar to entry path, you need to provide path to your custom ``tsconfig.json``.

        This can be useful if you need to do multiple builds of the same code with different settings.

        For example, ``{ 'tsconfig': 'path/custom.tsconfig.json' }``.

        :default: - automatically discovered by ``esbuild``
        '''
        result = self._values.get("tsconfig")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BundlingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_lambda_nodejs.Charset")
class Charset(enum.Enum):
    '''Charset for esbuild's output.

    :exampleMetadata: infused

    Example::

        nodejs.NodejsFunction(self, "my-handler",
            bundling=nodejs.BundlingOptions(
                minify=True,  # minify code, defaults to false
                source_map=True,  # include source map, defaults to false
                source_map_mode=nodejs.SourceMapMode.INLINE,  # defaults to SourceMapMode.DEFAULT
                sources_content=False,  # do not include original source into source map, defaults to true
                target="es2020",  # target environment for the generated JavaScript code
                loader={ # Use the 'dataurl' loader for '.png' files
                    ".png": "dataurl"},
                define={ # Replace strings during build time
                    "process.env.API_KEY": JSON.stringify("xxx-xxxx-xxx"),
                    "process.env.PRODUCTION": JSON.stringify(True),
                    "process.env.NUMBER": JSON.stringify(123)},
                log_level=nodejs.LogLevel.ERROR,  # defaults to LogLevel.WARNING
                keep_names=True,  # defaults to false
                tsconfig="custom-tsconfig.json",  # use custom-tsconfig.json instead of default,
                metafile=True,  # include meta file, defaults to false
                banner="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                footer="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                charset=nodejs.Charset.UTF8,  # do not escape non-ASCII characters, defaults to Charset.ASCII
                format=nodejs.OutputFormat.ESM,  # ECMAScript module output format, defaults to OutputFormat.CJS (OutputFormat.ESM requires Node.js >= 14)
                main_fields=["module", "main"],  # prefer ECMAScript versions of dependencies
                inject=["./my-shim.js", "./other-shim.js"],  # allows to automatically replace a global variable with an import from another file
                esbuild_args={ # Pass additional arguments to esbuild
                    "--log-limit": "0",
                    "--splitting": True}
            )
        )
    '''

    ASCII = "ASCII"
    '''ASCII.

    Any non-ASCII characters are escaped using backslash escape sequences
    '''
    UTF8 = "UTF8"
    '''UTF-8.

    Keep original characters without using escape sequences
    '''


@jsii.interface(jsii_type="aws-cdk-lib.aws_lambda_nodejs.ICommandHooks")
class ICommandHooks(typing_extensions.Protocol):
    '''Command hooks.

    These commands will run in the environment in which bundling occurs: inside
    the container for Docker bundling or on the host OS for local bundling.

    Commands are chained with ``&&``.

    The following example (specified in TypeScript) copies a file from the input
    directory to the output directory to include it in the bundled asset::

       afterBundling(inputDir: string, outputDir: string): string[]{
         return [`cp ${inputDir}/my-binary.node ${outputDir}`];
       }
    '''

    @jsii.member(jsii_name="afterBundling")
    def after_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run after bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        ...

    @jsii.member(jsii_name="beforeBundling")
    def before_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run before bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        ...

    @jsii.member(jsii_name="beforeInstall")
    def before_install(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run before installing node modules.

        This hook only runs when node modules are installed.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        ...


class _ICommandHooksProxy:
    '''Command hooks.

    These commands will run in the environment in which bundling occurs: inside
    the container for Docker bundling or on the host OS for local bundling.

    Commands are chained with ``&&``.

    The following example (specified in TypeScript) copies a file from the input
    directory to the output directory to include it in the bundled asset::

       afterBundling(inputDir: string, outputDir: string): string[]{
         return [`cp ${inputDir}/my-binary.node ${outputDir}`];
       }
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_lambda_nodejs.ICommandHooks"

    @jsii.member(jsii_name="afterBundling")
    def after_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run after bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09dbe8bce258730fd8ac7ba62771c22efb44c7ebd8461cc5d827148a83bfe77d)
            check_type(argname="argument input_dir", value=input_dir, expected_type=type_hints["input_dir"])
            check_type(argname="argument output_dir", value=output_dir, expected_type=type_hints["output_dir"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "afterBundling", [input_dir, output_dir]))

    @jsii.member(jsii_name="beforeBundling")
    def before_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run before bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0964adbd439e9dc3679a84cd96429fd1e28a83b5f8007bff7046cb07e80d59f4)
            check_type(argname="argument input_dir", value=input_dir, expected_type=type_hints["input_dir"])
            check_type(argname="argument output_dir", value=output_dir, expected_type=type_hints["output_dir"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "beforeBundling", [input_dir, output_dir]))

    @jsii.member(jsii_name="beforeInstall")
    def before_install(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run before installing node modules.

        This hook only runs when node modules are installed.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__307f3bcc172246dc345479dc042e832516dc064777e3fa352640c4351101fa0d)
            check_type(argname="argument input_dir", value=input_dir, expected_type=type_hints["input_dir"])
            check_type(argname="argument output_dir", value=output_dir, expected_type=type_hints["output_dir"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "beforeInstall", [input_dir, output_dir]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICommandHooks).__jsii_proxy_class__ = lambda : _ICommandHooksProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_lambda_nodejs.LogLevel")
class LogLevel(enum.Enum):
    '''Log levels for esbuild and package managers' install commands.

    :exampleMetadata: infused

    Example::

        nodejs.NodejsFunction(self, "my-handler",
            bundling=nodejs.BundlingOptions(
                minify=True,  # minify code, defaults to false
                source_map=True,  # include source map, defaults to false
                source_map_mode=nodejs.SourceMapMode.INLINE,  # defaults to SourceMapMode.DEFAULT
                sources_content=False,  # do not include original source into source map, defaults to true
                target="es2020",  # target environment for the generated JavaScript code
                loader={ # Use the 'dataurl' loader for '.png' files
                    ".png": "dataurl"},
                define={ # Replace strings during build time
                    "process.env.API_KEY": JSON.stringify("xxx-xxxx-xxx"),
                    "process.env.PRODUCTION": JSON.stringify(True),
                    "process.env.NUMBER": JSON.stringify(123)},
                log_level=nodejs.LogLevel.ERROR,  # defaults to LogLevel.WARNING
                keep_names=True,  # defaults to false
                tsconfig="custom-tsconfig.json",  # use custom-tsconfig.json instead of default,
                metafile=True,  # include meta file, defaults to false
                banner="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                footer="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                charset=nodejs.Charset.UTF8,  # do not escape non-ASCII characters, defaults to Charset.ASCII
                format=nodejs.OutputFormat.ESM,  # ECMAScript module output format, defaults to OutputFormat.CJS (OutputFormat.ESM requires Node.js >= 14)
                main_fields=["module", "main"],  # prefer ECMAScript versions of dependencies
                inject=["./my-shim.js", "./other-shim.js"],  # allows to automatically replace a global variable with an import from another file
                esbuild_args={ # Pass additional arguments to esbuild
                    "--log-limit": "0",
                    "--splitting": True}
            )
        )
    '''

    VERBOSE = "VERBOSE"
    '''Show everything.'''
    DEBUG = "DEBUG"
    '''Show everything from info and some additional messages for debugging.'''
    INFO = "INFO"
    '''Show warnings, errors, and an output file summary.'''
    WARNING = "WARNING"
    '''Show warnings and errors.'''
    ERROR = "ERROR"
    '''Show errors only.'''
    SILENT = "SILENT"
    '''Show nothing.'''


class NodejsFunction(
    _Function_244f85d8,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lambda_nodejs.NodejsFunction",
):
    '''A Node.js Lambda function bundled using esbuild.

    :exampleMetadata: infused

    Example::

        nodejs.NodejsFunction(self, "my-handler",
            bundling=nodejs.BundlingOptions(
                network="host",
                security_opt="no-new-privileges",
                user="user:group",
                volumes_from=["777f7dc92da7"],
                volumes=[DockerVolume(host_path="/host-path", container_path="/container-path")]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        aws_sdk_connection_reuse: typing.Optional[builtins.bool] = None,
        bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[_Code_7848f942] = None,
        deps_lock_file_path: typing.Optional[builtins.str] = None,
        entry: typing.Optional[builtins.str] = None,
        handler: typing.Optional[builtins.str] = None,
        project_root: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[_Runtime_b4eaa844] = None,
        adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        application_log_level: typing.Optional[builtins.str] = None,
        application_log_level_v2: typing.Optional[_ApplicationLogLevel_cd92660a] = None,
        architecture: typing.Optional[_Architecture_12d5a53f] = None,
        code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
        current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_5f11635f] = None,
        ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
        events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
        filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
        ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
        layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
        log_format: typing.Optional[builtins.str] = None,
        logging_format: typing.Optional[_LoggingFormat_30be8e01] = None,
        log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        snap_start: typing.Optional[_SnapStartConf_2ffaa769] = None,
        system_log_level: typing.Optional[builtins.str] = None,
        system_log_level_v2: typing.Optional[_SystemLogLevel_aea49dc2] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IDestination_40f19de4] = None,
        on_success: typing.Optional[_IDestination_40f19de4] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param aws_sdk_connection_reuse: The ``AWS_NODEJS_CONNECTION_REUSE_ENABLED`` environment variable does not exist in the AWS SDK for JavaScript v3. This prop will be deprecated when the Lambda Node16 runtime is deprecated on June 12, 2024. See https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy Info for Node 16 runtimes / SDK v2 users: Whether to automatically reuse TCP connections when working with the AWS SDK for JavaScript v2. This sets the ``AWS_NODEJS_CONNECTION_REUSE_ENABLED`` environment variable to ``1``. Default: - false (obsolete) for runtimes >= Node 18, true for runtimes <= Node 16.
        :param bundling: Bundling options. Default: - use default bundling options: no minify, no sourcemap, all modules are bundled.
        :param code: The code that will be deployed to the Lambda Handler. If included, then properties related to bundling of the code are ignored. - If the ``code`` field is specified, then you must include the ``handler`` property. Default: - the code is bundled by esbuild
        :param deps_lock_file_path: The path to the dependencies lock file (``yarn.lock``, ``pnpm-lock.yaml`` or ``package-lock.json``). This will be used as the source for the volume mounted in the Docker container. Modules specified in ``nodeModules`` will be installed using the right installer (``yarn``, ``pnpm`` or ``npm``) along with this lock file. Default: - the path is found by walking up parent directories searching for a ``yarn.lock``, ``pnpm-lock.yaml`` or ``package-lock.json`` file
        :param entry: Path to the entry file (JavaScript or TypeScript). Default: - Derived from the name of the defining file and the construct's id. If the ``NodejsFunction`` is defined in ``stack.ts`` with ``my-handler`` as id (``new NodejsFunction(this, 'my-handler')``), the construct will look at ``stack.my-handler.ts`` and ``stack.my-handler.js``.
        :param handler: The name of the exported handler in the entry file. - If the ``code`` property is supplied, then you must include the ``handler`` property. The handler should be the name of the file that contains the exported handler and the function that should be called when the AWS Lambda is invoked. For example, if you had a file called ``myLambda.js`` and the function to be invoked was ``myHandler``, then you should input ``handler`` property as ``myLambda.myHandler``. - If the ``code`` property is not supplied and the handler input does not contain a ``.``, then the handler is prefixed with ``index.`` (index period). Otherwise, the handler property is not modified. Default: handler
        :param project_root: The path to the directory containing project config files (``package.json`` or ``tsconfig.json``). Default: - the directory containing the ``depsLockFilePath``
        :param runtime: The runtime environment. Only runtimes of the Node.js family are supported. Default: ``Runtime.NODEJS_LATEST`` if the ``@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion`` feature flag is enabled, otherwise ``Runtime.NODEJS_16_X``
        :param adot_instrumentation: Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation. Default: - No ADOT instrumentation
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set. Instead, configure ``allowAllOutbound`` directly on the security group. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param application_log_level: (deprecated) Sets the application log level for the function. Default: "INFO"
        :param application_log_level_v2: Sets the application log level for the function. Default: ApplicationLogLevel.INFO
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param ipv6_allowed_for_dual_stack: Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets. Only used if 'vpc' is supplied. Default: false
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_format: (deprecated) Sets the logFormat for the function. Default: "Text"
        :param logging_format: Sets the loggingFormat for the function. Default: LoggingFormat.TEXT
        :param log_group: The log group the function sends logs to. By default, Lambda functions send logs to an automatically created default log group named /aws/lambda/<function name>. However you cannot change the properties of this auto-created log group using the AWS CDK, e.g. you cannot set a different log retention. Use the ``logGroup`` property to create a fully customizable LogGroup ahead of time, and instruct the Lambda function to send logs to it. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: ``/aws/lambda/${this.functionName}`` - default log group created by Lambda
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. This is a legacy API and we strongly recommend you move away from it if you can. Instead create a fully customizable log group with ``logs.LogGroup`` and use the ``logGroup`` property to instruct the Lambda function to send logs to it. Migrating from ``logRetention`` to ``logGroup`` will cause the name of the log group to change. Users and code and referencing the name verbatim will have to adjust. In AWS CDK code, you can access the log group name directly from the LogGroup construct:: import * as logs from 'aws-cdk-lib/aws-logs'; declare const myLogGroup: logs.LogGroup; myLogGroup.logGroupName; Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param params_and_secrets: Specify the configuration of Parameters and Secrets Extension. Default: - No Parameters and Secrets Extension
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param runtime_management_mode: Sets the runtime management configuration for a function's version. Default: Auto
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param snap_start: Enable SnapStart for Lambda Function. SnapStart is currently supported only for Java 11, 17 runtime Default: - No snapstart
        :param system_log_level: (deprecated) Sets the system log level for the function. Default: "INFO"
        :param system_log_level_v2: Sets the system log level for the function. Default: SystemLogLevel.INFO
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece177829b26ef102d4080d730f168e29d7d310d1518738839cd3fc822c258fb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NodejsFunctionProps(
            aws_sdk_connection_reuse=aws_sdk_connection_reuse,
            bundling=bundling,
            code=code,
            deps_lock_file_path=deps_lock_file_path,
            entry=entry,
            handler=handler,
            project_root=project_root,
            runtime=runtime,
            adot_instrumentation=adot_instrumentation,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            application_log_level=application_log_level,
            application_log_level_v2=application_log_level_v2,
            architecture=architecture,
            code_signing_config=code_signing_config,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            dead_letter_topic=dead_letter_topic,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            ephemeral_storage_size=ephemeral_storage_size,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            insights_version=insights_version,
            ipv6_allowed_for_dual_stack=ipv6_allowed_for_dual_stack,
            layers=layers,
            log_format=log_format,
            logging_format=logging_format,
            log_group=log_group,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            params_and_secrets=params_and_secrets,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            runtime_management_mode=runtime_management_mode,
            security_groups=security_groups,
            snap_start=snap_start,
            system_log_level=system_log_level,
            system_log_level_v2=system_log_level_v2,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lambda_nodejs.NodejsFunctionProps",
    jsii_struct_bases=[_FunctionOptions_328f4d39],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "adot_instrumentation": "adotInstrumentation",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "application_log_level": "applicationLogLevel",
        "application_log_level_v2": "applicationLogLevelV2",
        "architecture": "architecture",
        "code_signing_config": "codeSigningConfig",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "dead_letter_topic": "deadLetterTopic",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "insights_version": "insightsVersion",
        "ipv6_allowed_for_dual_stack": "ipv6AllowedForDualStack",
        "layers": "layers",
        "log_format": "logFormat",
        "logging_format": "loggingFormat",
        "log_group": "logGroup",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "params_and_secrets": "paramsAndSecrets",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "runtime_management_mode": "runtimeManagementMode",
        "security_groups": "securityGroups",
        "snap_start": "snapStart",
        "system_log_level": "systemLogLevel",
        "system_log_level_v2": "systemLogLevelV2",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "aws_sdk_connection_reuse": "awsSdkConnectionReuse",
        "bundling": "bundling",
        "code": "code",
        "deps_lock_file_path": "depsLockFilePath",
        "entry": "entry",
        "handler": "handler",
        "project_root": "projectRoot",
        "runtime": "runtime",
    },
)
class NodejsFunctionProps(_FunctionOptions_328f4d39):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IDestination_40f19de4] = None,
        on_success: typing.Optional[_IDestination_40f19de4] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        application_log_level: typing.Optional[builtins.str] = None,
        application_log_level_v2: typing.Optional[_ApplicationLogLevel_cd92660a] = None,
        architecture: typing.Optional[_Architecture_12d5a53f] = None,
        code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
        current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_5f11635f] = None,
        ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
        events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
        filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
        ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
        layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
        log_format: typing.Optional[builtins.str] = None,
        logging_format: typing.Optional[_LoggingFormat_30be8e01] = None,
        log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        snap_start: typing.Optional[_SnapStartConf_2ffaa769] = None,
        system_log_level: typing.Optional[builtins.str] = None,
        system_log_level_v2: typing.Optional[_SystemLogLevel_aea49dc2] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        aws_sdk_connection_reuse: typing.Optional[builtins.bool] = None,
        bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[_Code_7848f942] = None,
        deps_lock_file_path: typing.Optional[builtins.str] = None,
        entry: typing.Optional[builtins.str] = None,
        handler: typing.Optional[builtins.str] = None,
        project_root: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[_Runtime_b4eaa844] = None,
    ) -> None:
        '''Properties for a NodejsFunction.

        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param adot_instrumentation: Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation. Default: - No ADOT instrumentation
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set. Instead, configure ``allowAllOutbound`` directly on the security group. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param application_log_level: (deprecated) Sets the application log level for the function. Default: "INFO"
        :param application_log_level_v2: Sets the application log level for the function. Default: ApplicationLogLevel.INFO
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param ipv6_allowed_for_dual_stack: Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets. Only used if 'vpc' is supplied. Default: false
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_format: (deprecated) Sets the logFormat for the function. Default: "Text"
        :param logging_format: Sets the loggingFormat for the function. Default: LoggingFormat.TEXT
        :param log_group: The log group the function sends logs to. By default, Lambda functions send logs to an automatically created default log group named /aws/lambda/<function name>. However you cannot change the properties of this auto-created log group using the AWS CDK, e.g. you cannot set a different log retention. Use the ``logGroup`` property to create a fully customizable LogGroup ahead of time, and instruct the Lambda function to send logs to it. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: ``/aws/lambda/${this.functionName}`` - default log group created by Lambda
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. This is a legacy API and we strongly recommend you move away from it if you can. Instead create a fully customizable log group with ``logs.LogGroup`` and use the ``logGroup`` property to instruct the Lambda function to send logs to it. Migrating from ``logRetention`` to ``logGroup`` will cause the name of the log group to change. Users and code and referencing the name verbatim will have to adjust. In AWS CDK code, you can access the log group name directly from the LogGroup construct:: import * as logs from 'aws-cdk-lib/aws-logs'; declare const myLogGroup: logs.LogGroup; myLogGroup.logGroupName; Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param params_and_secrets: Specify the configuration of Parameters and Secrets Extension. Default: - No Parameters and Secrets Extension
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param runtime_management_mode: Sets the runtime management configuration for a function's version. Default: Auto
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param snap_start: Enable SnapStart for Lambda Function. SnapStart is currently supported only for Java 11, 17 runtime Default: - No snapstart
        :param system_log_level: (deprecated) Sets the system log level for the function. Default: "INFO"
        :param system_log_level_v2: Sets the system log level for the function. Default: SystemLogLevel.INFO
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param aws_sdk_connection_reuse: The ``AWS_NODEJS_CONNECTION_REUSE_ENABLED`` environment variable does not exist in the AWS SDK for JavaScript v3. This prop will be deprecated when the Lambda Node16 runtime is deprecated on June 12, 2024. See https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy Info for Node 16 runtimes / SDK v2 users: Whether to automatically reuse TCP connections when working with the AWS SDK for JavaScript v2. This sets the ``AWS_NODEJS_CONNECTION_REUSE_ENABLED`` environment variable to ``1``. Default: - false (obsolete) for runtimes >= Node 18, true for runtimes <= Node 16.
        :param bundling: Bundling options. Default: - use default bundling options: no minify, no sourcemap, all modules are bundled.
        :param code: The code that will be deployed to the Lambda Handler. If included, then properties related to bundling of the code are ignored. - If the ``code`` field is specified, then you must include the ``handler`` property. Default: - the code is bundled by esbuild
        :param deps_lock_file_path: The path to the dependencies lock file (``yarn.lock``, ``pnpm-lock.yaml`` or ``package-lock.json``). This will be used as the source for the volume mounted in the Docker container. Modules specified in ``nodeModules`` will be installed using the right installer (``yarn``, ``pnpm`` or ``npm``) along with this lock file. Default: - the path is found by walking up parent directories searching for a ``yarn.lock``, ``pnpm-lock.yaml`` or ``package-lock.json`` file
        :param entry: Path to the entry file (JavaScript or TypeScript). Default: - Derived from the name of the defining file and the construct's id. If the ``NodejsFunction`` is defined in ``stack.ts`` with ``my-handler`` as id (``new NodejsFunction(this, 'my-handler')``), the construct will look at ``stack.my-handler.ts`` and ``stack.my-handler.js``.
        :param handler: The name of the exported handler in the entry file. - If the ``code`` property is supplied, then you must include the ``handler`` property. The handler should be the name of the file that contains the exported handler and the function that should be called when the AWS Lambda is invoked. For example, if you had a file called ``myLambda.js`` and the function to be invoked was ``myHandler``, then you should input ``handler`` property as ``myLambda.myHandler``. - If the ``code`` property is not supplied and the handler input does not contain a ``.``, then the handler is prefixed with ``index.`` (index period). Otherwise, the handler property is not modified. Default: handler
        :param project_root: The path to the directory containing project config files (``package.json`` or ``tsconfig.json``). Default: - the directory containing the ``depsLockFilePath``
        :param runtime: The runtime environment. Only runtimes of the Node.js family are supported. Default: ``Runtime.NODEJS_LATEST`` if the ``@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion`` feature flag is enabled, otherwise ``Runtime.NODEJS_16_X``

        :exampleMetadata: infused

        Example::

            nodejs.NodejsFunction(self, "my-handler",
                bundling=nodejs.BundlingOptions(
                    network="host",
                    security_opt="no-new-privileges",
                    user="user:group",
                    volumes_from=["777f7dc92da7"],
                    volumes=[DockerVolume(host_path="/host-path", container_path="/container-path")]
                )
            )
        '''
        if isinstance(adot_instrumentation, dict):
            adot_instrumentation = _AdotInstrumentationConfig_7c38d65d(**adot_instrumentation)
        if isinstance(current_version_options, dict):
            current_version_options = _VersionOptions_981bb3c0(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = _LogRetentionRetryOptions_ad797a7a(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if isinstance(bundling, dict):
            bundling = BundlingOptions(**bundling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2da45b394f0332be0f6d6b7468d9fb54961953d56265da69955d36ffa3481d33)
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument adot_instrumentation", value=adot_instrumentation, expected_type=type_hints["adot_instrumentation"])
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument application_log_level", value=application_log_level, expected_type=type_hints["application_log_level"])
            check_type(argname="argument application_log_level_v2", value=application_log_level_v2, expected_type=type_hints["application_log_level_v2"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument code_signing_config", value=code_signing_config, expected_type=type_hints["code_signing_config"])
            check_type(argname="argument current_version_options", value=current_version_options, expected_type=type_hints["current_version_options"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument dead_letter_queue_enabled", value=dead_letter_queue_enabled, expected_type=type_hints["dead_letter_queue_enabled"])
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument environment_encryption", value=environment_encryption, expected_type=type_hints["environment_encryption"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument initial_policy", value=initial_policy, expected_type=type_hints["initial_policy"])
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument ipv6_allowed_for_dual_stack", value=ipv6_allowed_for_dual_stack, expected_type=type_hints["ipv6_allowed_for_dual_stack"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument logging_format", value=logging_format, expected_type=type_hints["logging_format"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument params_and_secrets", value=params_and_secrets, expected_type=type_hints["params_and_secrets"])
            check_type(argname="argument profiling", value=profiling, expected_type=type_hints["profiling"])
            check_type(argname="argument profiling_group", value=profiling_group, expected_type=type_hints["profiling_group"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument runtime_management_mode", value=runtime_management_mode, expected_type=type_hints["runtime_management_mode"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument snap_start", value=snap_start, expected_type=type_hints["snap_start"])
            check_type(argname="argument system_log_level", value=system_log_level, expected_type=type_hints["system_log_level"])
            check_type(argname="argument system_log_level_v2", value=system_log_level_v2, expected_type=type_hints["system_log_level_v2"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument aws_sdk_connection_reuse", value=aws_sdk_connection_reuse, expected_type=type_hints["aws_sdk_connection_reuse"])
            check_type(argname="argument bundling", value=bundling, expected_type=type_hints["bundling"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument deps_lock_file_path", value=deps_lock_file_path, expected_type=type_hints["deps_lock_file_path"])
            check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument project_root", value=project_root, expected_type=type_hints["project_root"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if adot_instrumentation is not None:
            self._values["adot_instrumentation"] = adot_instrumentation
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if application_log_level is not None:
            self._values["application_log_level"] = application_log_level
        if application_log_level_v2 is not None:
            self._values["application_log_level_v2"] = application_log_level_v2
        if architecture is not None:
            self._values["architecture"] = architecture
        if code_signing_config is not None:
            self._values["code_signing_config"] = code_signing_config
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if insights_version is not None:
            self._values["insights_version"] = insights_version
        if ipv6_allowed_for_dual_stack is not None:
            self._values["ipv6_allowed_for_dual_stack"] = ipv6_allowed_for_dual_stack
        if layers is not None:
            self._values["layers"] = layers
        if log_format is not None:
            self._values["log_format"] = log_format
        if logging_format is not None:
            self._values["logging_format"] = logging_format
        if log_group is not None:
            self._values["log_group"] = log_group
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if params_and_secrets is not None:
            self._values["params_and_secrets"] = params_and_secrets
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if runtime_management_mode is not None:
            self._values["runtime_management_mode"] = runtime_management_mode
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if snap_start is not None:
            self._values["snap_start"] = snap_start
        if system_log_level is not None:
            self._values["system_log_level"] = system_log_level
        if system_log_level_v2 is not None:
            self._values["system_log_level_v2"] = system_log_level_v2
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if aws_sdk_connection_reuse is not None:
            self._values["aws_sdk_connection_reuse"] = aws_sdk_connection_reuse
        if bundling is not None:
            self._values["bundling"] = bundling
        if code is not None:
            self._values["code"] = code
        if deps_lock_file_path is not None:
            self._values["deps_lock_file_path"] = deps_lock_file_path
        if entry is not None:
            self._values["entry"] = entry
        if handler is not None:
            self._values["handler"] = handler
        if project_root is not None:
            self._values["project_root"] = project_root
        if runtime is not None:
            self._values["runtime"] = runtime

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def on_failure(self) -> typing.Optional[_IDestination_40f19de4]:
        '''The destination for failed invocations.

        :default: - no destination
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional[_IDestination_40f19de4], result)

    @builtins.property
    def on_success(self) -> typing.Optional[_IDestination_40f19de4]:
        '''The destination for successful invocations.

        :default: - no destination
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional[_IDestination_40f19de4], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def adot_instrumentation(
        self,
    ) -> typing.Optional[_AdotInstrumentationConfig_7c38d65d]:
        '''Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation.

        :default: - No ADOT instrumentation

        :see: https://aws-otel.github.io/docs/getting-started/lambda
        '''
        result = self._values.get("adot_instrumentation")
        return typing.cast(typing.Optional[_AdotInstrumentationConfig_7c38d65d], result)

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set.
        Instead, configure ``allowAllOutbound`` directly on the security group.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def application_log_level(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Sets the application log level for the function.

        :default: "INFO"

        :deprecated: Use ``applicationLogLevelV2`` as a property instead.

        :stability: deprecated
        '''
        result = self._values.get("application_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_log_level_v2(
        self,
    ) -> typing.Optional[_ApplicationLogLevel_cd92660a]:
        '''Sets the application log level for the function.

        :default: ApplicationLogLevel.INFO
        '''
        result = self._values.get("application_log_level_v2")
        return typing.cast(typing.Optional[_ApplicationLogLevel_cd92660a], result)

    @builtins.property
    def architecture(self) -> typing.Optional[_Architecture_12d5a53f]:
        '''The system architectures compatible with this lambda function.

        :default: Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[_Architecture_12d5a53f], result)

    @builtins.property
    def code_signing_config(self) -> typing.Optional[_ICodeSigningConfig_edb41d1f]:
        '''Code signing config associated with this function.

        :default: - Not Sign the Code
        '''
        result = self._values.get("code_signing_config")
        return typing.cast(typing.Optional[_ICodeSigningConfig_edb41d1f], result)

    @builtins.property
    def current_version_options(self) -> typing.Optional[_VersionOptions_981bb3c0]:
        '''Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``
        '''
        result = self._values.get("current_version_options")
        return typing.cast(typing.Optional[_VersionOptions_981bb3c0], result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to use if DLQ is enabled.

        If SNS topic is desired, specify ``deadLetterTopic`` property instead.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        '''
        result = self._values.get("dead_letter_queue_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''The SNS topic to use as a DLQ.

        Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created
        rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly.

        :default: - no SNS topic
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_IKey_5f11635f]:
        '''The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        '''
        result = self._values.get("environment_encryption")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The size of the function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[_IEventSource_3686b3f8]]:
        '''Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[_IEventSource_3686b3f8]], result)

    @builtins.property
    def filesystem(self) -> typing.Optional[_FileSystem_a5fa005d]:
        '''The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[_FileSystem_a5fa005d], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.
        '''
        result = self._values.get("initial_policy")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def insights_version(self) -> typing.Optional[_LambdaInsightsVersion_9dfbfef9]:
        '''Specify the version of CloudWatch Lambda insights to use for monitoring.

        :default: - No Lambda Insights

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html
        '''
        result = self._values.get("insights_version")
        return typing.cast(typing.Optional[_LambdaInsightsVersion_9dfbfef9], result)

    @builtins.property
    def ipv6_allowed_for_dual_stack(self) -> typing.Optional[builtins.bool]:
        '''Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets.

        Only used if 'vpc' is supplied.

        :default: false
        '''
        result = self._values.get("ipv6_allowed_for_dual_stack")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[_ILayerVersion_5ac127c8]]:
        '''A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by multiple functions.

        :default: - No layers.
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[_ILayerVersion_5ac127c8]], result)

    @builtins.property
    def log_format(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Sets the logFormat for the function.

        :default: "Text"

        :deprecated: Use ``loggingFormat`` as a property instead.

        :stability: deprecated
        '''
        result = self._values.get("log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_format(self) -> typing.Optional[_LoggingFormat_30be8e01]:
        '''Sets the loggingFormat for the function.

        :default: LoggingFormat.TEXT
        '''
        result = self._values.get("logging_format")
        return typing.cast(typing.Optional[_LoggingFormat_30be8e01], result)

    @builtins.property
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The log group the function sends logs to.

        By default, Lambda functions send logs to an automatically created default log group named /aws/lambda/.
        However you cannot change the properties of this auto-created log group using the AWS CDK, e.g. you cannot set a different log retention.

        Use the ``logGroup`` property to create a fully customizable LogGroup ahead of time, and instruct the Lambda function to send logs to it.

        Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16.
        If you are deploying to another type of region, please check regional availability first.

        :default: ``/aws/lambda/${this.functionName}`` - default log group created by Lambda
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        This is a legacy API and we strongly recommend you move away from it if you can.
        Instead create a fully customizable log group with ``logs.LogGroup`` and use the ``logGroup`` property
        to instruct the Lambda function to send logs to it.
        Migrating from ``logRetention`` to ``logGroup`` will cause the name of the log group to change.
        Users and code and referencing the name verbatim will have to adjust.

        In AWS CDK code, you can access the log group name directly from the LogGroup construct::

           import aws_cdk.aws_logs as logs

           # my_log_group: logs.LogGroup

           my_log_group.log_group_name

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[_LogRetentionRetryOptions_ad797a7a]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can.
        ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[_LogRetentionRetryOptions_ad797a7a], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can.
        ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def params_and_secrets(
        self,
    ) -> typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06]:
        '''Specify the configuration of Parameters and Secrets Extension.

        :default: - No Parameters and Secrets Extension

        :see: https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html
        '''
        result = self._values.get("params_and_secrets")
        return typing.cast(typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06], result)

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        '''Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profiling_group(self) -> typing.Optional[_IProfilingGroup_0bba72c4]:
        '''Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling_group")
        return typing.cast(typing.Optional[_IProfilingGroup_0bba72c4], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def runtime_management_mode(
        self,
    ) -> typing.Optional[_RuntimeManagementMode_688c173b]:
        '''Sets the runtime management configuration for a function's version.

        :default: Auto
        '''
        result = self._values.get("runtime_management_mode")
        return typing.cast(typing.Optional[_RuntimeManagementMode_688c173b], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def snap_start(self) -> typing.Optional[_SnapStartConf_2ffaa769]:
        '''Enable SnapStart for Lambda Function.

        SnapStart is currently supported only for Java 11, 17 runtime

        :default: - No snapstart
        '''
        result = self._values.get("snap_start")
        return typing.cast(typing.Optional[_SnapStartConf_2ffaa769], result)

    @builtins.property
    def system_log_level(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Sets the system log level for the function.

        :default: "INFO"

        :deprecated: Use ``systemLogLevelV2`` as a property instead.

        :stability: deprecated
        '''
        result = self._values.get("system_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def system_log_level_v2(self) -> typing.Optional[_SystemLogLevel_aea49dc2]:
        '''Sets the system log level for the function.

        :default: SystemLogLevel.INFO
        '''
        result = self._values.get("system_log_level_v2")
        return typing.cast(typing.Optional[_SystemLogLevel_aea49dc2], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def tracing(self) -> typing.Optional[_Tracing_9fe8e2bb]:
        '''Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[_Tracing_9fe8e2bb], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.
        This is required when ``vpcSubnets`` is specified.

        :default: - Function is not placed within a VPC.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Where to place the network interfaces within the VPC.

        This requires ``vpc`` to be specified in order for interfaces to actually be
        placed in the subnets. If ``vpc`` is not specify, this will raise an error.

        Note: Internet access for Lambda Functions requires a NAT Gateway, so picking
        public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``).

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def aws_sdk_connection_reuse(self) -> typing.Optional[builtins.bool]:
        '''The ``AWS_NODEJS_CONNECTION_REUSE_ENABLED`` environment variable does not exist in the AWS SDK for JavaScript v3.

        This prop will be deprecated when the Lambda Node16 runtime is deprecated on June 12, 2024.
        See https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy

        Info for Node 16 runtimes / SDK v2 users:

        Whether to automatically reuse TCP connections when working with the AWS
        SDK for JavaScript v2.

        This sets the ``AWS_NODEJS_CONNECTION_REUSE_ENABLED`` environment variable
        to ``1``.

        :default: - false (obsolete) for runtimes >= Node 18, true for runtimes <= Node 16.

        :see: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-reusing-connections.html
        '''
        result = self._values.get("aws_sdk_connection_reuse")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bundling(self) -> typing.Optional[BundlingOptions]:
        '''Bundling options.

        :default:

        - use default bundling options: no minify, no sourcemap, all
        modules are bundled.
        '''
        result = self._values.get("bundling")
        return typing.cast(typing.Optional[BundlingOptions], result)

    @builtins.property
    def code(self) -> typing.Optional[_Code_7848f942]:
        '''The code that will be deployed to the Lambda Handler.

        If included, then properties related to
        bundling of the code are ignored.

        - If the ``code`` field is specified, then you must include the ``handler`` property.

        :default: - the code is bundled by esbuild
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[_Code_7848f942], result)

    @builtins.property
    def deps_lock_file_path(self) -> typing.Optional[builtins.str]:
        '''The path to the dependencies lock file (``yarn.lock``, ``pnpm-lock.yaml`` or ``package-lock.json``).

        This will be used as the source for the volume mounted in the Docker
        container.

        Modules specified in ``nodeModules`` will be installed using the right
        installer (``yarn``, ``pnpm`` or ``npm``) along with this lock file.

        :default:

        - the path is found by walking up parent directories searching for
        a ``yarn.lock``, ``pnpm-lock.yaml`` or ``package-lock.json`` file
        '''
        result = self._values.get("deps_lock_file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entry(self) -> typing.Optional[builtins.str]:
        '''Path to the entry file (JavaScript or TypeScript).

        :default:

        - Derived from the name of the defining file and the construct's id.
        If the ``NodejsFunction`` is defined in ``stack.ts`` with ``my-handler`` as id
        (``new NodejsFunction(this, 'my-handler')``), the construct will look at ``stack.my-handler.ts``
        and ``stack.my-handler.js``.
        '''
        result = self._values.get("entry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def handler(self) -> typing.Optional[builtins.str]:
        '''The name of the exported handler in the entry file.

        - If the ``code`` property is supplied, then you must include the ``handler`` property. The handler should be the name of the file
          that contains the exported handler and the function that should be called when the AWS Lambda is invoked. For example, if
          you had a file called ``myLambda.js`` and the function to be invoked was ``myHandler``, then you should input ``handler`` property as ``myLambda.myHandler``.
        - If the ``code`` property is not supplied and the handler input does not contain a ``.``, then the handler is prefixed with ``index.`` (index period). Otherwise,
          the handler property is not modified.

        :default: handler
        '''
        result = self._values.get("handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_root(self) -> typing.Optional[builtins.str]:
        '''The path to the directory containing project config files (``package.json`` or ``tsconfig.json``).

        :default: - the directory containing the ``depsLockFilePath``
        '''
        result = self._values.get("project_root")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(self) -> typing.Optional[_Runtime_b4eaa844]:
        '''The runtime environment.

        Only runtimes of the Node.js family are
        supported.

        :default: ``Runtime.NODEJS_LATEST`` if the ``@aws-cdk/aws-lambda-nodejs:useLatestRuntimeVersion`` feature flag is enabled, otherwise ``Runtime.NODEJS_16_X``
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[_Runtime_b4eaa844], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodejsFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_lambda_nodejs.OutputFormat")
class OutputFormat(enum.Enum):
    '''Output format for the generated JavaScript files.

    :exampleMetadata: infused

    Example::

        nodejs.NodejsFunction(self, "my-handler",
            bundling=nodejs.BundlingOptions(
                minify=True,  # minify code, defaults to false
                source_map=True,  # include source map, defaults to false
                source_map_mode=nodejs.SourceMapMode.INLINE,  # defaults to SourceMapMode.DEFAULT
                sources_content=False,  # do not include original source into source map, defaults to true
                target="es2020",  # target environment for the generated JavaScript code
                loader={ # Use the 'dataurl' loader for '.png' files
                    ".png": "dataurl"},
                define={ # Replace strings during build time
                    "process.env.API_KEY": JSON.stringify("xxx-xxxx-xxx"),
                    "process.env.PRODUCTION": JSON.stringify(True),
                    "process.env.NUMBER": JSON.stringify(123)},
                log_level=nodejs.LogLevel.ERROR,  # defaults to LogLevel.WARNING
                keep_names=True,  # defaults to false
                tsconfig="custom-tsconfig.json",  # use custom-tsconfig.json instead of default,
                metafile=True,  # include meta file, defaults to false
                banner="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                footer="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                charset=nodejs.Charset.UTF8,  # do not escape non-ASCII characters, defaults to Charset.ASCII
                format=nodejs.OutputFormat.ESM,  # ECMAScript module output format, defaults to OutputFormat.CJS (OutputFormat.ESM requires Node.js >= 14)
                main_fields=["module", "main"],  # prefer ECMAScript versions of dependencies
                inject=["./my-shim.js", "./other-shim.js"],  # allows to automatically replace a global variable with an import from another file
                esbuild_args={ # Pass additional arguments to esbuild
                    "--log-limit": "0",
                    "--splitting": True}
            )
        )
    '''

    CJS = "CJS"
    '''CommonJS.'''
    ESM = "ESM"
    '''ECMAScript module.

    Requires a running environment that supports ``import`` and ``export`` syntax.
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_lambda_nodejs.SourceMapMode")
class SourceMapMode(enum.Enum):
    '''SourceMap mode for esbuild.

    :see: https://esbuild.github.io/api/#sourcemap
    :exampleMetadata: infused

    Example::

        nodejs.NodejsFunction(self, "my-handler",
            bundling=nodejs.BundlingOptions(
                minify=True,  # minify code, defaults to false
                source_map=True,  # include source map, defaults to false
                source_map_mode=nodejs.SourceMapMode.INLINE,  # defaults to SourceMapMode.DEFAULT
                sources_content=False,  # do not include original source into source map, defaults to true
                target="es2020",  # target environment for the generated JavaScript code
                loader={ # Use the 'dataurl' loader for '.png' files
                    ".png": "dataurl"},
                define={ # Replace strings during build time
                    "process.env.API_KEY": JSON.stringify("xxx-xxxx-xxx"),
                    "process.env.PRODUCTION": JSON.stringify(True),
                    "process.env.NUMBER": JSON.stringify(123)},
                log_level=nodejs.LogLevel.ERROR,  # defaults to LogLevel.WARNING
                keep_names=True,  # defaults to false
                tsconfig="custom-tsconfig.json",  # use custom-tsconfig.json instead of default,
                metafile=True,  # include meta file, defaults to false
                banner="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                footer="/* comments */",  # requires esbuild >= 0.9.0, defaults to none
                charset=nodejs.Charset.UTF8,  # do not escape non-ASCII characters, defaults to Charset.ASCII
                format=nodejs.OutputFormat.ESM,  # ECMAScript module output format, defaults to OutputFormat.CJS (OutputFormat.ESM requires Node.js >= 14)
                main_fields=["module", "main"],  # prefer ECMAScript versions of dependencies
                inject=["./my-shim.js", "./other-shim.js"],  # allows to automatically replace a global variable with an import from another file
                esbuild_args={ # Pass additional arguments to esbuild
                    "--log-limit": "0",
                    "--splitting": True}
            )
        )
    '''

    DEFAULT = "DEFAULT"
    '''Default sourceMap mode - will generate a .js.map file alongside any generated .js file and add a special //# sourceMappingURL= comment to the bottom of the .js file pointing to the .js.map file.'''
    EXTERNAL = "EXTERNAL"
    '''External sourceMap mode - If you want to omit the special //# sourceMappingURL= comment from the generated .js file but you still want to generate the .js.map files.'''
    INLINE = "INLINE"
    '''Inline sourceMap mode - If you want to insert the entire source map into the .js file instead of generating a separate .js.map file.'''
    BOTH = "BOTH"
    '''Both sourceMap mode - If you want to have the effect of both inline and external simultaneously.'''


__all__ = [
    "BundlingOptions",
    "Charset",
    "ICommandHooks",
    "LogLevel",
    "NodejsFunction",
    "NodejsFunctionProps",
    "OutputFormat",
    "SourceMapMode",
]

publication.publish()

def _typecheckingstub__8049cd6c8eb3542b1c20a2677da2bd64b4125320c114432030729ac28f71df41(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    network: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    security_opt: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Sequence[typing.Union[_DockerVolume_849485b7, typing.Dict[builtins.str, typing.Any]]]] = None,
    volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    banner: typing.Optional[builtins.str] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    bundle_aws_sdk: typing.Optional[builtins.bool] = None,
    bundling_file_access: typing.Optional[_BundlingFileAccess_281370cc] = None,
    charset: typing.Optional[Charset] = None,
    command_hooks: typing.Optional[ICommandHooks] = None,
    define: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    docker_image: typing.Optional[_DockerImage_f97a0c12] = None,
    esbuild_args: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]] = None,
    esbuild_version: typing.Optional[builtins.str] = None,
    external_modules: typing.Optional[typing.Sequence[builtins.str]] = None,
    footer: typing.Optional[builtins.str] = None,
    force_docker_bundling: typing.Optional[builtins.bool] = None,
    format: typing.Optional[OutputFormat] = None,
    inject: typing.Optional[typing.Sequence[builtins.str]] = None,
    keep_names: typing.Optional[builtins.bool] = None,
    loader: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    log_level: typing.Optional[LogLevel] = None,
    main_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    metafile: typing.Optional[builtins.bool] = None,
    minify: typing.Optional[builtins.bool] = None,
    node_modules: typing.Optional[typing.Sequence[builtins.str]] = None,
    pre_compilation: typing.Optional[builtins.bool] = None,
    source_map: typing.Optional[builtins.bool] = None,
    source_map_mode: typing.Optional[SourceMapMode] = None,
    sources_content: typing.Optional[builtins.bool] = None,
    target: typing.Optional[builtins.str] = None,
    tsconfig: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09dbe8bce258730fd8ac7ba62771c22efb44c7ebd8461cc5d827148a83bfe77d(
    input_dir: builtins.str,
    output_dir: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0964adbd439e9dc3679a84cd96429fd1e28a83b5f8007bff7046cb07e80d59f4(
    input_dir: builtins.str,
    output_dir: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__307f3bcc172246dc345479dc042e832516dc064777e3fa352640c4351101fa0d(
    input_dir: builtins.str,
    output_dir: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece177829b26ef102d4080d730f168e29d7d310d1518738839cd3fc822c258fb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aws_sdk_connection_reuse: typing.Optional[builtins.bool] = None,
    bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[_Code_7848f942] = None,
    deps_lock_file_path: typing.Optional[builtins.str] = None,
    entry: typing.Optional[builtins.str] = None,
    handler: typing.Optional[builtins.str] = None,
    project_root: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[_Runtime_b4eaa844] = None,
    adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    application_log_level: typing.Optional[builtins.str] = None,
    application_log_level_v2: typing.Optional[_ApplicationLogLevel_cd92660a] = None,
    architecture: typing.Optional[_Architecture_12d5a53f] = None,
    code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
    current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_IKey_5f11635f] = None,
    ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
    events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
    filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
    ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
    layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
    log_format: typing.Optional[builtins.str] = None,
    logging_format: typing.Optional[_LoggingFormat_30be8e01] = None,
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    snap_start: typing.Optional[_SnapStartConf_2ffaa769] = None,
    system_log_level: typing.Optional[builtins.str] = None,
    system_log_level_v2: typing.Optional[_SystemLogLevel_aea49dc2] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    on_failure: typing.Optional[_IDestination_40f19de4] = None,
    on_success: typing.Optional[_IDestination_40f19de4] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2da45b394f0332be0f6d6b7468d9fb54961953d56265da69955d36ffa3481d33(
    *,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    on_failure: typing.Optional[_IDestination_40f19de4] = None,
    on_success: typing.Optional[_IDestination_40f19de4] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    application_log_level: typing.Optional[builtins.str] = None,
    application_log_level_v2: typing.Optional[_ApplicationLogLevel_cd92660a] = None,
    architecture: typing.Optional[_Architecture_12d5a53f] = None,
    code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
    current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_IKey_5f11635f] = None,
    ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
    events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
    filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
    ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
    layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
    log_format: typing.Optional[builtins.str] = None,
    logging_format: typing.Optional[_LoggingFormat_30be8e01] = None,
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    snap_start: typing.Optional[_SnapStartConf_2ffaa769] = None,
    system_log_level: typing.Optional[builtins.str] = None,
    system_log_level_v2: typing.Optional[_SystemLogLevel_aea49dc2] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_sdk_connection_reuse: typing.Optional[builtins.bool] = None,
    bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[_Code_7848f942] = None,
    deps_lock_file_path: typing.Optional[builtins.str] = None,
    entry: typing.Optional[builtins.str] = None,
    handler: typing.Optional[builtins.str] = None,
    project_root: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[_Runtime_b4eaa844] = None,
) -> None:
    """Type checking stubs"""
    pass
