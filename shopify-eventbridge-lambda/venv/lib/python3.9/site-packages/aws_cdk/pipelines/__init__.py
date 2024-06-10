'''
# CDK Pipelines

A construct library for painless Continuous Delivery of CDK applications.

CDK Pipelines is an *opinionated construct library*. It is purpose-built to
deploy one or more copies of your CDK applications using CloudFormation with a
minimal amount of effort on your part. It is *not* intended to support arbitrary
deployment pipelines, and very specifically it is not built to use CodeDeploy to
deploy applications to instances, or deploy your custom-built ECR images to an ECS
cluster directly: use CDK file assets with CloudFormation Init for instances, or
CDK container assets for ECS clusters instead.

Give the CDK Pipelines way of doing things a shot first: you might find it does
everything you need. If you need more control, or if you need `v2` support from
`aws-codepipeline`, we recommend you drop down to using the `aws-codepipeline`
construct library directly.

> This module contains two sets of APIs: an **original** and a **modern** version of
> CDK Pipelines. The *modern* API has been updated to be easier to work with and
> customize, and will be the preferred API going forward. The *original* version
> of the API is still available for backwards compatibility, but we recommend migrating
> to the new version if possible.
>
> Compared to the original API, the modern API: has more sensible defaults; is
> more flexible; supports parallel deployments; supports multiple synth inputs;
> allows more control of CodeBuild project generation; supports deployment
> engines other than CodePipeline.
>
> The README for the original API, as well as a migration guide, can be found in
> [our GitHub repository](https://github.com/aws/aws-cdk/blob/main/packages/@aws-cdk/pipelines/ORIGINAL_API.md).

## At a glance

Deploying your application continuously starts by defining a
`MyApplicationStage`, a subclass of `Stage` that contains the stacks that make
up a single copy of your application.

You then define a `Pipeline`, instantiate as many instances of
`MyApplicationStage` as you want for your test and production environments, with
different parameters for each, and calling `pipeline.addStage()` for each of
them. You can deploy to the same account and Region, or to a different one,
with the same amount of code. The *CDK Pipelines* library takes care of the
details.

CDK Pipelines supports multiple *deployment engines* (see
[Using a different deployment engine](#using-a-different-deployment-engine)),
and comes with a deployment engine that deploys CDK apps using AWS CodePipeline.
To use the CodePipeline engine, define a `CodePipeline` construct.  The following
example creates a CodePipeline that deploys an application from GitHub:

```python
# The stacks for our app are minimally defined here.  The internals of these
# stacks aren't important, except that DatabaseStack exposes an attribute
# "table" for a database table it defines, and ComputeStack accepts a reference
# to this table in its properties.
#
class DatabaseStack(Stack):

    def __init__(self, scope, id):
        super().__init__(scope, id)
        self.table = dynamodb.TableV2(self, "Table",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING)
        )

class ComputeStack(Stack):
    def __init__(self, scope, id, *, table):
        super().__init__(scope, id)

#
# Stack to hold the pipeline
#
class MyPipelineStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None, crossRegionReferences=None, permissionsBoundary=None, suppressTemplateIndentation=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting, crossRegionReferences=crossRegionReferences, permissionsBoundary=permissionsBoundary, suppressTemplateIndentation=suppressTemplateIndentation)

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep("Synth",
                # Use a connection created using the AWS console to authenticate to GitHub
                # Other sources are available.
                input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"
                ]
            )
        )

        # 'MyApplication' is defined below. Call `addStage` as many times as
        # necessary with any account and region (may be different from the
        # pipeline's).
        pipeline.add_stage(MyApplication(self, "Prod",
            env=cdk.Environment(
                account="123456789012",
                region="eu-west-1"
            )
        ))

#
# Your application
#
# May consist of one or more Stacks (here, two)
#
# By declaring our DatabaseStack and our ComputeStack inside a Stage,
# we make sure they are deployed together, or not at all.
#
class MyApplication(Stage):
    def __init__(self, scope, id, *, env=None, outdir=None, stageName=None, permissionsBoundary=None, policyValidationBeta1=None):
        super().__init__(scope, id, env=env, outdir=outdir, stageName=stageName, permissionsBoundary=permissionsBoundary, policyValidationBeta1=policyValidationBeta1)

        db_stack = DatabaseStack(self, "Database")
        ComputeStack(self, "Compute",
            table=db_stack.table
        )

# In your main file
MyPipelineStack(self, "PipelineStack",
    env=cdk.Environment(
        account="123456789012",
        region="eu-west-1"
    )
)
```

The pipeline is **self-mutating**, which means that if you add new
application stages in the source code, or new stacks to `MyApplication`, the
pipeline will automatically reconfigure itself to deploy those new stages and
stacks.

(Note that you have to *bootstrap* all environments before the above code
will work, and switch on "Modern synthesis" if you are using
CDKv1. See the section **CDK Environment Bootstrapping** below for
more information).

## Provisioning the pipeline

To provision the pipeline you have defined, make sure the target environment
has been bootstrapped (see below), and then execute deploying the
`PipelineStack` *once*. Afterwards, the pipeline will keep itself up-to-date.

> **Important**: be sure to `git commit` and `git push` before deploying the
> Pipeline stack using `cdk deploy`!
>
> The reason is that the pipeline will start deploying and self-mutating
> right away based on the sources in the repository, so the sources it finds
> in there should be the ones you want it to find.

Run the following commands to get the pipeline going:

```console
$ git commit -a
$ git push
$ cdk deploy PipelineStack
```

Administrative permissions to the account are only necessary up until
this point. We recommend you remove access to these credentials after doing this.

### Working on the pipeline

The self-mutation feature of the Pipeline might at times get in the way
of the pipeline development workflow. Each change to the pipeline must be pushed
to git, otherwise, after the pipeline was updated using `cdk deploy`, it will
automatically revert to the state found in git.

To make the development more convenient, the self-mutation feature can be turned
off temporarily, by passing `selfMutation: false` property, example:

```python
# Modern API
modern_pipeline = pipelines.CodePipeline(self, "Pipeline",
    self_mutation=False,
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"
        ]
    )
)

# Original API
cloud_assembly_artifact = codepipeline.Artifact()
original_pipeline = pipelines.CdkPipeline(self, "Pipeline",
    self_mutating=False,
    cloud_assembly_artifact=cloud_assembly_artifact
)
```

## Defining the pipeline

This section of the documentation describes the AWS CodePipeline engine,
which comes with this library. If you want to use a different deployment
engine, read the section
[Using a different deployment engine](#using-a-different-deployment-engine) below.

### Synth and sources

To define a pipeline, instantiate a `CodePipeline` construct from the
`aws-cdk-lib/pipelines` module. It takes one argument, a `synth` step, which is
expected to produce the CDK Cloud Assembly as its single output (the contents of
the `cdk.out` directory after running `cdk synth`). "Steps" are arbitrary
actions in the pipeline, typically used to run scripts or commands.

For the synth, use a `ShellStep` and specify the commands necessary to install
dependencies, the CDK CLI, build your project and run `cdk synth`; the specific
commands required will depend on the programming language you are using. For a
typical NPM-based project, the synth will look like this:

```python
# source: pipelines.IFileSetProducer
# the repository source

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=["npm ci", "npm run build", "npx cdk synth"
        ]
    )
)
```

The pipeline assumes that your `ShellStep` will produce a `cdk.out`
directory in the root, containing the CDK cloud assembly. If your
CDK project lives in a subdirectory, be sure to adjust the
`primaryOutputDirectory` to match:

```python
# source: pipelines.IFileSetProducer
# the repository source

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=["cd mysubdir", "npm ci", "npm run build", "npx cdk synth"
        ],
        primary_output_directory="mysubdir/cdk.out"
    )
)
```

The underlying `aws-cdk-lib/aws-codepipeline.Pipeline` construct will be produced
when `app.synth()` is called. You can also force it to be produced
earlier by calling `pipeline.buildPipeline()`. After you've called
that method, you can inspect the constructs that were produced by
accessing the properties of the `pipeline` object.

#### Commands for other languages and package managers

The commands you pass to `new ShellStep` will be very similar to the commands
you run on your own workstation to install dependencies and synth your CDK
project. Here are some (non-exhaustive) examples for what those commands might
look like in a number of different situations.

For Yarn, the install commands are different:

```python
# source: pipelines.IFileSetProducer
# the repository source

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=["yarn install --frozen-lockfile", "yarn build", "npx cdk synth"
        ]
    )
)
```

For Python projects, remember to install the CDK CLI globally (as
there is no `package.json` to automatically install it for you):

```python
# source: pipelines.IFileSetProducer
# the repository source

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=["pip install -r requirements.txt", "npm install -g aws-cdk", "cdk synth"
        ]
    )
)
```

For Java projects, remember to install the CDK CLI globally (as
there is no `package.json` to automatically install it for you),
and the Maven compilation step is automatically executed for you
as you run `cdk synth`:

```python
# source: pipelines.IFileSetProducer
# the repository source

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=["npm install -g aws-cdk", "cdk synth"
        ]
    )
)
```

You can adapt these examples to your own situation.

#### Migrating from buildspec.yml files

You may currently have the build instructions for your CodeBuild Projects in a
`buildspec.yml` file in your source repository. In addition to your build
commands, the CodeBuild Project's buildspec also controls some information that
CDK Pipelines manages for you, like artifact identifiers, input artifact
locations, Docker authorization, and exported variables.

Since there is no way in general for CDK Pipelines to modify the file in your
resource repository, CDK Pipelines configures the BuildSpec directly on the
CodeBuild Project, instead of loading it from the `buildspec.yml` file.
This requires a pipeline self-mutation to update.

To avoid this, put your build instructions in a separate script, for example
`build.sh`, and call that script from the build `commands` array:

```python
# source: pipelines.IFileSetProducer


pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=["./build.sh"
        ]
    )
)
```

Doing so keeps your exact build instructions in sync with your source code in
the source repository where it belongs, and provides a convenient build script
for developers at the same time.

#### CodePipeline Sources

In CodePipeline, *Sources* define where the source of your application lives.
When a change to the source is detected, the pipeline will start executing.
Source objects can be created by factory methods on the `CodePipelineSource` class:

##### GitHub, GitHub Enterprise, BitBucket using a connection

The recommended way of connecting to GitHub or BitBucket is by using a *connection*.
You will first use the AWS Console to authenticate to the source control
provider, and then use the connection ARN in your pipeline definition:

```python
pipelines.CodePipelineSource.connection("org/repo", "branch",
    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
)
```

##### GitHub using OAuth

You can also authenticate to GitHub using a personal access token. This expects
that you've created a personal access token and stored it in Secrets Manager.
By default, the source object will look for a secret named **github-token**, but
you can change the name. The token should have the **repo** and **admin:repo_hook**
scopes.

```python
pipelines.CodePipelineSource.git_hub("org/repo", "branch",
    # This is optional
    authentication=cdk.SecretValue.secrets_manager("my-token")
)
```

##### CodeCommit

You can use a CodeCommit repository as the source. Either create or import
that the CodeCommit repository and then use `CodePipelineSource.codeCommit`
to reference it:

```python
repository = codecommit.Repository.from_repository_name(self, "Repository", "my-repository")
pipelines.CodePipelineSource.code_commit(repository, "main")
```

##### S3

You can use a zip file in S3 as the source of the pipeline. The pipeline will be
triggered every time the file in S3 is changed:

```python
bucket = s3.Bucket.from_bucket_name(self, "Bucket", "my-bucket")
pipelines.CodePipelineSource.s3(bucket, "my/source.zip")
```

##### ECR

You can use a Docker image in ECR as the source of the pipeline. The pipeline will be
triggered every time an image is pushed to ECR:

```python
repository = ecr.Repository(self, "Repository")
pipelines.CodePipelineSource.ecr(repository)
```

#### Additional inputs

`ShellStep` allows passing in more than one input: additional
inputs will be placed in the directories you specify. Any step that produces an
output file set can be used as an input, such as a `CodePipelineSource`, but
also other `ShellStep`:

```python
prebuild = pipelines.ShellStep("Prebuild",
    input=pipelines.CodePipelineSource.git_hub("myorg/repo1", "main"),
    primary_output_directory="./build",
    commands=["./build.sh"]
)

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.git_hub("myorg/repo2", "main"),
        additional_inputs={
            "subdir": pipelines.CodePipelineSource.git_hub("myorg/repo3", "main"),
            "../siblingdir": prebuild
        },

        commands=["./build.sh"]
    )
)
```

### CDK application deployments

After you have defined the pipeline and the `synth` step, you can add one or
more CDK `Stages` which will be deployed to their target environments. To do
so, call `pipeline.addStage()` on the Stage object:

```python
# pipeline: pipelines.CodePipeline

# Do this as many times as necessary with any account and region
# Account and region may different from the pipeline's.
pipeline.add_stage(MyApplicationStage(self, "Prod",
    env=cdk.Environment(
        account="123456789012",
        region="eu-west-1"
    )
))
```

CDK Pipelines will automatically discover all `Stacks` in the given `Stage`
object, determine their dependency order, and add appropriate actions to the
pipeline to publish the assets referenced in those stacks and deploy the stacks
in the right order.

If the `Stacks` are targeted at an environment in a different AWS account or
Region and that environment has been
[bootstrapped](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html)
, CDK Pipelines will transparently make sure the IAM roles are set up
correctly and any requisite replication Buckets are created.

#### Deploying in parallel

By default, all applications added to CDK Pipelines by calling `addStage()` will
be deployed in sequence, one after the other. If you have a lot of stages, you can
speed up the pipeline by choosing to deploy some stages in parallel. You do this
by calling `addWave()` instead of `addStage()`: a *wave* is a set of stages that
are all deployed in parallel instead of sequentially. Waves themselves are still
deployed in sequence. For example, the following will deploy two copies of your
application to `eu-west-1` and `eu-central-1` in parallel:

```python
# pipeline: pipelines.CodePipeline

europe_wave = pipeline.add_wave("Europe")
europe_wave.add_stage(MyApplicationStage(self, "Ireland",
    env=cdk.Environment(region="eu-west-1")
))
europe_wave.add_stage(MyApplicationStage(self, "Germany",
    env=cdk.Environment(region="eu-central-1")
))
```

#### Deploying to other accounts / encrypting the Artifact Bucket

CDK Pipelines can transparently deploy to other Regions and other accounts
(provided those target environments have been
[*bootstrapped*](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html)).
However, deploying to another account requires one additional piece of
configuration: you need to enable `crossAccountKeys: true` when creating the
pipeline.

This will encrypt the artifact bucket(s), but incurs a cost for maintaining the
KMS key.

You may also wish to enable automatic key rotation for the created KMS key.

Example:

```python
pipeline = pipelines.CodePipeline(self, "Pipeline",
    # Encrypt artifacts, required for cross-account deployments
    cross_account_keys=True,
    enable_key_rotation=True,  # optional
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"
        ]
    )
)
```

#### Deploying without change sets

Deployment is done by default with `CodePipeline` engine using change sets,
i.e. to first create a change set and then execute it. This allows you to inject
steps that inspect the change set and approve or reject it, but failed deployments
are not retryable and creation of the change set costs time.

The creation of change sets can be switched off by setting `useChangeSets: false`:

```python
# synth: pipelines.ShellStep


class PipelineStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None, crossRegionReferences=None, permissionsBoundary=None, suppressTemplateIndentation=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting, crossRegionReferences=crossRegionReferences, permissionsBoundary=permissionsBoundary, suppressTemplateIndentation=suppressTemplateIndentation)

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=synth,

            # Disable change set creation and make deployments in pipeline as single step
            use_change_sets=False
        )
```

### Validation

Every `addStage()` and `addWave()` command takes additional options. As part of these options,
you can specify `pre` and `post` steps, which are arbitrary steps that run before or after
the contents of the stage or wave, respectively. You can use these to add validations like
manual or automated gates to your pipeline. We recommend putting manual approval gates in the set of `pre` steps, and automated approval gates in
the set of `post` steps.

The following example shows both an automated approval in the form of a `ShellStep`, and
a manual approval in the form of a `ManualApprovalStep` added to the pipeline. Both must
pass in order to promote from the `PreProd` to the `Prod` environment:

```python
# pipeline: pipelines.CodePipeline

preprod = MyApplicationStage(self, "PreProd")
prod = MyApplicationStage(self, "Prod")

pipeline.add_stage(preprod,
    post=[
        pipelines.ShellStep("Validate Endpoint",
            commands=["curl -Ssf https://my.webservice.com/"]
        )
    ]
)
pipeline.add_stage(prod,
    pre=[
        pipelines.ManualApprovalStep("PromoteToProd")
    ]
)
```

You can also specify steps to be executed at the stack level. To achieve this, you can specify the stack and step via the `stackSteps` property:

```python
# pipeline: pipelines.CodePipeline
class MyStacksStage(Stage):

    def __init__(self, scope, id, *, env=None, outdir=None, stageName=None, permissionsBoundary=None, policyValidationBeta1=None):
        super().__init__(scope, id, env=env, outdir=outdir, stageName=stageName, permissionsBoundary=permissionsBoundary, policyValidationBeta1=policyValidationBeta1)
        self.stack1 = Stack(self, "stack1")
        self.stack2 = Stack(self, "stack2")
prod = MyStacksStage(self, "Prod")

pipeline.add_stage(prod,
    stack_steps=[pipelines.StackSteps(
        stack=prod.stack1,
        pre=[pipelines.ManualApprovalStep("Pre-Stack Check")],  # Executed before stack is prepared
        change_set=[pipelines.ManualApprovalStep("ChangeSet Approval")],  # Executed after stack is prepared but before the stack is deployed
        post=[pipelines.ManualApprovalStep("Post-Deploy Check")]
    ), pipelines.StackSteps(
        stack=prod.stack2,
        post=[pipelines.ManualApprovalStep("Post-Deploy Check")]
    )]
)
```

If you specify multiple steps, they will execute in parallel by default. You can add dependencies between them
to if you wish to specify an order. To add a dependency, call `step.addStepDependency()`:

```python
first_step = pipelines.ManualApprovalStep("A")
second_step = pipelines.ManualApprovalStep("B")
second_step.add_step_dependency(first_step)
```

For convenience, `Step.sequence()` will take an array of steps and dependencies between adjacent steps,
so that the whole list executes in order:

```python
# Step A will depend on step B and step B will depend on step C
ordered_steps = pipelines.Step.sequence([
    pipelines.ManualApprovalStep("A"),
    pipelines.ManualApprovalStep("B"),
    pipelines.ManualApprovalStep("C")
])
```

#### Using CloudFormation Stack Outputs in approvals

Because many CloudFormation deployments result in the generation of resources with unpredictable
names, validations have support for reading back CloudFormation Outputs after a deployment. This
makes it possible to pass (for example) the generated URL of a load balancer to the test set.

To use Stack Outputs, expose the `CfnOutput` object you're interested in, and
pass it to `envFromCfnOutputs` of the `ShellStep`:

```python
# pipeline: pipelines.CodePipeline
class MyOutputStage(Stage):

    def __init__(self, scope, id, *, env=None, outdir=None, stageName=None, permissionsBoundary=None, policyValidationBeta1=None):
        super().__init__(scope, id, env=env, outdir=outdir, stageName=stageName, permissionsBoundary=permissionsBoundary, policyValidationBeta1=policyValidationBeta1)
        self.load_balancer_address = CfnOutput(self, "Output", value="value")

lb_app = MyOutputStage(self, "MyApp")
pipeline.add_stage(lb_app,
    post=[
        pipelines.ShellStep("HitEndpoint",
            env_from_cfn_outputs={
                # Make the load balancer address available as $URL inside the commands
                "URL": lb_app.load_balancer_address
            },
            commands=["curl -Ssf $URL"]
        )
    ]
)
```

#### Running scripts compiled during the synth step

As part of a validation, you probably want to run a test suite that's more
elaborate than what can be expressed in a couple of lines of shell script.
You can bring additional files into the shell script validation by supplying
the `input` or `additionalInputs` property of `ShellStep`. The input can
be produced by the `Synth` step, or come from a source or any other build
step.

Here's an example that captures an additional output directory in the synth
step and runs tests from there:

```python
# synth: pipelines.ShellStep

stage = MyApplicationStage(self, "MyApplication")
pipeline = pipelines.CodePipeline(self, "Pipeline", synth=synth)

pipeline.add_stage(stage,
    post=[
        pipelines.ShellStep("Approve",
            # Use the contents of the 'integ' directory from the synth step as the input
            input=synth.add_output_directory("integ"),
            commands=["cd integ && ./run.sh"]
        )
    ]
)
```

### Customizing CodeBuild Projects

CDK pipelines will generate CodeBuild projects for each `ShellStep` you use, and it
will also generate CodeBuild projects to publish assets and perform the self-mutation
of the pipeline. To control the various aspects of the CodeBuild projects that get
generated, use a `CodeBuildStep` instead of a `ShellStep`. This class has a number
of properties that allow you to customize various aspects of the projects:

```python
# vpc: ec2.Vpc
# my_security_group: ec2.SecurityGroup

pipelines.CodeBuildStep("Synth",
    # ...standard ShellStep props...
    commands=[],
    env={},

    # If you are using a CodeBuildStep explicitly, set the 'cdk.out' directory
    # to be the synth step's output.
    primary_output_directory="cdk.out",

    # Control the name of the project
    project_name="MyProject",

    # Control parts of the BuildSpec other than the regular 'build' and 'install' commands
    partial_build_spec=codebuild.BuildSpec.from_object({
        "version": "0.2"
    }),

    # Control the build environment
    build_environment=codebuild.BuildEnvironment(
        compute_type=codebuild.ComputeType.LARGE,
        privileged=True
    ),
    timeout=Duration.minutes(90),
    file_system_locations=[codebuild.FileSystemLocation.efs(
        identifier="myidentifier2",
        location="myclodation.mydnsroot.com:/loc",
        mount_point="/media",
        mount_options="opts"
    )],

    # Control Elastic Network Interface creation
    vpc=vpc,
    subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
    security_groups=[my_security_group],

    # Control caching
    cache=codebuild.Cache.bucket(s3.Bucket(self, "Cache")),

    # Additional policy statements for the execution role
    role_policy_statements=[
        iam.PolicyStatement()
    ]
)
```

You can also configure defaults for *all* CodeBuild projects by passing `codeBuildDefaults`,
or just for the synth, asset publishing, and self-mutation projects by passing `synthCodeBuildDefaults`,
`assetPublishingCodeBuildDefaults`, or `selfMutationCodeBuildDefaults`:

```python
from aws_cdk import aws_logs as logs

# vpc: ec2.Vpc
# my_security_group: ec2.SecurityGroup


pipelines.CodePipeline(self, "Pipeline",
    # Standard CodePipeline properties
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"
        ]
    ),

    # Defaults for all CodeBuild projects
    code_build_defaults=pipelines.CodeBuildOptions(
        # Prepend commands and configuration to all projects
        partial_build_spec=codebuild.BuildSpec.from_object({
            "version": "0.2"
        }),

        # Control the build environment
        build_environment=codebuild.BuildEnvironment(
            compute_type=codebuild.ComputeType.LARGE
        ),

        # Control Elastic Network Interface creation
        vpc=vpc,
        subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        security_groups=[my_security_group],

        # Additional policy statements for the execution role
        role_policy=[
            iam.PolicyStatement()
        ],

        # Information about logs
        logging=codebuild.LoggingOptions(
            cloud_watch=codebuild.CloudWatchLoggingOptions(
                log_group=logs.LogGroup(self, "MyLogGroup")
            ),
            s3=codebuild.S3LoggingOptions(
                bucket=s3.Bucket(self, "LogBucket")
            )
        )
    ),

    synth_code_build_defaults=pipelines.CodeBuildOptions(),
    asset_publishing_code_build_defaults=pipelines.CodeBuildOptions(),
    self_mutation_code_build_defaults=pipelines.CodeBuildOptions()
)
```

### Arbitrary CodePipeline actions

If you want to add a type of CodePipeline action to the CDK Pipeline that
doesn't have a matching class yet, you can define your own step class that extends
`Step` and implements `ICodePipelineActionFactory`.

Here's an example that adds a Jenkins step:

```python
@jsii.implements(pipelines.ICodePipelineActionFactory)
class MyJenkinsStep(pipelines.Step):
    def __init__(self, provider, input):
        super().__init__("MyJenkinsStep")

        # This is necessary if your step accepts parameters, like environment variables,
        # that may contain outputs from other steps. It doesn't matter what the
        # structure is, as long as it contains the values that may contain outputs.
        self.discover_referenced_outputs({
            "env": {}
        })

    def produce_action(self, stage, *, scope, actionName, runOrder, variablesNamespace=None, artifacts, fallbackArtifact=None, pipeline, codeBuildDefaults=None, beforeSelfMutation=None, stackOutputsMap):

        # This is where you control what type of Action gets added to the
        # CodePipeline
        stage.add_action(cpactions.JenkinsAction(
            # Copy 'actionName' and 'runOrder' from the options
            action_name=action_name,
            run_order=run_order,

            # Jenkins-specific configuration
            type=cpactions.JenkinsActionType.TEST,
            jenkins_provider=self.provider,
            project_name="MyJenkinsProject",

            # Translate the FileSet into a codepipeline.Artifact
            inputs=[artifacts.to_code_pipeline(self.input)]
        ))

        return pipelines.CodePipelineActionFactoryResult(run_orders_consumed=1)
```

Another example, adding a lambda step referencing outputs from a stack:

```python
@jsii.implements(pipelines.ICodePipelineActionFactory)
class MyLambdaStep(pipelines.Step):

    def __init__(self, fn, stack_output):
        super().__init__("MyLambdaStep")
        self.stack_output_reference = pipelines.StackOutputReference.from_cfn_output(stack_output)

    def produce_action(self, stage, *, scope, actionName, runOrder, variablesNamespace=None, artifacts, fallbackArtifact=None, pipeline, codeBuildDefaults=None, beforeSelfMutation=None, stackOutputsMap):

        stage.add_action(cpactions.LambdaInvokeAction(
            action_name=action_name,
            run_order=run_order,
            # Map the reference to the variable name the CDK has generated for you.
            user_parameters={"stack_output": stack_outputs_map.to_code_pipeline(self.stack_output_reference)},
            lambda_=self.fn
        ))

        return pipelines.CodePipelineActionFactoryResult(run_orders_consumed=1)public get consumedStackOutputs(): pipelines.StackOutputReference[] {
        return [this.stackOutputReference];
      }
```

### Using an existing AWS Codepipeline

If you wish to use an existing `CodePipeline.Pipeline` while using the modern API's
methods and classes, you can pass in the existing `CodePipeline.Pipeline` to be built upon
instead of having the `pipelines.CodePipeline` construct create a new `CodePipeline.Pipeline`.
This also gives you more direct control over the underlying `CodePipeline.Pipeline` construct
if the way the modern API creates it doesn't allow for desired configurations. Use `CodePipelineFileset` to convert CodePipeline **artifacts** into CDK Pipelines **file sets**,
that can be used everywhere a file set or file set producer is expected.

Here's an example of passing in an existing pipeline and using a *source* that's already
in the pipeline:

```python
# code_pipeline: codepipeline.Pipeline


source_artifact = codepipeline.Artifact("MySourceArtifact")

pipeline = pipelines.CodePipeline(self, "Pipeline",
    code_pipeline=code_pipeline,
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineFileSet.from_artifact(source_artifact),
        commands=["npm ci", "npm run build", "npx cdk synth"]
    )
)
```

If your existing pipeline already provides a synth step, pass the existing
artifact in place of the `synth` step:

```python
# code_pipeline: codepipeline.Pipeline


build_artifact = codepipeline.Artifact("MyBuildArtifact")

pipeline = pipelines.CodePipeline(self, "Pipeline",
    code_pipeline=code_pipeline,
    synth=pipelines.CodePipelineFileSet.from_artifact(build_artifact)
)
```

Note that if you provide an existing pipeline, you cannot provide values for
`pipelineName`, `crossAccountKeys`, `reuseCrossRegionSupportStacks`, or `role`
because those values are passed in directly to the underlying `codepipeline.Pipeline`.

## Using Docker in the pipeline

Docker can be used in 3 different places in the pipeline:

* If you are using Docker image assets in your application stages: Docker will
  run in the asset publishing projects.
* If you are using Docker image assets in your stack (for example as
  images for your CodeBuild projects): Docker will run in the self-mutate project.
* If you are using Docker to bundle file assets anywhere in your project (for
  example, if you are using such construct libraries as
  `aws-cdk-lib/aws-lambda-nodejs`): Docker will run in the
  *synth* project.

For the first case, you don't need to do anything special. For the other two cases,
you need to make sure that **privileged mode** is enabled on the correct CodeBuild
projects, so that Docker can run correctly. The follow sections describe how to do
that.

You may also need to authenticate to Docker registries to avoid being throttled.
See the section **Authenticating to Docker registries** below for information on how to do
that.

### Using Docker image assets in the pipeline

If your `PipelineStack` is using Docker image assets (as opposed to the application
stacks the pipeline is deploying), for example by the use of `LinuxBuildImage.fromAsset()`,
you need to pass `dockerEnabledForSelfMutation: true` to the pipeline. For example:

```python
pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"]
    ),

    # Turn this on because the pipeline uses Docker image assets
    docker_enabled_for_self_mutation=True
)

pipeline.add_wave("MyWave",
    post=[
        pipelines.CodeBuildStep("RunApproval",
            commands=["command-from-image"],
            build_environment=codebuild.BuildEnvironment(
                # The user of a Docker image asset in the pipeline requires turning on
                # 'dockerEnabledForSelfMutation'.
                build_image=codebuild.LinuxBuildImage.from_asset(self, "Image",
                    directory="./docker-image"
                )
            )
        )
    ]
)
```

> **Important**: You must turn on the `dockerEnabledForSelfMutation` flag,
> commit and allow the pipeline to self-update *before* adding the actual
> Docker asset.

### Using bundled file assets

If you are using asset bundling anywhere (such as automatically done for you
if you add a construct like `aws-cdk-lib/aws-lambda-nodejs`), you need to pass
`dockerEnabledForSynth: true` to the pipeline. For example:

```python
pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"]
    ),

    # Turn this on because the application uses bundled file assets
    docker_enabled_for_synth=True
)
```

> **Important**: You must turn on the `dockerEnabledForSynth` flag,
> commit and allow the pipeline to self-update *before* adding the actual
> Docker asset.

### Authenticating to Docker registries

You can specify credentials to use for authenticating to Docker registries as part of the
pipeline definition. This can be useful if any Docker image assets — in the pipeline or
any of the application stages — require authentication, either due to being in a
different environment (e.g., ECR repo) or to avoid throttling (e.g., DockerHub).

```python
docker_hub_secret = secretsmanager.Secret.from_secret_complete_arn(self, "DHSecret", "arn:aws:...")
custom_reg_secret = secretsmanager.Secret.from_secret_complete_arn(self, "CRSecret", "arn:aws:...")
repo1 = ecr.Repository.from_repository_arn(self, "Repo", "arn:aws:ecr:eu-west-1:0123456789012:repository/Repo1")
repo2 = ecr.Repository.from_repository_arn(self, "Repo", "arn:aws:ecr:eu-west-1:0123456789012:repository/Repo2")

pipeline = pipelines.CodePipeline(self, "Pipeline",
    docker_credentials=[
        pipelines.DockerCredential.docker_hub(docker_hub_secret),
        pipelines.DockerCredential.custom_registry("dockerregistry.example.com", custom_reg_secret),
        pipelines.DockerCredential.ecr([repo1, repo2])
    ],
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"]
    )
)
```

For authenticating to Docker registries that require a username and password combination
(like DockerHub), create a Secrets Manager Secret with fields named `username`
and `secret`, and import it (the field names change be customized).

Authentication to ECR repositories is done using the execution role of the
relevant CodeBuild job. Both types of credentials can be provided with an
optional role to assume before requesting the credentials.

By default, the Docker credentials provided to the pipeline will be available to
the **Synth**, **Self-Update**, and **Asset Publishing** actions within the
*pipeline. The scope of the credentials can be limited via the `DockerCredentialUsage` option.

```python
docker_hub_secret = secretsmanager.Secret.from_secret_complete_arn(self, "DHSecret", "arn:aws:...")
# Only the image asset publishing actions will be granted read access to the secret.
creds = pipelines.DockerCredential.docker_hub(docker_hub_secret, usages=[pipelines.DockerCredentialUsage.ASSET_PUBLISHING])
```

## CDK Environment Bootstrapping

An *environment* is an *(account, region)* pair where you want to deploy a
CDK stack (see
[Environments](https://docs.aws.amazon.com/cdk/latest/guide/environments.html)
in the CDK Developer Guide). In a Continuous Deployment pipeline, there are
at least two environments involved: the environment where the pipeline is
provisioned, and the environment where you want to deploy the application (or
different stages of the application). These can be the same, though best
practices recommend you isolate your different application stages from each
other in different AWS accounts or regions.

Before you can provision the pipeline, you have to *bootstrap* the environment you want
to create it in. If you are deploying your application to different environments, you
also have to bootstrap those and be sure to add a *trust* relationship.

After you have bootstrapped an environment and created a pipeline that deploys
to it, it's important that you don't delete the stack or change its *Qualifier*,
or future deployments to this environment will fail. If you want to upgrade
the bootstrap stack to a newer version, do that by updating it in-place.

> This library requires the *modern* bootstrapping stack which has
> been updated specifically to support cross-account continuous delivery.
>
> If you are using CDKv2, you do not need to do anything else. Modern
> bootstrapping and modern stack synthesis (also known as "default stack
> synthesis") is the default.
>
> If you are using CDKv1, you need to opt in to modern bootstrapping and
> modern stack synthesis using a feature flag. Make sure `cdk.json` includes:
>
> ```json
> {
>   "context": {
>     "@aws-cdk/core:newStyleStackSynthesis": true
>   }
> }
> ```
>
> And be sure to run `cdk bootstrap` in the same directory as the `cdk.json`
> file.

To bootstrap an environment for provisioning the pipeline:

```console
$ npx cdk bootstrap \
    [--profile admin-profile-1] \
    --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess \
    aws://111111111111/us-east-1
```

To bootstrap a different environment for deploying CDK applications into using
a pipeline in account `111111111111`:

```console
$ npx cdk bootstrap \
    [--profile admin-profile-2] \
    --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess \
    --trust 11111111111 \
    aws://222222222222/us-east-2
```

If you only want to trust an account to do lookups (e.g, when your CDK application has a
`Vpc.fromLookup()` call), use the option `--trust-for-lookup`:

```console
$ npx cdk bootstrap \
    [--profile admin-profile-2] \
    --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess \
    --trust-for-lookup 11111111111 \
    aws://222222222222/us-east-2
```

These command lines explained:

* `npx`: means to use the CDK CLI from the current NPM install. If you are using
  a global install of the CDK CLI, leave this out.
* `--profile`: should indicate a profile with administrator privileges that has
  permissions to provision a pipeline in the indicated account. You can leave this
  flag out if either the AWS default credentials or the `AWS_*` environment
  variables confer these permissions.
* `--cloudformation-execution-policies`: ARN of the managed policy that future CDK
  deployments should execute with. By default this is `AdministratorAccess`, but
  if you also specify the `--trust` flag to give another Account permissions to
  deploy into the current account, you must specify a value here.
* `--trust`: indicates which other account(s) should have permissions to deploy
  CDK applications into this account. In this case we indicate the Pipeline's account,
  but you could also use this for developer accounts (don't do that for production
  application accounts though!).
* `--trust-for-lookup`: gives a more limited set of permissions to the
  trusted account, only allowing it to look up values such as availability zones, EC2 images and
  VPCs. `--trust-for-lookup` does not give permissions to modify anything in the account.
  Note that `--trust` implies `--trust-for-lookup`, so you don't need to specify
  the same account twice.
* `aws://222222222222/us-east-2`: the account and region we're bootstrapping.

> Be aware that anyone who has access to the trusted Accounts **effectively has all
> permissions conferred by the configured CloudFormation execution policies**,
> allowing them to do things like read arbitrary S3 buckets and create arbitrary
> infrastructure in the bootstrapped account.  Restrict the list of `--trust`ed Accounts,
> or restrict the policies configured by `--cloudformation-execution-policies`.

<br>

> **Security tip**: we recommend that you use administrative credentials to an
> account only to bootstrap it and provision the initial pipeline. Otherwise,
> access to administrative credentials should be dropped as soon as possible.

<br>

> **On the use of AdministratorAccess**: The use of the `AdministratorAccess` policy
> ensures that your pipeline can deploy every type of AWS resource to your account.
> Make sure you trust all the code and dependencies that make up your CDK app.
> Check with the appropriate department within your organization to decide on the
> proper policy to use.
>
> If your policy includes permissions to create on attach permission to a role,
> developers can escalate their privilege with more permissive permission.
> Thus, we recommend implementing [permissions boundary](https://aws.amazon.com/premiumsupport/knowledge-center/iam-permission-boundaries/)
> in the CDK Execution role. To do this, you can bootstrap with the `--template` option with
> [a customized template](https://github.com/aws-samples/aws-bootstrap-kit-examples/blob/ba28a97d289128281bc9483bcba12c1793f2c27a/source/1-SDLC-organization/lib/cdk-bootstrap-template.yml#L395) that contains a permission boundary.

### Migrating from old bootstrap stack

The bootstrap stack is a CloudFormation stack in your account named
**CDKToolkit** that provisions a set of resources required for the CDK
to deploy into that environment.

The "new" bootstrap stack (obtained by running `cdk bootstrap` with
`CDK_NEW_BOOTSTRAP=1`) is slightly more elaborate than the "old" stack. It
contains:

* An S3 bucket and ECR repository with predictable names, so that we can reference
  assets in these storage locations *without* the use of CloudFormation template
  parameters.
* A set of roles with permissions to access these asset locations and to execute
  CloudFormation, assumable from whatever accounts you specify under `--trust`.

It is possible and safe to migrate from the old bootstrap stack to the new
bootstrap stack. This will create a new S3 file asset bucket in your account
and orphan the old bucket. You should manually delete the orphaned bucket
after you are sure you have redeployed all CDK applications and there are no
more references to the old asset bucket.

## Considerations around Running at Scale

If you are planning to run pipelines for more than a hundred repos
deploying across multiple regions, then you will want to consider reusing
both artifacts buckets and cross-region replication buckets.

In a situation like this, you will want to have a separate CDK app / dedicated repo which creates
and managed the buckets which will be shared by the pipelines of all your other apps.
Note that this app must NOT be using the shared buckets because of chicken & egg issues.

The following code assumes you have created and are managing your buckets in the aforementioned
separate cdk repo and are just importing them for use in one of your (many) pipelines.

```python
# shared_xRegion_us_west1_bucket_arn: str
# shared_xRegion_us_west1_key_arn: str

# shared_xRegion_us_west2_bucket_arn: str
# shared_xRegion_us_west2_key_arn: str


us_west1_bucket = s3.Bucket.from_bucket_attributes(scope, "UsEast1Bucket",
    bucket_arn=shared_xRegion_us_west1_bucket_arn,
    encryption_key=kms.Key.from_key_arn(scope, "UsEast1BucketKeyArn", shared_xRegion_us_west1_bucket_arn)
)

us_west2_bucket = s3.Bucket.from_bucket_attributes(scope, "UsWest2Bucket",
    bucket_arn=shared_xRegion_us_west2_bucket_arn,
    encryption_key=kms.Key.from_key_arn(scope, "UsWest2BucketKeyArn", shared_xRegion_us_west2_key_arn)
)

cross_region_replication_buckets = {
    "us-west-1": us_west1_bucket,
    "us-west-2": us_west2_bucket
}

pipeline = pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.ShellStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["npm ci", "npm run build", "npx cdk synth"]
    ),  # Use shared buckets.
    cross_region_replication_buckets=cross_region_replication_buckets
)
```

## Context Lookups

You might be using CDK constructs that need to look up [runtime
context](https://docs.aws.amazon.com/cdk/latest/guide/context.html#context_methods),
which is information from the target AWS Account and Region the CDK needs to
synthesize CloudFormation templates appropriate for that environment. Examples
of this kind of context lookups are the number of Availability Zones available
to you, a Route53 Hosted Zone ID, or the ID of an AMI in a given region. This
information is automatically looked up when you run `cdk synth`.

By default, a `cdk synth` performed in a pipeline will not have permissions
to perform these lookups, and the lookups will fail. This is by design.

**Our recommended way of using lookups** is by running `cdk synth` on the
developer workstation and checking in the `cdk.context.json` file, which
contains the results of the context lookups. This will make sure your
synthesized infrastructure is consistent and repeatable. If you do not commit
`cdk.context.json`, the results of the lookups may suddenly be different in
unexpected ways, and even produce results that cannot be deployed or will cause
data loss.  To give an account permissions to perform lookups against an
environment, without being able to deploy to it and make changes, run
`cdk bootstrap --trust-for-lookup=<account>`.

If you want to use lookups directly from the pipeline, you either need to accept
the risk of nondeterminism, or make sure you save and load the
`cdk.context.json` file somewhere between synth runs. Finally, you should
give the synth CodeBuild execution role permissions to assume the bootstrapped
lookup roles. As an example, doing so would look like this:

```python
pipelines.CodePipeline(self, "Pipeline",
    synth=pipelines.CodeBuildStep("Synth",
        input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
            connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
        ),
        commands=["...", "npm ci", "npm run build", "npx cdk synth", "..."
        ],
        role_policy_statements=[
            iam.PolicyStatement(
                actions=["sts:AssumeRole"],
                resources=["*"],
                conditions={
                    "StringEquals": {
                        "iam:ResourceTag/aws-cdk:bootstrap-role": "lookup"
                    }
                }
            )
        ]
    )
)
```

The above example requires that the target environments have all
been bootstrapped with bootstrap stack version `8`, released with
CDK CLI `1.114.0`.

## Security Considerations

It's important to stay safe while employing Continuous Delivery. The CDK Pipelines
library comes with secure defaults to the best of our ability, but by its
very nature the library cannot take care of everything.

We therefore expect you to mind the following:

* Maintain dependency hygiene and vet 3rd-party software you use. Any software you
  run on your build machine has the ability to change the infrastructure that gets
  deployed. Be careful with the software you depend on.
* Use dependency locking to prevent accidental upgrades! The default `CdkSynths` that
  come with CDK Pipelines will expect `package-lock.json` and `yarn.lock` to
  ensure your dependencies are the ones you expect.
* CDK Pipelines runs on resources created in your own account, and the configuration
  of those resources is controlled by developers submitting code through the pipeline.
  Therefore, CDK Pipelines by itself cannot protect against malicious
  developers trying to bypass compliance checks. If your threat model includes
  developers writing CDK code, you should have external compliance mechanisms in place like
  [AWS CloudFormation Hooks](https://aws.amazon.com/blogs/mt/proactively-keep-resources-secure-and-compliant-with-aws-cloudformation-hooks/)
  (preventive) or [AWS Config](https://aws.amazon.com/config/) (reactive) that
  the CloudFormation Execution Role does not have permissions to disable.
* Credentials to production environments should be short-lived. After
  bootstrapping and the initial pipeline provisioning, there is no more need for
  developers to have access to any of the account credentials; all further
  changes can be deployed through git. Avoid the chances of credentials leaking
  by not having them in the first place!

### Confirm permissions broadening

To keep tabs on the security impact of changes going out through your pipeline,
you can insert a security check before any stage deployment. This security check
will check if the upcoming deployment would add any new IAM permissions or
security group rules, and if so pause the pipeline and require you to confirm
the changes.

The security check will appear as two distinct actions in your pipeline: first
a CodeBuild project that runs `cdk diff` on the stage that's about to be deployed,
followed by a Manual Approval action that pauses the pipeline. If it so happens
that there no new IAM permissions or security group rules will be added by the deployment,
the manual approval step is automatically satisfied. The pipeline will look like this:

```txt
Pipeline
├── ...
├── MyApplicationStage
│    ├── MyApplicationSecurityCheck       // Security Diff Action
│    ├── MyApplicationManualApproval      // Manual Approval Action
│    ├── Stack.Prepare
│    └── Stack.Deploy
└── ...
```

You can insert the security check by using a `ConfirmPermissionsBroadening` step:

```python
# pipeline: pipelines.CodePipeline

stage = MyApplicationStage(self, "MyApplication")
pipeline.add_stage(stage,
    pre=[
        pipelines.ConfirmPermissionsBroadening("Check", stage=stage)
    ]
)
```

To get notified when there is a change that needs your manual approval,
create an SNS Topic, subscribe your own email address, and pass it in as
as the `notificationTopic` property:

```python
# pipeline: pipelines.CodePipeline

topic = sns.Topic(self, "SecurityChangesTopic")
topic.add_subscription(subscriptions.EmailSubscription("test@email.com"))

stage = MyApplicationStage(self, "MyApplication")
pipeline.add_stage(stage,
    pre=[
        pipelines.ConfirmPermissionsBroadening("Check",
            stage=stage,
            notification_topic=topic
        )
    ]
)
```

**Note**: Manual Approvals notifications only apply when an application has security
check enabled.

## Using a different deployment engine

CDK Pipelines supports multiple *deployment engines*, but this module vends a
construct for only one such engine: AWS CodePipeline. It is also possible to
use CDK Pipelines to build pipelines backed by other deployment engines.

Here is a list of CDK Libraries that integrate CDK Pipelines with
alternative deployment engines:

* GitHub Workflows: [`cdk-pipelines-github`](https://github.com/cdklabs/cdk-pipelines-github)

## Troubleshooting

Here are some common errors you may encounter while using this library.

### Pipeline: Internal Failure

If you see the following error during deployment of your pipeline:

```plaintext
CREATE_FAILED  | AWS::CodePipeline::Pipeline | Pipeline/Pipeline
Internal Failure
```

There's something wrong with your GitHub access token. It might be missing, or not have the
right permissions to access the repository you're trying to access.

### Key: Policy contains a statement with one or more invalid principals

If you see the following error during deployment of your pipeline:

```plaintext
CREATE_FAILED | AWS::KMS::Key | Pipeline/Pipeline/ArtifactsBucketEncryptionKey
Policy contains a statement with one or more invalid principals.
```

One of the target (account, region) environments has not been bootstrapped
with the new bootstrap stack. Check your target environments and make sure
they are all bootstrapped.

### Message: no matching base directory path found for cdk.out

If you see this error during the **Synth** step, it means that CodeBuild
is expecting to find a `cdk.out` directory in the root of your CodeBuild project,
but the directory wasn't there. There are two common causes for this:

* `cdk synth` is not being executed: `cdk synth` used to be run
  implicitly for you, but you now have to explicitly include the command.
  For NPM-based projects, add `npx cdk synth` to the end of the `commands`
  property, for other languages add `npm install -g aws-cdk` and `cdk synth`.
* Your CDK project lives in a subdirectory: you added a `cd <somedirectory>` command
  to the list of commands; don't forget to tell the `ScriptStep` about the
  different location of `cdk.out`, by passing `primaryOutputDirectory: '<somedirectory>/cdk.out'`.

### <Stack> is in ROLLBACK_COMPLETE state and can not be updated

If  you see the following error during execution of your pipeline:

```plaintext
Stack ... is in ROLLBACK_COMPLETE state and can not be updated. (Service:
AmazonCloudFormation; Status Code: 400; Error Code: ValidationError; Request
ID: ...)
```

The stack failed its previous deployment, and is in a non-retryable state.
Go into the CloudFormation console, delete the stack, and retry the deployment.

### Cannot find module 'xxxx' or its corresponding type declarations

You may see this if you are using TypeScript or other NPM-based languages,
when using NPM 7 on your workstation (where you generate `package-lock.json`)
and NPM 6 on the CodeBuild image used for synthesizing.

It looks like NPM 7 has started writing less information to `package-lock.json`,
leading NPM 6 reading that same file to not install all required packages anymore.

Make sure you are using the same NPM version everywhere, either downgrade your
workstation's version or upgrade the CodeBuild version.

### Cannot find module '.../check-node-version.js' (MODULE_NOT_FOUND)

The above error may be produced by `npx` when executing the CDK CLI, or any
project that uses the AWS SDK for JavaScript, without the target application
having been installed yet. For example, it can be triggered by `npx cdk synth`
if `aws-cdk` is not in your `package.json`.

Work around this by either installing the target application using NPM *before*
running `npx`, or set the environment variable `NPM_CONFIG_UNSAFE_PERM=true`.

### Cannot connect to the Docker daemon at unix:///var/run/docker.sock

If, in the 'Synth' action (inside the 'Build' stage) of your pipeline, you get an error like this:

```console
stderr: docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
```

It means that the AWS CodeBuild project for 'Synth' is not configured to run in privileged mode,
which prevents Docker builds from happening. This typically happens if you use a CDK construct
that bundles asset using tools run via Docker, like `aws-lambda-nodejs`, `aws-lambda-python`,
`aws-lambda-go` and others.

Make sure you set the `privileged` environment variable to `true` in the synth definition:

```python
source_artifact = codepipeline.Artifact()
cloud_assembly_artifact = codepipeline.Artifact()
pipeline = pipelines.CdkPipeline(self, "MyPipeline",
    cloud_assembly_artifact=cloud_assembly_artifact,
    synth_action=pipelines.SimpleSynthAction.standard_npm_synth(
        source_artifact=source_artifact,
        cloud_assembly_artifact=cloud_assembly_artifact,
        environment=codebuild.BuildEnvironment(
            privileged=True
        )
    )
)
```

After turning on `privilegedMode: true`, you will need to do a one-time manual cdk deploy of your
pipeline to get it going again (as with a broken 'synth' the pipeline will not be able to self
update to the right state).

### Not authorized to perform sts:AssumeRole on arn:aws:iam::*:role/*-lookup-role-*

You may get an error like the following in the **Synth** step:

```text
Could not assume role in target account using current credentials (which are for account 111111111111). User:
arn:aws:sts::111111111111:assumed-role/PipelineStack-PipelineBuildSynthCdkBuildProje-..../AWSCodeBuild-....
is not authorized to perform: sts:AssumeRole on resource:
arn:aws:iam::222222222222:role/cdk-hnb659fds-lookup-role-222222222222-us-east-1.
Please make sure that this role exists in the account. If it doesn't exist, (re)-bootstrap the environment with
the right '--trust', using the latest version of the CDK CLI.
```

This is a sign that the CLI is trying to do Context Lookups during the **Synth** step, which are failing
because it cannot assume the right role. We recommend you don't rely on Context Lookups in the pipeline at
all, and commit a file called `cdk.context.json` with the right lookup values in it to source control.

If you do want to do lookups in the pipeline, the cause is one of the following:

* The target environment has not been bootstrapped; OR
* The target environment has been bootstrapped without the right `--trust` relationship; OR
* The CodeBuild execution role does not have permissions to call `sts:AssumeRole`.

See the section called **Context Lookups** for more information on using this feature.

### IAM policies: Cannot exceed quota for PoliciesPerRole / Maximum policy size exceeded

This happens as a result of having a lot of targets in the Pipeline: the IAM policies that
get generated enumerate all required roles and grow too large.

Make sure you are on version `2.26.0` or higher, and that your `cdk.json` contains the
following:

```json
{
  "context": {
    "aws-cdk-lib/aws-iam:minimizePolicies": true
  }
}
```

### S3 error: Access Denied

An "S3 Access Denied" error can have two causes:

* Asset hashes have changed, but self-mutation has been disabled in the pipeline.
* You have deleted and recreated the bootstrap stack, or changed its qualifier.

#### Self-mutation step has been removed

Some constructs, such as EKS clusters, generate nested stacks. When CloudFormation tries
to deploy those stacks, it may fail with this error:

```console
S3 error: Access Denied For more information check http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html
```

This happens because the pipeline is not self-mutating and, as a consequence, the `FileAssetX`
build projects get out-of-sync with the generated templates. To fix this, make sure the
`selfMutating` property is set to `true`:

```python
cloud_assembly_artifact = codepipeline.Artifact()
pipeline = pipelines.CdkPipeline(self, "MyPipeline",
    self_mutating=True,
    cloud_assembly_artifact=cloud_assembly_artifact
)
```

#### Bootstrap roles have been renamed or recreated

While attempting to deploy an application stage, the "Prepare" or "Deploy" stage may fail with a cryptic error like:

`Action execution failed Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: 0123456ABCDEFGH; S3 Extended Request ID: 3hWcrVkhFGxfiMb/rTJO0Bk7Qn95x5ll4gyHiFsX6Pmk/NT+uX9+Z1moEcfkL7H3cjH7sWZfeD0=; Proxy: null)`

This generally indicates that the roles necessary to deploy have been deleted (or deleted and re-created);
for example, if the bootstrap stack has been deleted and re-created, this scenario will happen. Under the hood,
the resources that rely on these roles (e.g., `cdk-$qualifier-deploy-role-$account-$region`) point to different
canonical IDs than the recreated versions of these roles, which causes the errors. There are no simple solutions
to this issue, and for that reason we **strongly recommend** that bootstrap stacks not be deleted and re-created
once created.

The most automated way to solve the issue is to introduce a secondary bootstrap stack. By changing the qualifier
that the pipeline stack looks for, a change will be detected and the impacted policies and resources will be updated.
A hypothetical recovery workflow would look something like this:

* First, for all impacted environments, create a secondary bootstrap stack:

```sh
$ env CDK_NEW_BOOTSTRAP=1 npx cdk bootstrap \
    --qualifier random1234 \
    --toolkit-stack-name CDKToolkitTemp \
    aws://111111111111/us-east-1
```

* Update all impacted stacks in the pipeline to use this new qualifier.
  See https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html for more info.

```python
Stack(self, "MyStack",
    # Update this qualifier to match the one used above.
    synthesizer=cdk.DefaultStackSynthesizer(
        qualifier="randchars1234"
    )
)
```

* Deploy the updated stacks. This will update the stacks to use the roles created in the new bootstrap stack.
* (Optional) Restore back to the original state:

  * Revert the change made in step #2 above
  * Re-deploy the pipeline to use the original qualifier.
  * Delete the temporary bootstrap stack(s)

##### Manual Alternative

Alternatively, the errors can be resolved by finding each impacted resource and policy, and correcting the policies
by replacing the canonical IDs (e.g., `AROAYBRETNYCYV6ZF2R93`) with the appropriate ARNs. As an example, the KMS
encryption key policy for the artifacts bucket may have a statement that looks like the following:

```json
{
  "Effect" : "Allow",
  "Principal" : {
    // "AWS" : "AROAYBRETNYCYV6ZF2R93"  // Indicates this issue; replace this value
    "AWS": "arn:aws:iam::0123456789012:role/cdk-hnb659fds-deploy-role-0123456789012-eu-west-1", // Correct value
  },
  "Action" : [ "kms:Decrypt", "kms:DescribeKey" ],
  "Resource" : "*"
}
```

Any resource or policy that references the qualifier (`hnb659fds` by default) will need to be updated.

### This CDK CLI is not compatible with the CDK library used by your application

The CDK CLI version used in your pipeline is too old to read the Cloud Assembly
produced by your CDK app.

Most likely this happens in the `SelfMutate` action, you are passing the `cliVersion`
parameter to control the version of the CDK CLI, and you just updated the CDK
framework version that your application uses. You either forgot to change the
`cliVersion` parameter, or changed the `cliVersion` in the same commit in which
you changed the framework version. Because a change to the pipeline settings needs
a successful run of the `SelfMutate` step to be applied, the next iteration of the
`SelfMutate` step still executes with the *old* CLI version, and that old CLI version
is not able to read the cloud assembly produced by the new framework version.

Solution: change the `cliVersion` first, commit, push and deploy, and only then
change the framework version.

We recommend you avoid specifying the `cliVersion` parameter at all. By default
the pipeline will use the latest CLI version, which will support all cloud assembly
versions.

## Using Drop-in Docker Replacements

By default, the AWS CDK will build and publish Docker image assets using the
`docker` command. However, by specifying the `CDK_DOCKER` environment variable,
you can override the command that will be used to build and publish your
assets.

In CDK Pipelines, the drop-in replacement for the `docker` command must be
included in the CodeBuild environment and configured for your pipeline.

### Adding to the default CodeBuild image

You can add a drop-in Docker replacement command to the default CodeBuild
environment by adding install-phase commands that encode how to install
your tooling and by adding the `CDK_DOCKER` environment variable to your
build environment.

```python
# source: pipelines.IFileSetProducer # the repository source
# synth_commands: List[str] # Commands to synthesize your app
# install_commands: List[str]
# Commands to install your toolchain

pipeline = pipelines.CodePipeline(self, "Pipeline",
    # Standard CodePipeline properties...
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=synth_commands
    ),

    # Configure CodeBuild to use a drop-in Docker replacement.
    code_build_defaults=pipelines.CodeBuildOptions(
        partial_build_spec=codebuild.BuildSpec.from_object({
            "phases": {
                "install": {
                    # Add the shell commands to install your drop-in Docker
                    # replacement to the CodeBuild enviromment.
                    "commands": install_commands
                }
            }
        }),
        build_environment=codebuild.BuildEnvironment(
            environment_variables={
                # Instruct the AWS CDK to use `drop-in-replacement` instead of
                # `docker` when building / publishing docker images.
                # e.g., `drop-in-replacement build . -f path/to/Dockerfile`
                "CDK_DOCKER": codebuild.BuildEnvironmentVariable(value="drop-in-replacement")
            }
        )
    )
)
```

### Using a custom build image

If you're using a custom build image in CodeBuild, you can override the
command the AWS CDK uses to build Docker images by providing `CDK_DOCKER` as
an `ENV` in your `Dockerfile` or by providing the environment variable in the
pipeline as shown below.

```python
# source: pipelines.IFileSetProducer # the repository source
# synth_commands: List[str]
# Commands to synthesize your app

pipeline = pipelines.CodePipeline(self, "Pipeline",
    # Standard CodePipeline properties...
    synth=pipelines.ShellStep("Synth",
        input=source,
        commands=synth_commands
    ),

    # Configure CodeBuild to use a drop-in Docker replacement.
    code_build_defaults=pipelines.CodeBuildOptions(
        build_environment=codebuild.BuildEnvironment(
            # Provide a custom build image containing your toolchain and the
            # pre-installed replacement for the `docker` command.
            build_image=codebuild.LinuxBuildImage.from_docker_registry("your-docker-registry"),
            environment_variables={
                # If you haven't provided an `ENV` in your Dockerfile that overrides
                # `CDK_DOCKER`, then you must provide the name of the command that
                # the AWS CDK should run instead of `docker` here.
                "CDK_DOCKER": codebuild.BuildEnvironmentVariable(value="drop-in-replacement")
            }
        )
    )
)
```

## Known Issues

There are some usability issues that are caused by underlying technology, and
cannot be remedied by CDK at this point. They are reproduced here for completeness.

* **Console links to other accounts will not work**: the AWS CodePipeline
  console will assume all links are relative to the current account. You will
  not be able to use the pipeline console to click through to a CloudFormation
  stack in a different account.
* **If a change set failed to apply the pipeline must be restarted**: if a change
  set failed to apply, it cannot be retried. The pipeline must be restarted from
  the top by clicking **Release Change**.
* **A stack that failed to create must be deleted manually**: if a stack
  failed to create on the first attempt, you must delete it using the
  CloudFormation console before starting the pipeline again by clicking
  **Release Change**.
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
    CfnOutput as _CfnOutput_7273f911,
    Duration as _Duration_4839e8c3,
    SecretValue as _SecretValue_3dd0ddae,
    Stack as _Stack_2866e57f,
    Stage as _Stage_7df8511b,
)
from ..aws_codebuild import (
    BuildEnvironment as _BuildEnvironment_4ee6fb51,
    BuildSpec as _BuildSpec_4961ea5b,
    Cache as _Cache_ed12d453,
    IFileSystemLocation as _IFileSystemLocation_acb87263,
    IProject as _IProject_aafae30a,
    LoggingOptions as _LoggingOptions_31668710,
)
from ..aws_codecommit import IRepository as _IRepository_e7c062a1
from ..aws_codepipeline import (
    Artifact as _Artifact_0cb05964,
    IStage as _IStage_415fc571,
    Pipeline as _Pipeline_ea38de84,
)
from ..aws_codepipeline_actions import (
    Action as _Action_20e074ce,
    CodeCommitTrigger as _CodeCommitTrigger_e1096919,
    GitHubTrigger as _GitHubTrigger_0029a9bb,
    S3Trigger as _S3Trigger_3ab49ad8,
)
from ..aws_ec2 import (
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_ecr import IRepository as _IRepository_e6004aa6
from ..aws_iam import (
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_s3 import IBucket as _IBucket_42e086fd
from ..aws_secretsmanager import ISecret as _ISecret_6e020e6a
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..cx_api import (
    CloudFormationStackArtifact as _CloudFormationStackArtifact_97533dc8
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.AddStageOpts",
    jsii_struct_bases=[],
    name_mapping={"post": "post", "pre": "pre", "stack_steps": "stackSteps"},
)
class AddStageOpts:
    def __init__(
        self,
        *,
        post: typing.Optional[typing.Sequence["Step"]] = None,
        pre: typing.Optional[typing.Sequence["Step"]] = None,
        stack_steps: typing.Optional[typing.Sequence[typing.Union["StackSteps", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Options to pass to ``addStage``.

        :param post: Additional steps to run after all of the stacks in the stage. Default: - No additional steps
        :param pre: Additional steps to run before any of the stacks in the stage. Default: - No additional steps
        :param stack_steps: Instructions for stack level steps. Default: - No additional instructions

        :exampleMetadata: infused

        Example::

            # pipeline: pipelines.CodePipeline
            
            preprod = MyApplicationStage(self, "PreProd")
            prod = MyApplicationStage(self, "Prod")
            
            pipeline.add_stage(preprod,
                post=[
                    pipelines.ShellStep("Validate Endpoint",
                        commands=["curl -Ssf https://my.webservice.com/"]
                    )
                ]
            )
            pipeline.add_stage(prod,
                pre=[
                    pipelines.ManualApprovalStep("PromoteToProd")
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b9c1bc74292ecb27724ef07a41dc8f1b1ee5d9dc268940f2ec578982b596b0a)
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
            check_type(argname="argument pre", value=pre, expected_type=type_hints["pre"])
            check_type(argname="argument stack_steps", value=stack_steps, expected_type=type_hints["stack_steps"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if post is not None:
            self._values["post"] = post
        if pre is not None:
            self._values["pre"] = pre
        if stack_steps is not None:
            self._values["stack_steps"] = stack_steps

    @builtins.property
    def post(self) -> typing.Optional[typing.List["Step"]]:
        '''Additional steps to run after all of the stacks in the stage.

        :default: - No additional steps
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    @builtins.property
    def pre(self) -> typing.Optional[typing.List["Step"]]:
        '''Additional steps to run before any of the stacks in the stage.

        :default: - No additional steps
        '''
        result = self._values.get("pre")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    @builtins.property
    def stack_steps(self) -> typing.Optional[typing.List["StackSteps"]]:
        '''Instructions for stack level steps.

        :default: - No additional instructions
        '''
        result = self._values.get("stack_steps")
        return typing.cast(typing.Optional[typing.List["StackSteps"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddStageOpts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ArtifactMap(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.ArtifactMap",
):
    '''Translate FileSets to CodePipeline Artifacts.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import pipelines
        
        artifact_map = pipelines.ArtifactMap()
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toCodePipeline")
    def to_code_pipeline(self, x: "FileSet") -> _Artifact_0cb05964:
        '''Return the matching CodePipeline artifact for a FileSet.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25e392fc366b5e854a4d6ec5bf897ab0e51d041c4eae3089a12ab36474918e1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(_Artifact_0cb05964, jsii.invoke(self, "toCodePipeline", [x]))


@jsii.enum(jsii_type="aws-cdk-lib.pipelines.AssetType")
class AssetType(enum.Enum):
    '''Type of the asset that is being published.'''

    FILE = "FILE"
    '''A file.'''
    DOCKER_IMAGE = "DOCKER_IMAGE"
    '''A Docker image.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.CodeBuildOptions",
    jsii_struct_bases=[],
    name_mapping={
        "build_environment": "buildEnvironment",
        "cache": "cache",
        "file_system_locations": "fileSystemLocations",
        "logging": "logging",
        "partial_build_spec": "partialBuildSpec",
        "role_policy": "rolePolicy",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class CodeBuildOptions:
    def __init__(
        self,
        *,
        build_environment: typing.Optional[typing.Union[_BuildEnvironment_4ee6fb51, typing.Dict[builtins.str, typing.Any]]] = None,
        cache: typing.Optional[_Cache_ed12d453] = None,
        file_system_locations: typing.Optional[typing.Sequence[_IFileSystemLocation_acb87263]] = None,
        logging: typing.Optional[typing.Union[_LoggingOptions_31668710, typing.Dict[builtins.str, typing.Any]]] = None,
        partial_build_spec: typing.Optional[_BuildSpec_4961ea5b] = None,
        role_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
    ) -> None:
        '''Options for customizing a single CodeBuild project.

        :param build_environment: Partial build environment, will be combined with other build environments that apply. Default: - Non-privileged build, SMALL instance, LinuxBuildImage.STANDARD_7_0
        :param cache: Caching strategy to use. Default: - No cache
        :param file_system_locations: ProjectFileSystemLocation objects for CodeBuild build projects. A ProjectFileSystemLocation object specifies the identifier, location, mountOptions, mountPoint, and type of a file system created using Amazon Elastic File System. Requires a vpc to be set and privileged to be set to true. Default: - no file system locations
        :param logging: Information about logs for CodeBuild projects. A CodeBuild project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both. Default: - no log configuration is set
        :param partial_build_spec: Partial buildspec, will be combined with other buildspecs that apply. The BuildSpec must be available inline--it cannot reference a file on disk. Default: - No initial BuildSpec
        :param role_policy: Policy statements to add to role. Default: - No policy statements added to CodeBuild Project Role
        :param security_groups: Which security group(s) to associate with the project network interfaces. Only used if 'vpc' is supplied. Default: - Security group will be automatically created.
        :param subnet_selection: Which subnets to use. Only used if 'vpc' is supplied. Default: - All private subnets.
        :param timeout: The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: The VPC where to create the CodeBuild network interfaces in. Default: - No VPC

        :exampleMetadata: infused

        Example::

            # source: pipelines.IFileSetProducer # the repository source
            # synth_commands: List[str] # Commands to synthesize your app
            # install_commands: List[str]
            # Commands to install your toolchain
            
            pipeline = pipelines.CodePipeline(self, "Pipeline",
                # Standard CodePipeline properties...
                synth=pipelines.ShellStep("Synth",
                    input=source,
                    commands=synth_commands
                ),
            
                # Configure CodeBuild to use a drop-in Docker replacement.
                code_build_defaults=pipelines.CodeBuildOptions(
                    partial_build_spec=codebuild.BuildSpec.from_object({
                        "phases": {
                            "install": {
                                # Add the shell commands to install your drop-in Docker
                                # replacement to the CodeBuild enviromment.
                                "commands": install_commands
                            }
                        }
                    }),
                    build_environment=codebuild.BuildEnvironment(
                        environment_variables={
                            # Instruct the AWS CDK to use `drop-in-replacement` instead of
                            # `docker` when building / publishing docker images.
                            # e.g., `drop-in-replacement build . -f path/to/Dockerfile`
                            "CDK_DOCKER": codebuild.BuildEnvironmentVariable(value="drop-in-replacement")
                        }
                    )
                )
            )
        '''
        if isinstance(build_environment, dict):
            build_environment = _BuildEnvironment_4ee6fb51(**build_environment)
        if isinstance(logging, dict):
            logging = _LoggingOptions_31668710(**logging)
        if isinstance(subnet_selection, dict):
            subnet_selection = _SubnetSelection_e57d76df(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb14d0bc2bb7087520a3769dfb10a8c874fa4227208104c933f686486beec01c)
            check_type(argname="argument build_environment", value=build_environment, expected_type=type_hints["build_environment"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument file_system_locations", value=file_system_locations, expected_type=type_hints["file_system_locations"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument partial_build_spec", value=partial_build_spec, expected_type=type_hints["partial_build_spec"])
            check_type(argname="argument role_policy", value=role_policy, expected_type=type_hints["role_policy"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if build_environment is not None:
            self._values["build_environment"] = build_environment
        if cache is not None:
            self._values["cache"] = cache
        if file_system_locations is not None:
            self._values["file_system_locations"] = file_system_locations
        if logging is not None:
            self._values["logging"] = logging
        if partial_build_spec is not None:
            self._values["partial_build_spec"] = partial_build_spec
        if role_policy is not None:
            self._values["role_policy"] = role_policy
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def build_environment(self) -> typing.Optional[_BuildEnvironment_4ee6fb51]:
        '''Partial build environment, will be combined with other build environments that apply.

        :default: - Non-privileged build, SMALL instance, LinuxBuildImage.STANDARD_7_0
        '''
        result = self._values.get("build_environment")
        return typing.cast(typing.Optional[_BuildEnvironment_4ee6fb51], result)

    @builtins.property
    def cache(self) -> typing.Optional[_Cache_ed12d453]:
        '''Caching strategy to use.

        :default: - No cache
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[_Cache_ed12d453], result)

    @builtins.property
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.List[_IFileSystemLocation_acb87263]]:
        '''ProjectFileSystemLocation objects for CodeBuild build projects.

        A ProjectFileSystemLocation object specifies the identifier, location, mountOptions, mountPoint,
        and type of a file system created using Amazon Elastic File System.
        Requires a vpc to be set and privileged to be set to true.

        :default: - no file system locations
        '''
        result = self._values.get("file_system_locations")
        return typing.cast(typing.Optional[typing.List[_IFileSystemLocation_acb87263]], result)

    @builtins.property
    def logging(self) -> typing.Optional[_LoggingOptions_31668710]:
        '''Information about logs for CodeBuild projects.

        A CodeBuild project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both.

        :default: - no log configuration is set
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[_LoggingOptions_31668710], result)

    @builtins.property
    def partial_build_spec(self) -> typing.Optional[_BuildSpec_4961ea5b]:
        '''Partial buildspec, will be combined with other buildspecs that apply.

        The BuildSpec must be available inline--it cannot reference a file
        on disk.

        :default: - No initial BuildSpec
        '''
        result = self._values.get("partial_build_spec")
        return typing.cast(typing.Optional[_BuildSpec_4961ea5b], result)

    @builtins.property
    def role_policy(self) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Policy statements to add to role.

        :default: - No policy statements added to CodeBuild Project Role
        '''
        result = self._values.get("role_policy")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''Which security group(s) to associate with the project network interfaces.

        Only used if 'vpc' is supplied.

        :default: - Security group will be automatically created.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Which subnets to use.

        Only used if 'vpc' is supplied.

        :default: - All private subnets.
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The VPC where to create the CodeBuild network interfaces in.

        :default: - No VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.CodeCommitSourceOptions",
    jsii_struct_bases=[],
    name_mapping={
        "action_name": "actionName",
        "code_build_clone_output": "codeBuildCloneOutput",
        "event_role": "eventRole",
        "trigger": "trigger",
    },
)
class CodeCommitSourceOptions:
    def __init__(
        self,
        *,
        action_name: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        trigger: typing.Optional[_CodeCommitTrigger_e1096919] = None,
    ) -> None:
        '''Configuration options for a CodeCommit source.

        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository name
        :param code_build_clone_output: If this is set, the next CodeBuild job clones the repository (instead of CodePipeline downloading the files). This provides access to repository history, and retains symlinks (symlinks would otherwise be removed by CodePipeline). **Note**: if this option is true, only CodeBuild jobs can use the output artifact. Default: false
        :param event_role: Role to be used by on commit event rule. Used only when trigger value is CodeCommitTrigger.EVENTS. Default: a new role will be created.
        :param trigger: How should CodePipeline detect source changes for this Action. Default: CodeCommitTrigger.EVENTS

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            from aws_cdk import aws_iam as iam
            from aws_cdk import pipelines
            
            # role: iam.Role
            
            code_commit_source_options = pipelines.CodeCommitSourceOptions(
                action_name="actionName",
                code_build_clone_output=False,
                event_role=role,
                trigger=codepipeline_actions.CodeCommitTrigger.NONE
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e17ff0fc6dc5e2614664c26c6bd947f6c7d12e7871a3cb4f169cdb8abc431ab0)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument code_build_clone_output", value=code_build_clone_output, expected_type=type_hints["code_build_clone_output"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action_name is not None:
            self._values["action_name"] = action_name
        if code_build_clone_output is not None:
            self._values["code_build_clone_output"] = code_build_clone_output
        if event_role is not None:
            self._values["event_role"] = event_role
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The action name used for this source in the CodePipeline.

        :default: - The repository name
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_build_clone_output(self) -> typing.Optional[builtins.bool]:
        '''If this is set, the next CodeBuild job clones the repository (instead of CodePipeline downloading the files).

        This provides access to repository history, and retains symlinks (symlinks would otherwise be
        removed by CodePipeline).

        **Note**: if this option is true, only CodeBuild jobs can use the output artifact.

        :default: false

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeCommit.html
        '''
        result = self._values.get("code_build_clone_output")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Role to be used by on commit event rule.

        Used only when trigger value is CodeCommitTrigger.EVENTS.

        :default: a new role will be created.
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def trigger(self) -> typing.Optional[_CodeCommitTrigger_e1096919]:
        '''How should CodePipeline detect source changes for this Action.

        :default: CodeCommitTrigger.EVENTS
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional[_CodeCommitTrigger_e1096919], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeCommitSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.CodePipelineActionFactoryResult",
    jsii_struct_bases=[],
    name_mapping={"run_orders_consumed": "runOrdersConsumed", "project": "project"},
)
class CodePipelineActionFactoryResult:
    def __init__(
        self,
        *,
        run_orders_consumed: jsii.Number,
        project: typing.Optional[_IProject_aafae30a] = None,
    ) -> None:
        '''The result of adding actions to the pipeline.

        :param run_orders_consumed: How many RunOrders were consumed. If you add 1 action, return the value 1 here.
        :param project: If a CodeBuild project got created, the project. Default: - This factory did not create a CodeBuild project

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codebuild as codebuild
            from aws_cdk import pipelines
            
            # project: codebuild.Project
            
            code_pipeline_action_factory_result = pipelines.CodePipelineActionFactoryResult(
                run_orders_consumed=123,
            
                # the properties below are optional
                project=project
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9624d5022538eedc98a469f78de5916fac4ee13ff0d2f5f9a5e9d447ce9f909f)
            check_type(argname="argument run_orders_consumed", value=run_orders_consumed, expected_type=type_hints["run_orders_consumed"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "run_orders_consumed": run_orders_consumed,
        }
        if project is not None:
            self._values["project"] = project

    @builtins.property
    def run_orders_consumed(self) -> jsii.Number:
        '''How many RunOrders were consumed.

        If you add 1 action, return the value 1 here.
        '''
        result = self._values.get("run_orders_consumed")
        assert result is not None, "Required property 'run_orders_consumed' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def project(self) -> typing.Optional[_IProject_aafae30a]:
        '''If a CodeBuild project got created, the project.

        :default: - This factory did not create a CodeBuild project
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[_IProject_aafae30a], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineActionFactoryResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.CodePipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "synth": "synth",
        "artifact_bucket": "artifactBucket",
        "asset_publishing_code_build_defaults": "assetPublishingCodeBuildDefaults",
        "cli_version": "cliVersion",
        "code_build_defaults": "codeBuildDefaults",
        "code_pipeline": "codePipeline",
        "cross_account_keys": "crossAccountKeys",
        "cross_region_replication_buckets": "crossRegionReplicationBuckets",
        "docker_credentials": "dockerCredentials",
        "docker_enabled_for_self_mutation": "dockerEnabledForSelfMutation",
        "docker_enabled_for_synth": "dockerEnabledForSynth",
        "enable_key_rotation": "enableKeyRotation",
        "pipeline_name": "pipelineName",
        "publish_assets_in_parallel": "publishAssetsInParallel",
        "reuse_cross_region_support_stacks": "reuseCrossRegionSupportStacks",
        "role": "role",
        "self_mutation": "selfMutation",
        "self_mutation_code_build_defaults": "selfMutationCodeBuildDefaults",
        "synth_code_build_defaults": "synthCodeBuildDefaults",
        "use_change_sets": "useChangeSets",
    },
)
class CodePipelineProps:
    def __init__(
        self,
        *,
        synth: "IFileSetProducer",
        artifact_bucket: typing.Optional[_IBucket_42e086fd] = None,
        asset_publishing_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cli_version: typing.Optional[builtins.str] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        code_pipeline: typing.Optional[_Pipeline_ea38de84] = None,
        cross_account_keys: typing.Optional[builtins.bool] = None,
        cross_region_replication_buckets: typing.Optional[typing.Mapping[builtins.str, _IBucket_42e086fd]] = None,
        docker_credentials: typing.Optional[typing.Sequence["DockerCredential"]] = None,
        docker_enabled_for_self_mutation: typing.Optional[builtins.bool] = None,
        docker_enabled_for_synth: typing.Optional[builtins.bool] = None,
        enable_key_rotation: typing.Optional[builtins.bool] = None,
        pipeline_name: typing.Optional[builtins.str] = None,
        publish_assets_in_parallel: typing.Optional[builtins.bool] = None,
        reuse_cross_region_support_stacks: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        self_mutation: typing.Optional[builtins.bool] = None,
        self_mutation_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        synth_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        use_change_sets: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for a ``CodePipeline``.

        :param synth: The build step that produces the CDK Cloud Assembly. The primary output of this step needs to be the ``cdk.out`` directory generated by the ``cdk synth`` command. If you use a ``ShellStep`` here and you don't configure an output directory, the output directory will automatically be assumed to be ``cdk.out``.
        :param artifact_bucket: An existing S3 Bucket to use for storing the pipeline's artifact. Default: - A new S3 bucket will be created.
        :param asset_publishing_code_build_defaults: Additional customizations to apply to the asset publishing CodeBuild projects. Default: - Only ``codeBuildDefaults`` are applied
        :param cli_version: CDK CLI version to use in self-mutation and asset publishing steps. If you want to lock the CDK CLI version used in the pipeline, by steps that are automatically generated for you, specify the version here. We recommend you do not specify this value, as not specifying it always uses the latest CLI version which is backwards compatible with old versions. If you do specify it, be aware that this version should always be equal to or higher than the version of the CDK framework used by the CDK app, when the CDK commands are run during your pipeline execution. When you change this version, the *next time* the ``SelfMutate`` step runs it will still be using the CLI of the the *previous* version that was in this property: it will only start using the new version after ``SelfMutate`` completes successfully. That means that if you want to update both framework and CLI version, you should update the CLI version first, commit, push and deploy, and only then update the framework version. Default: - Latest version
        :param code_build_defaults: Customize the CodeBuild projects created for this pipeline. Default: - All projects run non-privileged build, SMALL instance, LinuxBuildImage.STANDARD_7_0
        :param code_pipeline: An existing Pipeline to be reused and built upon. [disable-awslint:ref-via-interface] Default: - a new underlying pipeline is created.
        :param cross_account_keys: Create KMS keys for the artifact buckets, allowing cross-account deployments. The artifact buckets have to be encrypted to support deploying CDK apps to another account, so if you want to do that or want to have your artifact buckets encrypted, be sure to set this value to ``true``. Be aware there is a cost associated with maintaining the KMS keys. Default: false
        :param cross_region_replication_buckets: A map of region to S3 bucket name used for cross-region CodePipeline. For every Action that you specify targeting a different region than the Pipeline itself, if you don't provide an explicit Bucket for that region using this property, the construct will automatically create a Stack containing an S3 Bucket in that region. Passed directly through to the {@link cp.Pipeline}. Default: - no cross region replication buckets.
        :param docker_credentials: A list of credentials used to authenticate to Docker registries. Specify any credentials necessary within the pipeline to build, synth, update, or publish assets. Default: []
        :param docker_enabled_for_self_mutation: Enable Docker for the self-mutate step. Set this to true if the pipeline itself uses Docker container assets (for example, if you use ``LinuxBuildImage.fromAsset()`` as the build image of a CodeBuild step in the pipeline). You do not need to set it if you build Docker image assets in the application Stages and Stacks that are *deployed* by this pipeline. Configures privileged mode for the self-mutation CodeBuild action. If you are about to turn this on in an already-deployed Pipeline, set the value to ``true`` first, commit and allow the pipeline to self-update, and only then use the Docker asset in the pipeline. Default: false
        :param docker_enabled_for_synth: Enable Docker for the 'synth' step. Set this to true if you are using file assets that require "bundling" anywhere in your application (meaning an asset compilation step will be run with the tools provided by a Docker image), both for the Pipeline stack as well as the application stacks. A common way to use bundling assets in your application is by using the ``aws-cdk-lib/aws-lambda-nodejs`` library. Configures privileged mode for the synth CodeBuild action. If you are about to turn this on in an already-deployed Pipeline, set the value to ``true`` first, commit and allow the pipeline to self-update, and only then use the bundled asset. Default: false
        :param enable_key_rotation: Enable KMS key rotation for the generated KMS keys. By default KMS key rotation is disabled, but will add additional costs when enabled. Default: - false (key rotation is disabled)
        :param pipeline_name: The name of the CodePipeline pipeline. Default: - Automatically generated
        :param publish_assets_in_parallel: Publish assets in multiple CodeBuild projects. If set to false, use one Project per type to publish all assets. Publishing in parallel improves concurrency and may reduce publishing latency, but may also increase overall provisioning time of the CodeBuild projects. Experiment and see what value works best for you. Default: true
        :param reuse_cross_region_support_stacks: Reuse the same cross region support stack for all pipelines in the App. Default: - true (Use the same support stack for all pipelines in App)
        :param role: The IAM role to be assumed by this Pipeline. Default: - A new role is created
        :param self_mutation: Whether the pipeline will update itself. This needs to be set to ``true`` to allow the pipeline to reconfigure itself when assets or stages are being added to it, and ``true`` is the recommended setting. You can temporarily set this to ``false`` while you are iterating on the pipeline itself and prefer to deploy changes using ``cdk deploy``. Default: true
        :param self_mutation_code_build_defaults: Additional customizations to apply to the self mutation CodeBuild projects. Default: - Only ``codeBuildDefaults`` are applied
        :param synth_code_build_defaults: Additional customizations to apply to the synthesize CodeBuild projects. Default: - Only ``codeBuildDefaults`` are applied
        :param use_change_sets: Deploy every stack by creating a change set and executing it. When enabled, creates a "Prepare" and "Execute" action for each stack. Disable to deploy the stack in one pipeline action. Default: true

        :exampleMetadata: infused

        Example::

            # Modern API
            modern_pipeline = pipelines.CodePipeline(self, "Pipeline",
                self_mutation=False,
                synth=pipelines.ShellStep("Synth",
                    input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                        connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                    ),
                    commands=["npm ci", "npm run build", "npx cdk synth"
                    ]
                )
            )
            
            # Original API
            cloud_assembly_artifact = codepipeline.Artifact()
            original_pipeline = pipelines.CdkPipeline(self, "Pipeline",
                self_mutating=False,
                cloud_assembly_artifact=cloud_assembly_artifact
            )
        '''
        if isinstance(asset_publishing_code_build_defaults, dict):
            asset_publishing_code_build_defaults = CodeBuildOptions(**asset_publishing_code_build_defaults)
        if isinstance(code_build_defaults, dict):
            code_build_defaults = CodeBuildOptions(**code_build_defaults)
        if isinstance(self_mutation_code_build_defaults, dict):
            self_mutation_code_build_defaults = CodeBuildOptions(**self_mutation_code_build_defaults)
        if isinstance(synth_code_build_defaults, dict):
            synth_code_build_defaults = CodeBuildOptions(**synth_code_build_defaults)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c46bc21ca63efb27c935c31017ebbc8c85b3b93ae1798e54892dd3eae41d99aa)
            check_type(argname="argument synth", value=synth, expected_type=type_hints["synth"])
            check_type(argname="argument artifact_bucket", value=artifact_bucket, expected_type=type_hints["artifact_bucket"])
            check_type(argname="argument asset_publishing_code_build_defaults", value=asset_publishing_code_build_defaults, expected_type=type_hints["asset_publishing_code_build_defaults"])
            check_type(argname="argument cli_version", value=cli_version, expected_type=type_hints["cli_version"])
            check_type(argname="argument code_build_defaults", value=code_build_defaults, expected_type=type_hints["code_build_defaults"])
            check_type(argname="argument code_pipeline", value=code_pipeline, expected_type=type_hints["code_pipeline"])
            check_type(argname="argument cross_account_keys", value=cross_account_keys, expected_type=type_hints["cross_account_keys"])
            check_type(argname="argument cross_region_replication_buckets", value=cross_region_replication_buckets, expected_type=type_hints["cross_region_replication_buckets"])
            check_type(argname="argument docker_credentials", value=docker_credentials, expected_type=type_hints["docker_credentials"])
            check_type(argname="argument docker_enabled_for_self_mutation", value=docker_enabled_for_self_mutation, expected_type=type_hints["docker_enabled_for_self_mutation"])
            check_type(argname="argument docker_enabled_for_synth", value=docker_enabled_for_synth, expected_type=type_hints["docker_enabled_for_synth"])
            check_type(argname="argument enable_key_rotation", value=enable_key_rotation, expected_type=type_hints["enable_key_rotation"])
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
            check_type(argname="argument publish_assets_in_parallel", value=publish_assets_in_parallel, expected_type=type_hints["publish_assets_in_parallel"])
            check_type(argname="argument reuse_cross_region_support_stacks", value=reuse_cross_region_support_stacks, expected_type=type_hints["reuse_cross_region_support_stacks"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument self_mutation", value=self_mutation, expected_type=type_hints["self_mutation"])
            check_type(argname="argument self_mutation_code_build_defaults", value=self_mutation_code_build_defaults, expected_type=type_hints["self_mutation_code_build_defaults"])
            check_type(argname="argument synth_code_build_defaults", value=synth_code_build_defaults, expected_type=type_hints["synth_code_build_defaults"])
            check_type(argname="argument use_change_sets", value=use_change_sets, expected_type=type_hints["use_change_sets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "synth": synth,
        }
        if artifact_bucket is not None:
            self._values["artifact_bucket"] = artifact_bucket
        if asset_publishing_code_build_defaults is not None:
            self._values["asset_publishing_code_build_defaults"] = asset_publishing_code_build_defaults
        if cli_version is not None:
            self._values["cli_version"] = cli_version
        if code_build_defaults is not None:
            self._values["code_build_defaults"] = code_build_defaults
        if code_pipeline is not None:
            self._values["code_pipeline"] = code_pipeline
        if cross_account_keys is not None:
            self._values["cross_account_keys"] = cross_account_keys
        if cross_region_replication_buckets is not None:
            self._values["cross_region_replication_buckets"] = cross_region_replication_buckets
        if docker_credentials is not None:
            self._values["docker_credentials"] = docker_credentials
        if docker_enabled_for_self_mutation is not None:
            self._values["docker_enabled_for_self_mutation"] = docker_enabled_for_self_mutation
        if docker_enabled_for_synth is not None:
            self._values["docker_enabled_for_synth"] = docker_enabled_for_synth
        if enable_key_rotation is not None:
            self._values["enable_key_rotation"] = enable_key_rotation
        if pipeline_name is not None:
            self._values["pipeline_name"] = pipeline_name
        if publish_assets_in_parallel is not None:
            self._values["publish_assets_in_parallel"] = publish_assets_in_parallel
        if reuse_cross_region_support_stacks is not None:
            self._values["reuse_cross_region_support_stacks"] = reuse_cross_region_support_stacks
        if role is not None:
            self._values["role"] = role
        if self_mutation is not None:
            self._values["self_mutation"] = self_mutation
        if self_mutation_code_build_defaults is not None:
            self._values["self_mutation_code_build_defaults"] = self_mutation_code_build_defaults
        if synth_code_build_defaults is not None:
            self._values["synth_code_build_defaults"] = synth_code_build_defaults
        if use_change_sets is not None:
            self._values["use_change_sets"] = use_change_sets

    @builtins.property
    def synth(self) -> "IFileSetProducer":
        '''The build step that produces the CDK Cloud Assembly.

        The primary output of this step needs to be the ``cdk.out`` directory
        generated by the ``cdk synth`` command.

        If you use a ``ShellStep`` here and you don't configure an output directory,
        the output directory will automatically be assumed to be ``cdk.out``.
        '''
        result = self._values.get("synth")
        assert result is not None, "Required property 'synth' is missing"
        return typing.cast("IFileSetProducer", result)

    @builtins.property
    def artifact_bucket(self) -> typing.Optional[_IBucket_42e086fd]:
        '''An existing S3 Bucket to use for storing the pipeline's artifact.

        :default: - A new S3 bucket will be created.
        '''
        result = self._values.get("artifact_bucket")
        return typing.cast(typing.Optional[_IBucket_42e086fd], result)

    @builtins.property
    def asset_publishing_code_build_defaults(self) -> typing.Optional[CodeBuildOptions]:
        '''Additional customizations to apply to the asset publishing CodeBuild projects.

        :default: - Only ``codeBuildDefaults`` are applied
        '''
        result = self._values.get("asset_publishing_code_build_defaults")
        return typing.cast(typing.Optional[CodeBuildOptions], result)

    @builtins.property
    def cli_version(self) -> typing.Optional[builtins.str]:
        '''CDK CLI version to use in self-mutation and asset publishing steps.

        If you want to lock the CDK CLI version used in the pipeline, by steps
        that are automatically generated for you, specify the version here.

        We recommend you do not specify this value, as not specifying it always
        uses the latest CLI version which is backwards compatible with old versions.

        If you do specify it, be aware that this version should always be equal to or higher than the
        version of the CDK framework used by the CDK app, when the CDK commands are
        run during your pipeline execution. When you change this version, the *next
        time* the ``SelfMutate`` step runs it will still be using the CLI of the the
        *previous* version that was in this property: it will only start using the
        new version after ``SelfMutate`` completes successfully. That means that if
        you want to update both framework and CLI version, you should update the
        CLI version first, commit, push and deploy, and only then update the
        framework version.

        :default: - Latest version
        '''
        result = self._values.get("cli_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_build_defaults(self) -> typing.Optional[CodeBuildOptions]:
        '''Customize the CodeBuild projects created for this pipeline.

        :default: - All projects run non-privileged build, SMALL instance, LinuxBuildImage.STANDARD_7_0
        '''
        result = self._values.get("code_build_defaults")
        return typing.cast(typing.Optional[CodeBuildOptions], result)

    @builtins.property
    def code_pipeline(self) -> typing.Optional[_Pipeline_ea38de84]:
        '''An existing Pipeline to be reused and built upon.

        [disable-awslint:ref-via-interface]

        :default: - a new underlying pipeline is created.
        '''
        result = self._values.get("code_pipeline")
        return typing.cast(typing.Optional[_Pipeline_ea38de84], result)

    @builtins.property
    def cross_account_keys(self) -> typing.Optional[builtins.bool]:
        '''Create KMS keys for the artifact buckets, allowing cross-account deployments.

        The artifact buckets have to be encrypted to support deploying CDK apps to
        another account, so if you want to do that or want to have your artifact
        buckets encrypted, be sure to set this value to ``true``.

        Be aware there is a cost associated with maintaining the KMS keys.

        :default: false
        '''
        result = self._values.get("cross_account_keys")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cross_region_replication_buckets(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _IBucket_42e086fd]]:
        '''A map of region to S3 bucket name used for cross-region CodePipeline.

        For every Action that you specify targeting a different region than the Pipeline itself,
        if you don't provide an explicit Bucket for that region using this property,
        the construct will automatically create a Stack containing an S3 Bucket in that region.
        Passed directly through to the {@link cp.Pipeline}.

        :default: - no cross region replication buckets.
        '''
        result = self._values.get("cross_region_replication_buckets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _IBucket_42e086fd]], result)

    @builtins.property
    def docker_credentials(self) -> typing.Optional[typing.List["DockerCredential"]]:
        '''A list of credentials used to authenticate to Docker registries.

        Specify any credentials necessary within the pipeline to build, synth, update, or publish assets.

        :default: []
        '''
        result = self._values.get("docker_credentials")
        return typing.cast(typing.Optional[typing.List["DockerCredential"]], result)

    @builtins.property
    def docker_enabled_for_self_mutation(self) -> typing.Optional[builtins.bool]:
        '''Enable Docker for the self-mutate step.

        Set this to true if the pipeline itself uses Docker container assets
        (for example, if you use ``LinuxBuildImage.fromAsset()`` as the build
        image of a CodeBuild step in the pipeline).

        You do not need to set it if you build Docker image assets in the
        application Stages and Stacks that are *deployed* by this pipeline.

        Configures privileged mode for the self-mutation CodeBuild action.

        If you are about to turn this on in an already-deployed Pipeline,
        set the value to ``true`` first, commit and allow the pipeline to
        self-update, and only then use the Docker asset in the pipeline.

        :default: false
        '''
        result = self._values.get("docker_enabled_for_self_mutation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def docker_enabled_for_synth(self) -> typing.Optional[builtins.bool]:
        '''Enable Docker for the 'synth' step.

        Set this to true if you are using file assets that require
        "bundling" anywhere in your application (meaning an asset
        compilation step will be run with the tools provided by
        a Docker image), both for the Pipeline stack as well as the
        application stacks.

        A common way to use bundling assets in your application is by
        using the ``aws-cdk-lib/aws-lambda-nodejs`` library.

        Configures privileged mode for the synth CodeBuild action.

        If you are about to turn this on in an already-deployed Pipeline,
        set the value to ``true`` first, commit and allow the pipeline to
        self-update, and only then use the bundled asset.

        :default: false
        '''
        result = self._values.get("docker_enabled_for_synth")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_key_rotation(self) -> typing.Optional[builtins.bool]:
        '''Enable KMS key rotation for the generated KMS keys.

        By default KMS key rotation is disabled, but will add
        additional costs when enabled.

        :default: - false (key rotation is disabled)
        '''
        result = self._values.get("enable_key_rotation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pipeline_name(self) -> typing.Optional[builtins.str]:
        '''The name of the CodePipeline pipeline.

        :default: - Automatically generated
        '''
        result = self._values.get("pipeline_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish_assets_in_parallel(self) -> typing.Optional[builtins.bool]:
        '''Publish assets in multiple CodeBuild projects.

        If set to false, use one Project per type to publish all assets.

        Publishing in parallel improves concurrency and may reduce publishing
        latency, but may also increase overall provisioning time of the CodeBuild
        projects.

        Experiment and see what value works best for you.

        :default: true
        '''
        result = self._values.get("publish_assets_in_parallel")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reuse_cross_region_support_stacks(self) -> typing.Optional[builtins.bool]:
        '''Reuse the same cross region support stack for all pipelines in the App.

        :default: - true (Use the same support stack for all pipelines in App)
        '''
        result = self._values.get("reuse_cross_region_support_stacks")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to be assumed by this Pipeline.

        :default: - A new role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def self_mutation(self) -> typing.Optional[builtins.bool]:
        '''Whether the pipeline will update itself.

        This needs to be set to ``true`` to allow the pipeline to reconfigure
        itself when assets or stages are being added to it, and ``true`` is the
        recommended setting.

        You can temporarily set this to ``false`` while you are iterating
        on the pipeline itself and prefer to deploy changes using ``cdk deploy``.

        :default: true
        '''
        result = self._values.get("self_mutation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def self_mutation_code_build_defaults(self) -> typing.Optional[CodeBuildOptions]:
        '''Additional customizations to apply to the self mutation CodeBuild projects.

        :default: - Only ``codeBuildDefaults`` are applied
        '''
        result = self._values.get("self_mutation_code_build_defaults")
        return typing.cast(typing.Optional[CodeBuildOptions], result)

    @builtins.property
    def synth_code_build_defaults(self) -> typing.Optional[CodeBuildOptions]:
        '''Additional customizations to apply to the synthesize CodeBuild projects.

        :default: - Only ``codeBuildDefaults`` are applied
        '''
        result = self._values.get("synth_code_build_defaults")
        return typing.cast(typing.Optional[CodeBuildOptions], result)

    @builtins.property
    def use_change_sets(self) -> typing.Optional[builtins.bool]:
        '''Deploy every stack by creating a change set and executing it.

        When enabled, creates a "Prepare" and "Execute" action for each stack. Disable
        to deploy the stack in one pipeline action.

        :default: true
        '''
        result = self._values.get("use_change_sets")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.ConnectionSourceOptions",
    jsii_struct_bases=[],
    name_mapping={
        "connection_arn": "connectionArn",
        "action_name": "actionName",
        "code_build_clone_output": "codeBuildCloneOutput",
        "trigger_on_push": "triggerOnPush",
    },
)
class ConnectionSourceOptions:
    def __init__(
        self,
        *,
        connection_arn: builtins.str,
        action_name: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        trigger_on_push: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Configuration options for CodeStar source.

        :param connection_arn: The ARN of the CodeStar Connection created in the AWS console that has permissions to access this GitHub or BitBucket repository.
        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository string
        :param code_build_clone_output: If this is set, the next CodeBuild job clones the repository (instead of CodePipeline downloading the files). This provides access to repository history, and retains symlinks (symlinks would otherwise be removed by CodePipeline). **Note**: if this option is true, only CodeBuild jobs can use the output artifact. Default: false
        :param trigger_on_push: Controls automatically starting your pipeline when a new commit is made on the configured repository and branch. If unspecified, the default value is true, and the field does not display by default. Default: true

        :exampleMetadata: infused

        Example::

            pipeline = pipelines.CodePipeline(self, "Pipeline",
                synth=pipelines.ShellStep("Synth",
                    input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                        connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                    ),
                    commands=["npm ci", "npm run build", "npx cdk synth"]
                ),
            
                # Turn this on because the pipeline uses Docker image assets
                docker_enabled_for_self_mutation=True
            )
            
            pipeline.add_wave("MyWave",
                post=[
                    pipelines.CodeBuildStep("RunApproval",
                        commands=["command-from-image"],
                        build_environment=codebuild.BuildEnvironment(
                            # The user of a Docker image asset in the pipeline requires turning on
                            # 'dockerEnabledForSelfMutation'.
                            build_image=codebuild.LinuxBuildImage.from_asset(self, "Image",
                                directory="./docker-image"
                            )
                        )
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14ea58b20f21cf64b1c4567507d80ce40ed1cdc8e5831d98bd00ec1322a9ab5)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument code_build_clone_output", value=code_build_clone_output, expected_type=type_hints["code_build_clone_output"])
            check_type(argname="argument trigger_on_push", value=trigger_on_push, expected_type=type_hints["trigger_on_push"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
        }
        if action_name is not None:
            self._values["action_name"] = action_name
        if code_build_clone_output is not None:
            self._values["code_build_clone_output"] = code_build_clone_output
        if trigger_on_push is not None:
            self._values["trigger_on_push"] = trigger_on_push

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ARN of the CodeStar Connection created in the AWS console that has permissions to access this GitHub or BitBucket repository.

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-create.html

        Example::

            "arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-abcd-12ab-34cdef5678gh"
        '''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The action name used for this source in the CodePipeline.

        :default: - The repository string
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_build_clone_output(self) -> typing.Optional[builtins.bool]:
        '''If this is set, the next CodeBuild job clones the repository (instead of CodePipeline downloading the files).

        This provides access to repository history, and retains symlinks (symlinks would otherwise be
        removed by CodePipeline).

        **Note**: if this option is true, only CodeBuild jobs can use the output artifact.

        :default: false

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html#action-reference-CodestarConnectionSource-config
        '''
        result = self._values.get("code_build_clone_output")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def trigger_on_push(self) -> typing.Optional[builtins.bool]:
        '''Controls automatically starting your pipeline when a new commit is made on the configured repository and branch.

        If unspecified,
        the default value is true, and the field does not display by default.

        :default: true

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html
        '''
        result = self._values.get("trigger_on_push")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DockerCredential(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.pipelines.DockerCredential",
):
    '''Represents credentials used to access a Docker registry.

    :exampleMetadata: infused

    Example::

        docker_hub_secret = secretsmanager.Secret.from_secret_complete_arn(self, "DHSecret", "arn:aws:...")
        custom_reg_secret = secretsmanager.Secret.from_secret_complete_arn(self, "CRSecret", "arn:aws:...")
        repo1 = ecr.Repository.from_repository_arn(self, "Repo", "arn:aws:ecr:eu-west-1:0123456789012:repository/Repo1")
        repo2 = ecr.Repository.from_repository_arn(self, "Repo", "arn:aws:ecr:eu-west-1:0123456789012:repository/Repo2")
        
        pipeline = pipelines.CodePipeline(self, "Pipeline",
            docker_credentials=[
                pipelines.DockerCredential.docker_hub(docker_hub_secret),
                pipelines.DockerCredential.custom_registry("dockerregistry.example.com", custom_reg_secret),
                pipelines.DockerCredential.ecr([repo1, repo2])
            ],
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"]
            )
        )
    '''

    def __init__(
        self,
        usages: typing.Optional[typing.Sequence["DockerCredentialUsage"]] = None,
    ) -> None:
        '''
        :param usages: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4796d36763a8311889ba388377df25c49f4d460f74af5013bbfd7374dadc940)
            check_type(argname="argument usages", value=usages, expected_type=type_hints["usages"])
        jsii.create(self.__class__, self, [usages])

    @jsii.member(jsii_name="customRegistry")
    @builtins.classmethod
    def custom_registry(
        cls,
        registry_domain: builtins.str,
        secret: _ISecret_6e020e6a,
        *,
        assume_role: typing.Optional[_IRole_235f5d8e] = None,
        secret_password_field: typing.Optional[builtins.str] = None,
        secret_username_field: typing.Optional[builtins.str] = None,
        usages: typing.Optional[typing.Sequence["DockerCredentialUsage"]] = None,
    ) -> "DockerCredential":
        '''Creates a DockerCredential for a registry, based on its domain name (e.g., 'www.example.com').

        :param registry_domain: -
        :param secret: -
        :param assume_role: An IAM role to assume prior to accessing the secret. Default: - none. The current execution role will be used.
        :param secret_password_field: The name of the JSON field of the secret which contains the secret/password. Default: 'secret'
        :param secret_username_field: The name of the JSON field of the secret which contains the user/login name. Default: 'username'
        :param usages: Defines which stages of the pipeline should be granted access to these credentials. Default: - all relevant stages (synth, self-update, asset publishing) are granted access.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c646af2493265594a1cf787d9e1152d57f57cc81c6c36614a8c7b6cd36d441)
            check_type(argname="argument registry_domain", value=registry_domain, expected_type=type_hints["registry_domain"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        opts = ExternalDockerCredentialOptions(
            assume_role=assume_role,
            secret_password_field=secret_password_field,
            secret_username_field=secret_username_field,
            usages=usages,
        )

        return typing.cast("DockerCredential", jsii.sinvoke(cls, "customRegistry", [registry_domain, secret, opts]))

    @jsii.member(jsii_name="dockerHub")
    @builtins.classmethod
    def docker_hub(
        cls,
        secret: _ISecret_6e020e6a,
        *,
        assume_role: typing.Optional[_IRole_235f5d8e] = None,
        secret_password_field: typing.Optional[builtins.str] = None,
        secret_username_field: typing.Optional[builtins.str] = None,
        usages: typing.Optional[typing.Sequence["DockerCredentialUsage"]] = None,
    ) -> "DockerCredential":
        '''Creates a DockerCredential for DockerHub.

        Convenience method for ``customRegistry('https://index.docker.io/v1/', opts)``.

        :param secret: -
        :param assume_role: An IAM role to assume prior to accessing the secret. Default: - none. The current execution role will be used.
        :param secret_password_field: The name of the JSON field of the secret which contains the secret/password. Default: 'secret'
        :param secret_username_field: The name of the JSON field of the secret which contains the user/login name. Default: 'username'
        :param usages: Defines which stages of the pipeline should be granted access to these credentials. Default: - all relevant stages (synth, self-update, asset publishing) are granted access.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e01732750f5b98b4a7cb4b141a1ef2d0c5e2042c8754d0cb0f829f0a2219577)
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        opts = ExternalDockerCredentialOptions(
            assume_role=assume_role,
            secret_password_field=secret_password_field,
            secret_username_field=secret_username_field,
            usages=usages,
        )

        return typing.cast("DockerCredential", jsii.sinvoke(cls, "dockerHub", [secret, opts]))

    @jsii.member(jsii_name="ecr")
    @builtins.classmethod
    def ecr(
        cls,
        repositories: typing.Sequence[_IRepository_e6004aa6],
        *,
        assume_role: typing.Optional[_IRole_235f5d8e] = None,
        usages: typing.Optional[typing.Sequence["DockerCredentialUsage"]] = None,
    ) -> "DockerCredential":
        '''Creates a DockerCredential for one or more ECR repositories.

        NOTE - All ECR repositories in the same account and region share a domain name
        (e.g., 0123456789012.dkr.ecr.eu-west-1.amazonaws.com), and can only have one associated
        set of credentials (and DockerCredential). Attempting to associate one set of credentials
        with one ECR repo and another with another ECR repo in the same account and region will
        result in failures when using these credentials in the pipeline.

        :param repositories: -
        :param assume_role: An IAM role to assume prior to accessing the secret. Default: - none. The current execution role will be used.
        :param usages: Defines which stages of the pipeline should be granted access to these credentials. Default: - all relevant stages (synth, self-update, asset publishing) are granted access.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44075e2f8f9f423076a4b55e04677bdcd7ac2a9a1018ab4dc8116173bd7e1cf5)
            check_type(argname="argument repositories", value=repositories, expected_type=type_hints["repositories"])
        opts = EcrDockerCredentialOptions(assume_role=assume_role, usages=usages)

        return typing.cast("DockerCredential", jsii.sinvoke(cls, "ecr", [repositories, opts]))

    @jsii.member(jsii_name="grantRead")
    @abc.abstractmethod
    def grant_read(
        self,
        grantee: _IGrantable_71c4f5de,
        usage: "DockerCredentialUsage",
    ) -> None:
        '''Grant read-only access to the registry credentials.

        This grants read access to any secrets, and pull access to any repositories.

        :param grantee: -
        :param usage: -
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="usages")
    def _usages(self) -> typing.Optional[typing.List["DockerCredentialUsage"]]:
        return typing.cast(typing.Optional[typing.List["DockerCredentialUsage"]], jsii.get(self, "usages"))


class _DockerCredentialProxy(DockerCredential):
    @jsii.member(jsii_name="grantRead")
    def grant_read(
        self,
        grantee: _IGrantable_71c4f5de,
        usage: "DockerCredentialUsage",
    ) -> None:
        '''Grant read-only access to the registry credentials.

        This grants read access to any secrets, and pull access to any repositories.

        :param grantee: -
        :param usage: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__554247a15294fead54d7e6a1adaddf130cd8f655b45d31098bee6ef197e7f6b6)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument usage", value=usage, expected_type=type_hints["usage"])
        return typing.cast(None, jsii.invoke(self, "grantRead", [grantee, usage]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DockerCredential).__jsii_proxy_class__ = lambda : _DockerCredentialProxy


@jsii.enum(jsii_type="aws-cdk-lib.pipelines.DockerCredentialUsage")
class DockerCredentialUsage(enum.Enum):
    '''Defines which stages of a pipeline require the specified credentials.

    :exampleMetadata: infused

    Example::

        docker_hub_secret = secretsmanager.Secret.from_secret_complete_arn(self, "DHSecret", "arn:aws:...")
        # Only the image asset publishing actions will be granted read access to the secret.
        creds = pipelines.DockerCredential.docker_hub(docker_hub_secret, usages=[pipelines.DockerCredentialUsage.ASSET_PUBLISHING])
    '''

    SYNTH = "SYNTH"
    '''Synth/Build.'''
    SELF_UPDATE = "SELF_UPDATE"
    '''Self-update.'''
    ASSET_PUBLISHING = "ASSET_PUBLISHING"
    '''Asset publishing.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.ECRSourceOptions",
    jsii_struct_bases=[],
    name_mapping={"action_name": "actionName", "image_tag": "imageTag"},
)
class ECRSourceOptions:
    def __init__(
        self,
        *,
        action_name: typing.Optional[builtins.str] = None,
        image_tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for ECR sources.

        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository name
        :param image_tag: The image tag that will be checked for changes. Default: latest

        :exampleMetadata: infused

        Example::

            # repository: ecr.IRepository
            
            pipelines.CodePipelineSource.ecr(repository,
                image_tag="latest"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833a04c7f2e7f664e66a7534f73736d4c5911188c503aaf662baf8c6f39cf208)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action_name is not None:
            self._values["action_name"] = action_name
        if image_tag is not None:
            self._values["image_tag"] = image_tag

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The action name used for this source in the CodePipeline.

        :default: - The repository name
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_tag(self) -> typing.Optional[builtins.str]:
        '''The image tag that will be checked for changes.

        :default: latest
        '''
        result = self._values.get("image_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ECRSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.EcrDockerCredentialOptions",
    jsii_struct_bases=[],
    name_mapping={"assume_role": "assumeRole", "usages": "usages"},
)
class EcrDockerCredentialOptions:
    def __init__(
        self,
        *,
        assume_role: typing.Optional[_IRole_235f5d8e] = None,
        usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
    ) -> None:
        '''Options for defining access for a Docker Credential composed of ECR repos.

        :param assume_role: An IAM role to assume prior to accessing the secret. Default: - none. The current execution role will be used.
        :param usages: Defines which stages of the pipeline should be granted access to these credentials. Default: - all relevant stages (synth, self-update, asset publishing) are granted access.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import pipelines
            
            # role: iam.Role
            
            ecr_docker_credential_options = pipelines.EcrDockerCredentialOptions(
                assume_role=role,
                usages=[pipelines.DockerCredentialUsage.SYNTH]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b8aaeef2e17487ef54d1992c6a3a7e2349b4c4a5d93c775a043f2db02c5287)
            check_type(argname="argument assume_role", value=assume_role, expected_type=type_hints["assume_role"])
            check_type(argname="argument usages", value=usages, expected_type=type_hints["usages"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assume_role is not None:
            self._values["assume_role"] = assume_role
        if usages is not None:
            self._values["usages"] = usages

    @builtins.property
    def assume_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An IAM role to assume prior to accessing the secret.

        :default: - none. The current execution role will be used.
        '''
        result = self._values.get("assume_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def usages(self) -> typing.Optional[typing.List[DockerCredentialUsage]]:
        '''Defines which stages of the pipeline should be granted access to these credentials.

        :default: - all relevant stages (synth, self-update, asset publishing) are granted access.
        '''
        result = self._values.get("usages")
        return typing.cast(typing.Optional[typing.List[DockerCredentialUsage]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcrDockerCredentialOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.ExternalDockerCredentialOptions",
    jsii_struct_bases=[],
    name_mapping={
        "assume_role": "assumeRole",
        "secret_password_field": "secretPasswordField",
        "secret_username_field": "secretUsernameField",
        "usages": "usages",
    },
)
class ExternalDockerCredentialOptions:
    def __init__(
        self,
        *,
        assume_role: typing.Optional[_IRole_235f5d8e] = None,
        secret_password_field: typing.Optional[builtins.str] = None,
        secret_username_field: typing.Optional[builtins.str] = None,
        usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
    ) -> None:
        '''Options for defining credentials for a Docker Credential.

        :param assume_role: An IAM role to assume prior to accessing the secret. Default: - none. The current execution role will be used.
        :param secret_password_field: The name of the JSON field of the secret which contains the secret/password. Default: 'secret'
        :param secret_username_field: The name of the JSON field of the secret which contains the user/login name. Default: 'username'
        :param usages: Defines which stages of the pipeline should be granted access to these credentials. Default: - all relevant stages (synth, self-update, asset publishing) are granted access.

        :exampleMetadata: infused

        Example::

            docker_hub_secret = secretsmanager.Secret.from_secret_complete_arn(self, "DHSecret", "arn:aws:...")
            # Only the image asset publishing actions will be granted read access to the secret.
            creds = pipelines.DockerCredential.docker_hub(docker_hub_secret, usages=[pipelines.DockerCredentialUsage.ASSET_PUBLISHING])
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c359b9b78870cd0768aec95eba517b31efce3c0139487e9574671e537d4d9c8a)
            check_type(argname="argument assume_role", value=assume_role, expected_type=type_hints["assume_role"])
            check_type(argname="argument secret_password_field", value=secret_password_field, expected_type=type_hints["secret_password_field"])
            check_type(argname="argument secret_username_field", value=secret_username_field, expected_type=type_hints["secret_username_field"])
            check_type(argname="argument usages", value=usages, expected_type=type_hints["usages"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assume_role is not None:
            self._values["assume_role"] = assume_role
        if secret_password_field is not None:
            self._values["secret_password_field"] = secret_password_field
        if secret_username_field is not None:
            self._values["secret_username_field"] = secret_username_field
        if usages is not None:
            self._values["usages"] = usages

    @builtins.property
    def assume_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An IAM role to assume prior to accessing the secret.

        :default: - none. The current execution role will be used.
        '''
        result = self._values.get("assume_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def secret_password_field(self) -> typing.Optional[builtins.str]:
        '''The name of the JSON field of the secret which contains the secret/password.

        :default: 'secret'
        '''
        result = self._values.get("secret_password_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_username_field(self) -> typing.Optional[builtins.str]:
        '''The name of the JSON field of the secret which contains the user/login name.

        :default: 'username'
        '''
        result = self._values.get("secret_username_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usages(self) -> typing.Optional[typing.List[DockerCredentialUsage]]:
        '''Defines which stages of the pipeline should be granted access to these credentials.

        :default: - all relevant stages (synth, self-update, asset publishing) are granted access.
        '''
        result = self._values.get("usages")
        return typing.cast(typing.Optional[typing.List[DockerCredentialUsage]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalDockerCredentialOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.FileSetLocation",
    jsii_struct_bases=[],
    name_mapping={"directory": "directory", "file_set": "fileSet"},
)
class FileSetLocation:
    def __init__(self, *, directory: builtins.str, file_set: "FileSet") -> None:
        '''Location of a FileSet consumed or produced by a ShellStep.

        :param directory: The (relative) directory where the FileSet is found.
        :param file_set: The FileSet object.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import pipelines
            
            # file_set: pipelines.FileSet
            
            file_set_location = pipelines.FileSetLocation(
                directory="directory",
                file_set=file_set
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cf7e83b5d5ed6c40f4a63f11e08a6255275802428d4153f786e83b3477442f2)
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument file_set", value=file_set, expected_type=type_hints["file_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory": directory,
            "file_set": file_set,
        }

    @builtins.property
    def directory(self) -> builtins.str:
        '''The (relative) directory where the FileSet is found.'''
        result = self._values.get("directory")
        assert result is not None, "Required property 'directory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_set(self) -> "FileSet":
        '''The FileSet object.'''
        result = self._values.get("file_set")
        assert result is not None, "Required property 'file_set' is missing"
        return typing.cast("FileSet", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSetLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.GitHubSourceOptions",
    jsii_struct_bases=[],
    name_mapping={
        "action_name": "actionName",
        "authentication": "authentication",
        "trigger": "trigger",
    },
)
class GitHubSourceOptions:
    def __init__(
        self,
        *,
        action_name: typing.Optional[builtins.str] = None,
        authentication: typing.Optional[_SecretValue_3dd0ddae] = None,
        trigger: typing.Optional[_GitHubTrigger_0029a9bb] = None,
    ) -> None:
        '''Options for GitHub sources.

        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository string
        :param authentication: A GitHub OAuth token to use for authentication. It is recommended to use a Secrets Manager ``Secret`` to obtain the token:: const oauth = cdk.SecretValue.secretsManager('my-github-token'); The GitHub Personal Access Token should have these scopes: - **repo** - to read the repository - **admin:repo_hook** - if you plan to use webhooks (true by default) Default: - SecretValue.secretsManager('github-token')
        :param trigger: How AWS CodePipeline should be triggered. With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action. With "POLL", CodePipeline periodically checks the source for changes. With "None", the action is not triggered through changes in the source. To use ``WEBHOOK``, your GitHub Personal Access Token should have **admin:repo_hook** scope (in addition to the regular **repo** scope). Default: GitHubTrigger.WEBHOOK

        :exampleMetadata: infused

        Example::

            pipelines.CodePipelineSource.git_hub("org/repo", "branch",
                # This is optional
                authentication=cdk.SecretValue.secrets_manager("my-token")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92035a41f512b5c8f05e89aaf8eff67c15b38e88a96495de7594813674d59c85)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action_name is not None:
            self._values["action_name"] = action_name
        if authentication is not None:
            self._values["authentication"] = authentication
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The action name used for this source in the CodePipeline.

        :default: - The repository string
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''A GitHub OAuth token to use for authentication.

        It is recommended to use a Secrets Manager ``Secret`` to obtain the token::

           oauth = cdk.SecretValue.secrets_manager("my-github-token")

        The GitHub Personal Access Token should have these scopes:

        - **repo** - to read the repository
        - **admin:repo_hook** - if you plan to use webhooks (true by default)

        :default: - SecretValue.secretsManager('github-token')

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/GitHub-create-personal-token-CLI.html
        '''
        result = self._values.get("authentication")
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], result)

    @builtins.property
    def trigger(self) -> typing.Optional[_GitHubTrigger_0029a9bb]:
        '''How AWS CodePipeline should be triggered.

        With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action.
        With "POLL", CodePipeline periodically checks the source for changes.
        With "None", the action is not triggered through changes in the source.

        To use ``WEBHOOK``, your GitHub Personal Access Token should have
        **admin:repo_hook** scope (in addition to the regular **repo** scope).

        :default: GitHubTrigger.WEBHOOK
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional[_GitHubTrigger_0029a9bb], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.pipelines.ICodePipelineActionFactory")
class ICodePipelineActionFactory(typing_extensions.Protocol):
    '''Factory for explicit CodePipeline Actions.

    If you have specific types of Actions you want to add to a
    CodePipeline, write a subclass of ``Step`` that implements this
    interface, and add the action or actions you want in the ``produce`` method.

    There needs to be a level of indirection here, because some aspects of the
    Action creation need to be controlled by the workflow engine (name and
    runOrder). All the rest of the properties are controlled by the factory.
    '''

    @jsii.member(jsii_name="produceAction")
    def produce_action(
        self,
        stage: _IStage_415fc571,
        *,
        action_name: builtins.str,
        artifacts: ArtifactMap,
        pipeline: "CodePipeline",
        run_order: jsii.Number,
        scope: _constructs_77d1e7e8.Construct,
        stack_outputs_map: "StackOutputsMap",
        before_self_mutation: typing.Optional[builtins.bool] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> CodePipelineActionFactoryResult:
        '''Create the desired Action and add it to the pipeline.

        :param stage: -
        :param action_name: Name the action should get.
        :param artifacts: Helper object to translate FileSets to CodePipeline Artifacts.
        :param pipeline: The pipeline the action is being generated for.
        :param run_order: RunOrder the action should get.
        :param scope: Scope in which to create constructs.
        :param stack_outputs_map: Helper object to produce variables exported from stack deployments. If your step references outputs from a stack deployment, use this to map the output references to Codepipeline variable names. Note - Codepipeline variables can only be referenced in action configurations.
        :param before_self_mutation: Whether or not this action is inserted before self mutation. If it is, the action should take care to reflect some part of its own definition in the pipeline action definition, to trigger a restart after self-mutation (if necessary). Default: false
        :param code_build_defaults: If this action factory creates a CodeBuild step, default options to inherit. Default: - No CodeBuild project defaults
        :param fallback_artifact: An input artifact that CodeBuild projects that don't actually need an input artifact can use. CodeBuild Projects MUST have an input artifact in order to be added to the Pipeline. If the Project doesn't actually care about its input (it can be anything), it can use the Artifact passed here. Default: - A fallback artifact does not exist
        :param variables_namespace: If this step is producing outputs, the variables namespace assigned to it. Pass this on to the Action you are creating. Default: - Step doesn't produce any outputs
        '''
        ...


class _ICodePipelineActionFactoryProxy:
    '''Factory for explicit CodePipeline Actions.

    If you have specific types of Actions you want to add to a
    CodePipeline, write a subclass of ``Step`` that implements this
    interface, and add the action or actions you want in the ``produce`` method.

    There needs to be a level of indirection here, because some aspects of the
    Action creation need to be controlled by the workflow engine (name and
    runOrder). All the rest of the properties are controlled by the factory.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.pipelines.ICodePipelineActionFactory"

    @jsii.member(jsii_name="produceAction")
    def produce_action(
        self,
        stage: _IStage_415fc571,
        *,
        action_name: builtins.str,
        artifacts: ArtifactMap,
        pipeline: "CodePipeline",
        run_order: jsii.Number,
        scope: _constructs_77d1e7e8.Construct,
        stack_outputs_map: "StackOutputsMap",
        before_self_mutation: typing.Optional[builtins.bool] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> CodePipelineActionFactoryResult:
        '''Create the desired Action and add it to the pipeline.

        :param stage: -
        :param action_name: Name the action should get.
        :param artifacts: Helper object to translate FileSets to CodePipeline Artifacts.
        :param pipeline: The pipeline the action is being generated for.
        :param run_order: RunOrder the action should get.
        :param scope: Scope in which to create constructs.
        :param stack_outputs_map: Helper object to produce variables exported from stack deployments. If your step references outputs from a stack deployment, use this to map the output references to Codepipeline variable names. Note - Codepipeline variables can only be referenced in action configurations.
        :param before_self_mutation: Whether or not this action is inserted before self mutation. If it is, the action should take care to reflect some part of its own definition in the pipeline action definition, to trigger a restart after self-mutation (if necessary). Default: false
        :param code_build_defaults: If this action factory creates a CodeBuild step, default options to inherit. Default: - No CodeBuild project defaults
        :param fallback_artifact: An input artifact that CodeBuild projects that don't actually need an input artifact can use. CodeBuild Projects MUST have an input artifact in order to be added to the Pipeline. If the Project doesn't actually care about its input (it can be anything), it can use the Artifact passed here. Default: - A fallback artifact does not exist
        :param variables_namespace: If this step is producing outputs, the variables namespace assigned to it. Pass this on to the Action you are creating. Default: - Step doesn't produce any outputs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99773084b7df122e2f7df8455d5966ec674016081ec53bbdb52b9a758a61641f)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        options = ProduceActionOptions(
            action_name=action_name,
            artifacts=artifacts,
            pipeline=pipeline,
            run_order=run_order,
            scope=scope,
            stack_outputs_map=stack_outputs_map,
            before_self_mutation=before_self_mutation,
            code_build_defaults=code_build_defaults,
            fallback_artifact=fallback_artifact,
            variables_namespace=variables_namespace,
        )

        return typing.cast(CodePipelineActionFactoryResult, jsii.invoke(self, "produceAction", [stage, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodePipelineActionFactory).__jsii_proxy_class__ = lambda : _ICodePipelineActionFactoryProxy


@jsii.interface(jsii_type="aws-cdk-lib.pipelines.IFileSetProducer")
class IFileSetProducer(typing_extensions.Protocol):
    '''Any class that produces, or is itself, a ``FileSet``.

    Steps implicitly produce a primary FileSet as an output.
    '''

    @builtins.property
    @jsii.member(jsii_name="primaryOutput")
    def primary_output(self) -> typing.Optional["FileSet"]:
        '''The ``FileSet`` produced by this file set producer.

        :default: - This producer doesn't produce any file set
        '''
        ...


class _IFileSetProducerProxy:
    '''Any class that produces, or is itself, a ``FileSet``.

    Steps implicitly produce a primary FileSet as an output.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.pipelines.IFileSetProducer"

    @builtins.property
    @jsii.member(jsii_name="primaryOutput")
    def primary_output(self) -> typing.Optional["FileSet"]:
        '''The ``FileSet`` produced by this file set producer.

        :default: - This producer doesn't produce any file set
        '''
        return typing.cast(typing.Optional["FileSet"], jsii.get(self, "primaryOutput"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSetProducer).__jsii_proxy_class__ = lambda : _IFileSetProducerProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.ManualApprovalStepProps",
    jsii_struct_bases=[],
    name_mapping={"comment": "comment"},
)
class ManualApprovalStepProps:
    def __init__(self, *, comment: typing.Optional[builtins.str] = None) -> None:
        '''Construction properties for a ``ManualApprovalStep``.

        :param comment: The comment to display with this manual approval. Default: - No comment

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import pipelines
            
            manual_approval_step_props = pipelines.ManualApprovalStepProps(
                comment="comment"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0a42f985a6aa39b8db8606833d899bd8c93567a96ac5acb2c9407bde8793ed)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''The comment to display with this manual approval.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManualApprovalStepProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.PermissionsBroadeningCheckProps",
    jsii_struct_bases=[],
    name_mapping={"stage": "stage", "notification_topic": "notificationTopic"},
)
class PermissionsBroadeningCheckProps:
    def __init__(
        self,
        *,
        stage: _Stage_7df8511b,
        notification_topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''Properties for a ``PermissionsBroadeningCheck``.

        :param stage: The CDK Stage object to check the stacks of. This should be the same Stage object you are passing to ``addStage()``.
        :param notification_topic: Topic to send notifications when a human needs to give manual confirmation. Default: - no notification

        :exampleMetadata: infused

        Example::

            # pipeline: pipelines.CodePipeline
            
            stage = MyApplicationStage(self, "MyApplication")
            pipeline.add_stage(stage,
                pre=[
                    pipelines.ConfirmPermissionsBroadening("Check", stage=stage)
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a493d3747f3c71b362bc21e20cdcb176192a8ddabde715a88ac4943a53a03e8)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            check_type(argname="argument notification_topic", value=notification_topic, expected_type=type_hints["notification_topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stage": stage,
        }
        if notification_topic is not None:
            self._values["notification_topic"] = notification_topic

    @builtins.property
    def stage(self) -> _Stage_7df8511b:
        '''The CDK Stage object to check the stacks of.

        This should be the same Stage object you are passing to ``addStage()``.
        '''
        result = self._values.get("stage")
        assert result is not None, "Required property 'stage' is missing"
        return typing.cast(_Stage_7df8511b, result)

    @builtins.property
    def notification_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''Topic to send notifications when a human needs to give manual confirmation.

        :default: - no notification
        '''
        result = self._values.get("notification_topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionsBroadeningCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineBase(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.pipelines.PipelineBase",
):
    '''A generic CDK Pipelines pipeline.

    Different deployment systems will provide subclasses of ``Pipeline`` that generate
    the deployment infrastructure necessary to deploy CDK apps, specific to that system.

    This library comes with the ``CodePipeline`` class, which uses AWS CodePipeline
    to deploy CDK apps.

    The actual pipeline infrastructure is constructed (by invoking the engine)
    when ``buildPipeline()`` is called, or when ``app.synth()`` is called (whichever
    happens first).
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        synth: IFileSetProducer,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param synth: The build step that produces the CDK Cloud Assembly. The primary output of this step needs to be the ``cdk.out`` directory generated by the ``cdk synth`` command. If you use a ``ShellStep`` here and you don't configure an output directory, the output directory will automatically be assumed to be ``cdk.out``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d184a64a4ab9776e0cde448a4015acadcea743c3fc3b48f622df0afb4024c6e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PipelineBaseProps(synth=synth)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isPipeline")
    @builtins.classmethod
    def is_pipeline(cls, x: typing.Any) -> builtins.bool:
        '''Return whether the given object extends ``PipelineBase``.

        We do attribute detection since we can't reliably use 'instanceof'.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f67cf9a317d65ff87cbc38b2a72ad26c2ee3899fb8a0b5068ccdc87b2c46b2da)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isPipeline", [x]))

    @jsii.member(jsii_name="addStage")
    def add_stage(
        self,
        stage: _Stage_7df8511b,
        *,
        post: typing.Optional[typing.Sequence["Step"]] = None,
        pre: typing.Optional[typing.Sequence["Step"]] = None,
        stack_steps: typing.Optional[typing.Sequence[typing.Union["StackSteps", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> "StageDeployment":
        '''Deploy a single Stage by itself.

        Add a Stage to the pipeline, to be deployed in sequence with other
        Stages added to the pipeline. All Stacks in the stage will be deployed
        in an order automatically determined by their relative dependencies.

        :param stage: -
        :param post: Additional steps to run after all of the stacks in the stage. Default: - No additional steps
        :param pre: Additional steps to run before any of the stacks in the stage. Default: - No additional steps
        :param stack_steps: Instructions for stack level steps. Default: - No additional instructions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cfb2052bce20c2fa202ea358095de4d8c0da42de12b0481096f461291c33ee4)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        options = AddStageOpts(post=post, pre=pre, stack_steps=stack_steps)

        return typing.cast("StageDeployment", jsii.invoke(self, "addStage", [stage, options]))

    @jsii.member(jsii_name="addWave")
    def add_wave(
        self,
        id: builtins.str,
        *,
        post: typing.Optional[typing.Sequence["Step"]] = None,
        pre: typing.Optional[typing.Sequence["Step"]] = None,
    ) -> "Wave":
        '''Add a Wave to the pipeline, for deploying multiple Stages in parallel.

        Use the return object of this method to deploy multiple stages in parallel.

        Example::

           # pipeline: pipelines.CodePipeline


           wave = pipeline.add_wave("MyWave")
           wave.add_stage(MyApplicationStage(self, "Stage1"))
           wave.add_stage(MyApplicationStage(self, "Stage2"))

        :param id: -
        :param post: Additional steps to run after all of the stages in the wave. Default: - No additional steps
        :param pre: Additional steps to run before any of the stages in the wave. Default: - No additional steps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad54c6253f19ba3a870e05ab1a3c0f4069394612e1bb5e45764182211f8ce8f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = WaveOptions(post=post, pre=pre)

        return typing.cast("Wave", jsii.invoke(self, "addWave", [id, options]))

    @jsii.member(jsii_name="buildPipeline")
    def build_pipeline(self) -> None:
        '''Send the current pipeline definition to the engine, and construct the pipeline.

        It is not possible to modify the pipeline after calling this method.
        '''
        return typing.cast(None, jsii.invoke(self, "buildPipeline", []))

    @jsii.member(jsii_name="doBuildPipeline")
    @abc.abstractmethod
    def _do_build_pipeline(self) -> None:
        '''Implemented by subclasses to do the actual pipeline construction.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="cloudAssemblyFileSet")
    def cloud_assembly_file_set(self) -> "FileSet":
        '''The FileSet tha contains the cloud assembly.

        This is the primary output of the synth step.
        '''
        return typing.cast("FileSet", jsii.get(self, "cloudAssemblyFileSet"))

    @builtins.property
    @jsii.member(jsii_name="synth")
    def synth(self) -> IFileSetProducer:
        '''The build step that produces the CDK Cloud Assembly.'''
        return typing.cast(IFileSetProducer, jsii.get(self, "synth"))

    @builtins.property
    @jsii.member(jsii_name="waves")
    def waves(self) -> typing.List["Wave"]:
        '''The waves in this pipeline.'''
        return typing.cast(typing.List["Wave"], jsii.get(self, "waves"))


class _PipelineBaseProxy(PipelineBase):
    @jsii.member(jsii_name="doBuildPipeline")
    def _do_build_pipeline(self) -> None:
        '''Implemented by subclasses to do the actual pipeline construction.'''
        return typing.cast(None, jsii.invoke(self, "doBuildPipeline", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, PipelineBase).__jsii_proxy_class__ = lambda : _PipelineBaseProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.PipelineBaseProps",
    jsii_struct_bases=[],
    name_mapping={"synth": "synth"},
)
class PipelineBaseProps:
    def __init__(self, *, synth: IFileSetProducer) -> None:
        '''Properties for a ``Pipeline``.

        :param synth: The build step that produces the CDK Cloud Assembly. The primary output of this step needs to be the ``cdk.out`` directory generated by the ``cdk synth`` command. If you use a ``ShellStep`` here and you don't configure an output directory, the output directory will automatically be assumed to be ``cdk.out``.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import pipelines
            
            # file_set_producer: pipelines.IFileSetProducer
            
            pipeline_base_props = pipelines.PipelineBaseProps(
                synth=file_set_producer
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79842ef214ef2802f8ca77d0d6f69188566d39e1953e2067e21825205ad4e2d0)
            check_type(argname="argument synth", value=synth, expected_type=type_hints["synth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "synth": synth,
        }

    @builtins.property
    def synth(self) -> IFileSetProducer:
        '''The build step that produces the CDK Cloud Assembly.

        The primary output of this step needs to be the ``cdk.out`` directory
        generated by the ``cdk synth`` command.

        If you use a ``ShellStep`` here and you don't configure an output directory,
        the output directory will automatically be assumed to be ``cdk.out``.
        '''
        result = self._values.get("synth")
        assert result is not None, "Required property 'synth' is missing"
        return typing.cast(IFileSetProducer, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.ProduceActionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "action_name": "actionName",
        "artifacts": "artifacts",
        "pipeline": "pipeline",
        "run_order": "runOrder",
        "scope": "scope",
        "stack_outputs_map": "stackOutputsMap",
        "before_self_mutation": "beforeSelfMutation",
        "code_build_defaults": "codeBuildDefaults",
        "fallback_artifact": "fallbackArtifact",
        "variables_namespace": "variablesNamespace",
    },
)
class ProduceActionOptions:
    def __init__(
        self,
        *,
        action_name: builtins.str,
        artifacts: ArtifactMap,
        pipeline: "CodePipeline",
        run_order: jsii.Number,
        scope: _constructs_77d1e7e8.Construct,
        stack_outputs_map: "StackOutputsMap",
        before_self_mutation: typing.Optional[builtins.bool] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for the ``CodePipelineActionFactory.produce()`` method.

        :param action_name: Name the action should get.
        :param artifacts: Helper object to translate FileSets to CodePipeline Artifacts.
        :param pipeline: The pipeline the action is being generated for.
        :param run_order: RunOrder the action should get.
        :param scope: Scope in which to create constructs.
        :param stack_outputs_map: Helper object to produce variables exported from stack deployments. If your step references outputs from a stack deployment, use this to map the output references to Codepipeline variable names. Note - Codepipeline variables can only be referenced in action configurations.
        :param before_self_mutation: Whether or not this action is inserted before self mutation. If it is, the action should take care to reflect some part of its own definition in the pipeline action definition, to trigger a restart after self-mutation (if necessary). Default: false
        :param code_build_defaults: If this action factory creates a CodeBuild step, default options to inherit. Default: - No CodeBuild project defaults
        :param fallback_artifact: An input artifact that CodeBuild projects that don't actually need an input artifact can use. CodeBuild Projects MUST have an input artifact in order to be added to the Pipeline. If the Project doesn't actually care about its input (it can be anything), it can use the Artifact passed here. Default: - A fallback artifact does not exist
        :param variables_namespace: If this step is producing outputs, the variables namespace assigned to it. Pass this on to the Action you are creating. Default: - Step doesn't produce any outputs

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_codebuild as codebuild
            from aws_cdk import aws_codepipeline as codepipeline
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            from aws_cdk import aws_s3 as s3
            from aws_cdk import pipelines
            import constructs as constructs
            
            # artifact: codepipeline.Artifact
            # artifact_map: pipelines.ArtifactMap
            # bucket: s3.Bucket
            # build_image: codebuild.IBuildImage
            # build_spec: codebuild.BuildSpec
            # cache: codebuild.Cache
            # code_pipeline: pipelines.CodePipeline
            # construct: constructs.Construct
            # file_system_location: codebuild.IFileSystemLocation
            # log_group: logs.LogGroup
            # policy_statement: iam.PolicyStatement
            # security_group: ec2.SecurityGroup
            # stack_outputs_map: pipelines.StackOutputsMap
            # subnet: ec2.Subnet
            # subnet_filter: ec2.SubnetFilter
            # value: Any
            # vpc: ec2.Vpc
            
            produce_action_options = pipelines.ProduceActionOptions(
                action_name="actionName",
                artifacts=artifact_map,
                pipeline=code_pipeline,
                run_order=123,
                scope=construct,
                stack_outputs_map=stack_outputs_map,
            
                # the properties below are optional
                before_self_mutation=False,
                code_build_defaults=pipelines.CodeBuildOptions(
                    build_environment=codebuild.BuildEnvironment(
                        build_image=build_image,
                        certificate=codebuild.BuildEnvironmentCertificate(
                            bucket=bucket,
                            object_key="objectKey"
                        ),
                        compute_type=codebuild.ComputeType.SMALL,
                        environment_variables={
                            "environment_variables_key": codebuild.BuildEnvironmentVariable(
                                value=value,
            
                                # the properties below are optional
                                type=codebuild.BuildEnvironmentVariableType.PLAINTEXT
                            )
                        },
                        privileged=False
                    ),
                    cache=cache,
                    file_system_locations=[file_system_location],
                    logging=codebuild.LoggingOptions(
                        cloud_watch=codebuild.CloudWatchLoggingOptions(
                            enabled=False,
                            log_group=log_group,
                            prefix="prefix"
                        ),
                        s3=codebuild.S3LoggingOptions(
                            bucket=bucket,
            
                            # the properties below are optional
                            enabled=False,
                            encrypted=False,
                            prefix="prefix"
                        )
                    ),
                    partial_build_spec=build_spec,
                    role_policy=[policy_statement],
                    security_groups=[security_group],
                    subnet_selection=ec2.SubnetSelection(
                        availability_zones=["availabilityZones"],
                        one_per_az=False,
                        subnet_filters=[subnet_filter],
                        subnet_group_name="subnetGroupName",
                        subnets=[subnet],
                        subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                    ),
                    timeout=cdk.Duration.minutes(30),
                    vpc=vpc
                ),
                fallback_artifact=artifact,
                variables_namespace="variablesNamespace"
            )
        '''
        if isinstance(code_build_defaults, dict):
            code_build_defaults = CodeBuildOptions(**code_build_defaults)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93aef9a478cf51d0a19344db9575ea0a8f1c4048021aae6ecbd679f0230708cb)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument stack_outputs_map", value=stack_outputs_map, expected_type=type_hints["stack_outputs_map"])
            check_type(argname="argument before_self_mutation", value=before_self_mutation, expected_type=type_hints["before_self_mutation"])
            check_type(argname="argument code_build_defaults", value=code_build_defaults, expected_type=type_hints["code_build_defaults"])
            check_type(argname="argument fallback_artifact", value=fallback_artifact, expected_type=type_hints["fallback_artifact"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "artifacts": artifacts,
            "pipeline": pipeline,
            "run_order": run_order,
            "scope": scope,
            "stack_outputs_map": stack_outputs_map,
        }
        if before_self_mutation is not None:
            self._values["before_self_mutation"] = before_self_mutation
        if code_build_defaults is not None:
            self._values["code_build_defaults"] = code_build_defaults
        if fallback_artifact is not None:
            self._values["fallback_artifact"] = fallback_artifact
        if variables_namespace is not None:
            self._values["variables_namespace"] = variables_namespace

    @builtins.property
    def action_name(self) -> builtins.str:
        '''Name the action should get.'''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def artifacts(self) -> ArtifactMap:
        '''Helper object to translate FileSets to CodePipeline Artifacts.'''
        result = self._values.get("artifacts")
        assert result is not None, "Required property 'artifacts' is missing"
        return typing.cast(ArtifactMap, result)

    @builtins.property
    def pipeline(self) -> "CodePipeline":
        '''The pipeline the action is being generated for.'''
        result = self._values.get("pipeline")
        assert result is not None, "Required property 'pipeline' is missing"
        return typing.cast("CodePipeline", result)

    @builtins.property
    def run_order(self) -> jsii.Number:
        '''RunOrder the action should get.'''
        result = self._values.get("run_order")
        assert result is not None, "Required property 'run_order' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scope(self) -> _constructs_77d1e7e8.Construct:
        '''Scope in which to create constructs.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(_constructs_77d1e7e8.Construct, result)

    @builtins.property
    def stack_outputs_map(self) -> "StackOutputsMap":
        '''Helper object to produce variables exported from stack deployments.

        If your step references outputs from a stack deployment, use
        this to map the output references to Codepipeline variable names.

        Note - Codepipeline variables can only be referenced in action
        configurations.
        '''
        result = self._values.get("stack_outputs_map")
        assert result is not None, "Required property 'stack_outputs_map' is missing"
        return typing.cast("StackOutputsMap", result)

    @builtins.property
    def before_self_mutation(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this action is inserted before self mutation.

        If it is, the action should take care to reflect some part of
        its own definition in the pipeline action definition, to
        trigger a restart after self-mutation (if necessary).

        :default: false
        '''
        result = self._values.get("before_self_mutation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def code_build_defaults(self) -> typing.Optional[CodeBuildOptions]:
        '''If this action factory creates a CodeBuild step, default options to inherit.

        :default: - No CodeBuild project defaults
        '''
        result = self._values.get("code_build_defaults")
        return typing.cast(typing.Optional[CodeBuildOptions], result)

    @builtins.property
    def fallback_artifact(self) -> typing.Optional[_Artifact_0cb05964]:
        '''An input artifact that CodeBuild projects that don't actually need an input artifact can use.

        CodeBuild Projects MUST have an input artifact in order to be added to the Pipeline. If
        the Project doesn't actually care about its input (it can be anything), it can use the
        Artifact passed here.

        :default: - A fallback artifact does not exist
        '''
        result = self._values.get("fallback_artifact")
        return typing.cast(typing.Optional[_Artifact_0cb05964], result)

    @builtins.property
    def variables_namespace(self) -> typing.Optional[builtins.str]:
        '''If this step is producing outputs, the variables namespace assigned to it.

        Pass this on to the Action you are creating.

        :default: - Step doesn't produce any outputs
        '''
        result = self._values.get("variables_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProduceActionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.S3SourceOptions",
    jsii_struct_bases=[],
    name_mapping={"action_name": "actionName", "role": "role", "trigger": "trigger"},
)
class S3SourceOptions:
    def __init__(
        self,
        *,
        action_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        trigger: typing.Optional[_S3Trigger_3ab49ad8] = None,
    ) -> None:
        '''Options for S3 sources.

        :param action_name: The action name used for this source in the CodePipeline. Default: - The bucket name
        :param role: The role that will be assumed by the pipeline prior to executing the ``S3Source`` action. Default: - a new role will be generated
        :param trigger: How should CodePipeline detect source changes for this Action. Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail, as otherwise the CloudWatch Events will not be emitted. Default: S3Trigger.POLL

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codepipeline_actions as codepipeline_actions
            from aws_cdk import aws_iam as iam
            from aws_cdk import pipelines
            
            # role: iam.Role
            
            s3_source_options = pipelines.S3SourceOptions(
                action_name="actionName",
                role=role,
                trigger=codepipeline_actions.S3Trigger.NONE
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cae2e2afdaad184f628a943e938bcc586f2ec9060bde2ab497f96efaf7c265a7)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action_name is not None:
            self._values["action_name"] = action_name
        if role is not None:
            self._values["role"] = role
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The action name used for this source in the CodePipeline.

        :default: - The bucket name
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role that will be assumed by the pipeline prior to executing the ``S3Source`` action.

        :default: - a new role will be generated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def trigger(self) -> typing.Optional[_S3Trigger_3ab49ad8]:
        '''How should CodePipeline detect source changes for this Action.

        Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail,
        as otherwise the CloudWatch Events will not be emitted.

        :default: S3Trigger.POLL

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/log-s3-data-events.html
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional[_S3Trigger_3ab49ad8], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3SourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.ShellStepProps",
    jsii_struct_bases=[],
    name_mapping={
        "commands": "commands",
        "additional_inputs": "additionalInputs",
        "env": "env",
        "env_from_cfn_outputs": "envFromCfnOutputs",
        "input": "input",
        "install_commands": "installCommands",
        "primary_output_directory": "primaryOutputDirectory",
    },
)
class ShellStepProps:
    def __init__(
        self,
        *,
        commands: typing.Sequence[builtins.str],
        additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
        input: typing.Optional[IFileSetProducer] = None,
        install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary_output_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a ``ShellStep``.

        :param commands: Commands to run.
        :param additional_inputs: Additional FileSets to put in other directories. Specifies a mapping from directory name to FileSets. During the script execution, the FileSets will be available in the directories indicated. The directory names may be relative. For example, you can put the main input and an additional input side-by-side with the following configuration:: const script = new pipelines.ShellStep('MainScript', { commands: ['npm ci','npm run build','npx cdk synth'], input: pipelines.CodePipelineSource.gitHub('org/source1', 'main'), additionalInputs: { '../siblingdir': pipelines.CodePipelineSource.gitHub('org/source2', 'main'), } }); Default: - No additional inputs
        :param env: Environment variables to set. Default: - No environment variables
        :param env_from_cfn_outputs: Set environment variables based on Stack Outputs. ``ShellStep``s following stack or stage deployments may access the ``CfnOutput``s of those stacks to get access to --for example--automatically generated resource names or endpoint URLs. Default: - No environment variables created from stack outputs
        :param input: FileSet to run these scripts on. The files in the FileSet will be placed in the working directory when the script is executed. Use ``additionalInputs`` to download file sets to other directories as well. Default: - No input specified
        :param install_commands: Installation commands to run before the regular commands. For deployment engines that support it, install commands will be classified differently in the job history from the regular ``commands``. Default: - No installation commands
        :param primary_output_directory: The directory that will contain the primary output fileset. After running the script, the contents of the given directory will be treated as the primary output of this Step. Default: - No primary output

        :exampleMetadata: infused

        Example::

            # Modern API
            modern_pipeline = pipelines.CodePipeline(self, "Pipeline",
                self_mutation=False,
                synth=pipelines.ShellStep("Synth",
                    input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                        connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                    ),
                    commands=["npm ci", "npm run build", "npx cdk synth"
                    ]
                )
            )
            
            # Original API
            cloud_assembly_artifact = codepipeline.Artifact()
            original_pipeline = pipelines.CdkPipeline(self, "Pipeline",
                self_mutating=False,
                cloud_assembly_artifact=cloud_assembly_artifact
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__672600085b4c1f54d7e497f605a0be2945f1a2759aaf8632197707da6d73a55c)
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument additional_inputs", value=additional_inputs, expected_type=type_hints["additional_inputs"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument env_from_cfn_outputs", value=env_from_cfn_outputs, expected_type=type_hints["env_from_cfn_outputs"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument install_commands", value=install_commands, expected_type=type_hints["install_commands"])
            check_type(argname="argument primary_output_directory", value=primary_output_directory, expected_type=type_hints["primary_output_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "commands": commands,
        }
        if additional_inputs is not None:
            self._values["additional_inputs"] = additional_inputs
        if env is not None:
            self._values["env"] = env
        if env_from_cfn_outputs is not None:
            self._values["env_from_cfn_outputs"] = env_from_cfn_outputs
        if input is not None:
            self._values["input"] = input
        if install_commands is not None:
            self._values["install_commands"] = install_commands
        if primary_output_directory is not None:
            self._values["primary_output_directory"] = primary_output_directory

    @builtins.property
    def commands(self) -> typing.List[builtins.str]:
        '''Commands to run.'''
        result = self._values.get("commands")
        assert result is not None, "Required property 'commands' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def additional_inputs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]]:
        '''Additional FileSets to put in other directories.

        Specifies a mapping from directory name to FileSets. During the
        script execution, the FileSets will be available in the directories
        indicated.

        The directory names may be relative. For example, you can put
        the main input and an additional input side-by-side with the
        following configuration::

           script = pipelines.ShellStep("MainScript",
               commands=["npm ci", "npm run build", "npx cdk synth"],
               input=pipelines.CodePipelineSource.git_hub("org/source1", "main"),
               additional_inputs={
                   "../siblingdir": pipelines.CodePipelineSource.git_hub("org/source2", "main")
               }
           )

        :default: - No additional inputs
        '''
        result = self._values.get("additional_inputs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Environment variables to set.

        :default: - No environment variables
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def env_from_cfn_outputs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]]:
        '''Set environment variables based on Stack Outputs.

        ``ShellStep``s following stack or stage deployments may
        access the ``CfnOutput``s of those stacks to get access to
        --for example--automatically generated resource names or
        endpoint URLs.

        :default: - No environment variables created from stack outputs
        '''
        result = self._values.get("env_from_cfn_outputs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]], result)

    @builtins.property
    def input(self) -> typing.Optional[IFileSetProducer]:
        '''FileSet to run these scripts on.

        The files in the FileSet will be placed in the working directory when
        the script is executed. Use ``additionalInputs`` to download file sets
        to other directories as well.

        :default: - No input specified
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[IFileSetProducer], result)

    @builtins.property
    def install_commands(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Installation commands to run before the regular commands.

        For deployment engines that support it, install commands will be classified
        differently in the job history from the regular ``commands``.

        :default: - No installation commands
        '''
        result = self._values.get("install_commands")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def primary_output_directory(self) -> typing.Optional[builtins.str]:
        '''The directory that will contain the primary output fileset.

        After running the script, the contents of the given directory
        will be treated as the primary output of this Step.

        :default: - No primary output
        '''
        result = self._values.get("primary_output_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ShellStepProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.StackAsset",
    jsii_struct_bases=[],
    name_mapping={
        "asset_id": "assetId",
        "asset_manifest_path": "assetManifestPath",
        "asset_selector": "assetSelector",
        "asset_type": "assetType",
        "is_template": "isTemplate",
        "asset_publishing_role_arn": "assetPublishingRoleArn",
    },
)
class StackAsset:
    def __init__(
        self,
        *,
        asset_id: builtins.str,
        asset_manifest_path: builtins.str,
        asset_selector: builtins.str,
        asset_type: AssetType,
        is_template: builtins.bool,
        asset_publishing_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''An asset used by a Stack.

        :param asset_id: Asset identifier.
        :param asset_manifest_path: Absolute asset manifest path. This needs to be made relative at a later point in time, but when this information is parsed we don't know about the root cloud assembly yet.
        :param asset_selector: Asset selector to pass to ``cdk-assets``.
        :param asset_type: Type of asset to publish.
        :param is_template: Does this asset represent the CloudFormation template for the stack. Default: false
        :param asset_publishing_role_arn: Role ARN to assume to publish. Default: - No need to assume any role

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import pipelines
            
            stack_asset = pipelines.StackAsset(
                asset_id="assetId",
                asset_manifest_path="assetManifestPath",
                asset_selector="assetSelector",
                asset_type=pipelines.AssetType.FILE,
                is_template=False,
            
                # the properties below are optional
                asset_publishing_role_arn="assetPublishingRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b53846c07332af34759787d6881e8bb143a9ccedff4818aa7909126839e2a09)
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
            check_type(argname="argument asset_manifest_path", value=asset_manifest_path, expected_type=type_hints["asset_manifest_path"])
            check_type(argname="argument asset_selector", value=asset_selector, expected_type=type_hints["asset_selector"])
            check_type(argname="argument asset_type", value=asset_type, expected_type=type_hints["asset_type"])
            check_type(argname="argument is_template", value=is_template, expected_type=type_hints["is_template"])
            check_type(argname="argument asset_publishing_role_arn", value=asset_publishing_role_arn, expected_type=type_hints["asset_publishing_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_id": asset_id,
            "asset_manifest_path": asset_manifest_path,
            "asset_selector": asset_selector,
            "asset_type": asset_type,
            "is_template": is_template,
        }
        if asset_publishing_role_arn is not None:
            self._values["asset_publishing_role_arn"] = asset_publishing_role_arn

    @builtins.property
    def asset_id(self) -> builtins.str:
        '''Asset identifier.'''
        result = self._values.get("asset_id")
        assert result is not None, "Required property 'asset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_manifest_path(self) -> builtins.str:
        '''Absolute asset manifest path.

        This needs to be made relative at a later point in time, but when this
        information is parsed we don't know about the root cloud assembly yet.
        '''
        result = self._values.get("asset_manifest_path")
        assert result is not None, "Required property 'asset_manifest_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_selector(self) -> builtins.str:
        '''Asset selector to pass to ``cdk-assets``.'''
        result = self._values.get("asset_selector")
        assert result is not None, "Required property 'asset_selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_type(self) -> AssetType:
        '''Type of asset to publish.'''
        result = self._values.get("asset_type")
        assert result is not None, "Required property 'asset_type' is missing"
        return typing.cast(AssetType, result)

    @builtins.property
    def is_template(self) -> builtins.bool:
        '''Does this asset represent the CloudFormation template for the stack.

        :default: false
        '''
        result = self._values.get("is_template")
        assert result is not None, "Required property 'is_template' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def asset_publishing_role_arn(self) -> typing.Optional[builtins.str]:
        '''Role ARN to assume to publish.

        :default: - No need to assume any role
        '''
        result = self._values.get("asset_publishing_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackAsset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StackDeployment(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.StackDeployment",
):
    '''Deployment of a single Stack.

    You don't need to instantiate this class -- it will
    be automatically instantiated as necessary when you
    add a ``Stage`` to a pipeline.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import cx_api
        from aws_cdk import pipelines
        
        # cloud_formation_stack_artifact: cx_api.CloudFormationStackArtifact
        
        stack_deployment = pipelines.StackDeployment.from_artifact(cloud_formation_stack_artifact)
    '''

    @jsii.member(jsii_name="fromArtifact")
    @builtins.classmethod
    def from_artifact(
        cls,
        stack_artifact: _CloudFormationStackArtifact_97533dc8,
    ) -> "StackDeployment":
        '''Build a ``StackDeployment`` from a Stack Artifact in a Cloud Assembly.

        :param stack_artifact: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e4b846e8d3dadc7378b689c2dab6fb92e7f2100aef448009c9ec434fe88e2e)
            check_type(argname="argument stack_artifact", value=stack_artifact, expected_type=type_hints["stack_artifact"])
        return typing.cast("StackDeployment", jsii.sinvoke(cls, "fromArtifact", [stack_artifact]))

    @jsii.member(jsii_name="addStackDependency")
    def add_stack_dependency(self, stack_deployment: "StackDeployment") -> None:
        '''Add a dependency on another stack.

        :param stack_deployment: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8ba0ab32a6826cbb7060a998d3ac3da2d06cd442d144b5ecf691e35278bb3a0)
            check_type(argname="argument stack_deployment", value=stack_deployment, expected_type=type_hints["stack_deployment"])
        return typing.cast(None, jsii.invoke(self, "addStackDependency", [stack_deployment]))

    @jsii.member(jsii_name="addStackSteps")
    def add_stack_steps(
        self,
        pre: typing.Sequence["Step"],
        change_set: typing.Sequence["Step"],
        post: typing.Sequence["Step"],
    ) -> None:
        '''Adds steps to each phase of the stack.

        :param pre: steps executed before stack.prepare.
        :param change_set: steps executed after stack.prepare and before stack.deploy.
        :param post: steps executed after stack.deploy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee2fbbf15668f466092e120cac329bba8450a234aeb44ff69f7e6d6118482210)
            check_type(argname="argument pre", value=pre, expected_type=type_hints["pre"])
            check_type(argname="argument change_set", value=change_set, expected_type=type_hints["change_set"])
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
        return typing.cast(None, jsii.invoke(self, "addStackSteps", [pre, change_set, post]))

    @builtins.property
    @jsii.member(jsii_name="absoluteTemplatePath")
    def absolute_template_path(self) -> builtins.str:
        '''Template path on disk to CloudAssembly.'''
        return typing.cast(builtins.str, jsii.get(self, "absoluteTemplatePath"))

    @builtins.property
    @jsii.member(jsii_name="assets")
    def assets(self) -> typing.List[StackAsset]:
        '''Assets referenced by this stack.'''
        return typing.cast(typing.List[StackAsset], jsii.get(self, "assets"))

    @builtins.property
    @jsii.member(jsii_name="changeSet")
    def change_set(self) -> typing.List["Step"]:
        '''Steps that take place after stack is prepared but before stack deploys.

        Your pipeline engine may not disable ``prepareStep``.
        '''
        return typing.cast(typing.List["Step"], jsii.get(self, "changeSet"))

    @builtins.property
    @jsii.member(jsii_name="constructPath")
    def construct_path(self) -> builtins.str:
        '''Construct path for this stack.'''
        return typing.cast(builtins.str, jsii.get(self, "constructPath"))

    @builtins.property
    @jsii.member(jsii_name="post")
    def post(self) -> typing.List["Step"]:
        '''Steps to execute after stack deploys.'''
        return typing.cast(typing.List["Step"], jsii.get(self, "post"))

    @builtins.property
    @jsii.member(jsii_name="pre")
    def pre(self) -> typing.List["Step"]:
        '''Steps that take place before stack is prepared.

        If your pipeline engine disables 'prepareStep', then this will happen before stack deploys
        '''
        return typing.cast(typing.List["Step"], jsii.get(self, "pre"))

    @builtins.property
    @jsii.member(jsii_name="stackArtifactId")
    def stack_artifact_id(self) -> builtins.str:
        '''Artifact ID for this stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackArtifactId"))

    @builtins.property
    @jsii.member(jsii_name="stackDependencies")
    def stack_dependencies(self) -> typing.List["StackDeployment"]:
        '''Other stacks this stack depends on.'''
        return typing.cast(typing.List["StackDeployment"], jsii.get(self, "stackDependencies"))

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''Name for this stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Tags to apply to the stack.'''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        '''Account where the stack should be deployed.

        :default: - Pipeline account
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleArn")
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''Role to assume before deploying this stack.

        :default: - Don't assume any role
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assumeRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''Execution role to pass to CloudFormation.

        :default: - No execution role
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the stack should be deployed.

        :default: - Pipeline region
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="templateAsset")
    def template_asset(self) -> typing.Optional[StackAsset]:
        '''The asset that represents the CloudFormation template for this stack.'''
        return typing.cast(typing.Optional[StackAsset], jsii.get(self, "templateAsset"))

    @builtins.property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> typing.Optional[builtins.str]:
        '''The S3 URL which points to the template asset location in the publishing bucket.

        This is ``undefined`` if the stack template is not published. Use the
        ``DefaultStackSynthesizer`` to ensure it is.

        Example value: ``https://bucket.s3.amazonaws.com/object/key``
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrl"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.StackDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "absolute_template_path": "absoluteTemplatePath",
        "construct_path": "constructPath",
        "stack_artifact_id": "stackArtifactId",
        "stack_name": "stackName",
        "account": "account",
        "assets": "assets",
        "assume_role_arn": "assumeRoleArn",
        "execution_role_arn": "executionRoleArn",
        "region": "region",
        "tags": "tags",
        "template_s3_uri": "templateS3Uri",
    },
)
class StackDeploymentProps:
    def __init__(
        self,
        *,
        absolute_template_path: builtins.str,
        construct_path: builtins.str,
        stack_artifact_id: builtins.str,
        stack_name: builtins.str,
        account: typing.Optional[builtins.str] = None,
        assets: typing.Optional[typing.Sequence[typing.Union[StackAsset, typing.Dict[builtins.str, typing.Any]]]] = None,
        assume_role_arn: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a ``StackDeployment``.

        :param absolute_template_path: Template path on disk to cloud assembly (cdk.out).
        :param construct_path: Construct path for this stack.
        :param stack_artifact_id: Artifact ID for this stack.
        :param stack_name: Name for this stack.
        :param account: Account where the stack should be deployed. Default: - Pipeline account
        :param assets: Assets referenced by this stack. Default: - No assets
        :param assume_role_arn: Role to assume before deploying this stack. Default: - Don't assume any role
        :param execution_role_arn: Execution role to pass to CloudFormation. Default: - No execution role
        :param region: Region where the stack should be deployed. Default: - Pipeline region
        :param tags: Tags to apply to the stack. Default: - No tags
        :param template_s3_uri: The S3 URL which points to the template asset location in the publishing bucket. Default: - Stack template is not published

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import pipelines
            
            stack_deployment_props = pipelines.StackDeploymentProps(
                absolute_template_path="absoluteTemplatePath",
                construct_path="constructPath",
                stack_artifact_id="stackArtifactId",
                stack_name="stackName",
            
                # the properties below are optional
                account="account",
                assets=[pipelines.StackAsset(
                    asset_id="assetId",
                    asset_manifest_path="assetManifestPath",
                    asset_selector="assetSelector",
                    asset_type=pipelines.AssetType.FILE,
                    is_template=False,
            
                    # the properties below are optional
                    asset_publishing_role_arn="assetPublishingRoleArn"
                )],
                assume_role_arn="assumeRoleArn",
                execution_role_arn="executionRoleArn",
                region="region",
                tags={
                    "tags_key": "tags"
                },
                template_s3_uri="templateS3Uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee959d9efa16dfdb6813c606cf8d87ccf20db0aa7716242deca0a8be262c6f75)
            check_type(argname="argument absolute_template_path", value=absolute_template_path, expected_type=type_hints["absolute_template_path"])
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument stack_artifact_id", value=stack_artifact_id, expected_type=type_hints["stack_artifact_id"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument assets", value=assets, expected_type=type_hints["assets"])
            check_type(argname="argument assume_role_arn", value=assume_role_arn, expected_type=type_hints["assume_role_arn"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_s3_uri", value=template_s3_uri, expected_type=type_hints["template_s3_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "absolute_template_path": absolute_template_path,
            "construct_path": construct_path,
            "stack_artifact_id": stack_artifact_id,
            "stack_name": stack_name,
        }
        if account is not None:
            self._values["account"] = account
        if assets is not None:
            self._values["assets"] = assets
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if region is not None:
            self._values["region"] = region
        if tags is not None:
            self._values["tags"] = tags
        if template_s3_uri is not None:
            self._values["template_s3_uri"] = template_s3_uri

    @builtins.property
    def absolute_template_path(self) -> builtins.str:
        '''Template path on disk to cloud assembly (cdk.out).'''
        result = self._values.get("absolute_template_path")
        assert result is not None, "Required property 'absolute_template_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def construct_path(self) -> builtins.str:
        '''Construct path for this stack.'''
        result = self._values.get("construct_path")
        assert result is not None, "Required property 'construct_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_artifact_id(self) -> builtins.str:
        '''Artifact ID for this stack.'''
        result = self._values.get("stack_artifact_id")
        assert result is not None, "Required property 'stack_artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''Name for this stack.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Account where the stack should be deployed.

        :default: - Pipeline account
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assets(self) -> typing.Optional[typing.List[StackAsset]]:
        '''Assets referenced by this stack.

        :default: - No assets
        '''
        result = self._values.get("assets")
        return typing.cast(typing.Optional[typing.List[StackAsset]], result)

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''Role to assume before deploying this stack.

        :default: - Don't assume any role
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''Execution role to pass to CloudFormation.

        :default: - No execution role
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the stack should be deployed.

        :default: - Pipeline region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags to apply to the stack.

        :default: - No tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URL which points to the template asset location in the publishing bucket.

        :default: - Stack template is not published
        '''
        result = self._values.get("template_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StackOutputReference(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.StackOutputReference",
):
    '''A Reference to a Stack Output.

    :exampleMetadata: infused

    Example::

        @jsii.implements(pipelines.ICodePipelineActionFactory)
        class MyLambdaStep(pipelines.Step):
        
            def __init__(self, fn, stack_output):
                super().__init__("MyLambdaStep")
                self.stack_output_reference = pipelines.StackOutputReference.from_cfn_output(stack_output)
        
            def produce_action(self, stage, *, scope, actionName, runOrder, variablesNamespace=None, artifacts, fallbackArtifact=None, pipeline, codeBuildDefaults=None, beforeSelfMutation=None, stackOutputsMap):
        
                stage.add_action(cpactions.LambdaInvokeAction(
                    action_name=action_name,
                    run_order=run_order,
                    # Map the reference to the variable name the CDK has generated for you.
                    user_parameters={"stack_output": stack_outputs_map.to_code_pipeline(self.stack_output_reference)},
                    lambda_=self.fn
                ))
        
                return pipelines.CodePipelineActionFactoryResult(run_orders_consumed=1)public get consumedStackOutputs(): pipelines.StackOutputReference[] {
                return [this.stackOutputReference];
              }
    '''

    @jsii.member(jsii_name="fromCfnOutput")
    @builtins.classmethod
    def from_cfn_output(cls, output: _CfnOutput_7273f911) -> "StackOutputReference":
        '''Create a StackOutputReference that references the given CfnOutput.

        :param output: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d8745bc64df0b3aa6e7dfd1168c6139f2c024dac1d882f0d4af23b942b5ec34)
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
        return typing.cast("StackOutputReference", jsii.sinvoke(cls, "fromCfnOutput", [output]))

    @jsii.member(jsii_name="isProducedBy")
    def is_produced_by(self, stack: StackDeployment) -> builtins.bool:
        '''Whether or not this stack output is being produced by the given Stack deployment.

        :param stack: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b335ec5f93b8ed0338c0e4961948e8606ff0d3b66288aad78ffdd955b373584c)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isProducedBy", [stack]))

    @builtins.property
    @jsii.member(jsii_name="outputName")
    def output_name(self) -> builtins.str:
        '''Output name of the producing stack.'''
        return typing.cast(builtins.str, jsii.get(self, "outputName"))

    @builtins.property
    @jsii.member(jsii_name="stackDescription")
    def stack_description(self) -> builtins.str:
        '''A human-readable description of the producing stack.'''
        return typing.cast(builtins.str, jsii.get(self, "stackDescription"))


class StackOutputsMap(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.StackOutputsMap",
):
    '''Translate stack outputs to Codepipline variable references.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import pipelines
        
        # pipeline_base: pipelines.PipelineBase
        
        stack_outputs_map = pipelines.StackOutputsMap(pipeline_base)
    '''

    def __init__(self, pipeline: PipelineBase) -> None:
        '''
        :param pipeline: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b50e71bc676eac9027f6ea818ba4d747ff0c565ffd3d254888a264b4c946d9bc)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
        jsii.create(self.__class__, self, [pipeline])

    @jsii.member(jsii_name="toCodePipeline")
    def to_code_pipeline(self, x: StackOutputReference) -> builtins.str:
        '''Return the matching variable reference string for a StackOutputReference.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6208cae78a5089ece754de6bca07ee8e0f93d368525e449cb62ab9aa02d5387d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.str, jsii.invoke(self, "toCodePipeline", [x]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.StackSteps",
    jsii_struct_bases=[],
    name_mapping={
        "stack": "stack",
        "change_set": "changeSet",
        "post": "post",
        "pre": "pre",
    },
)
class StackSteps:
    def __init__(
        self,
        *,
        stack: _Stack_2866e57f,
        change_set: typing.Optional[typing.Sequence["Step"]] = None,
        post: typing.Optional[typing.Sequence["Step"]] = None,
        pre: typing.Optional[typing.Sequence["Step"]] = None,
    ) -> None:
        '''Instructions for additional steps that are run at stack level.

        :param stack: The stack you want the steps to run in.
        :param change_set: Steps that execute after stack is prepared but before stack is deployed. Default: - no additional steps
        :param post: Steps that execute after stack is deployed. Default: - no additional steps
        :param pre: Steps that execute before stack is prepared. Default: - no additional steps

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import pipelines
            
            # stack: cdk.Stack
            # step: pipelines.Step
            
            stack_steps = pipelines.StackSteps(
                stack=stack,
            
                # the properties below are optional
                change_set=[step],
                post=[step],
                pre=[step]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca5d40f3edb2136fa92aadc52d7d0d639af5efa3c3907aa21900a78546472e9)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument change_set", value=change_set, expected_type=type_hints["change_set"])
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
            check_type(argname="argument pre", value=pre, expected_type=type_hints["pre"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack": stack,
        }
        if change_set is not None:
            self._values["change_set"] = change_set
        if post is not None:
            self._values["post"] = post
        if pre is not None:
            self._values["pre"] = pre

    @builtins.property
    def stack(self) -> _Stack_2866e57f:
        '''The stack you want the steps to run in.'''
        result = self._values.get("stack")
        assert result is not None, "Required property 'stack' is missing"
        return typing.cast(_Stack_2866e57f, result)

    @builtins.property
    def change_set(self) -> typing.Optional[typing.List["Step"]]:
        '''Steps that execute after stack is prepared but before stack is deployed.

        :default: - no additional steps
        '''
        result = self._values.get("change_set")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    @builtins.property
    def post(self) -> typing.Optional[typing.List["Step"]]:
        '''Steps that execute after stack is deployed.

        :default: - no additional steps
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    @builtins.property
    def pre(self) -> typing.Optional[typing.List["Step"]]:
        '''Steps that execute before stack is prepared.

        :default: - no additional steps
        '''
        result = self._values.get("pre")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StageDeployment(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.StageDeployment",
):
    '''Deployment of a single ``Stage``.

    A ``Stage`` consists of one or more ``Stacks``, which will be
    deployed in dependency order.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import pipelines
        
        # stack: cdk.Stack
        # stage: cdk.Stage
        # step: pipelines.Step
        
        stage_deployment = pipelines.StageDeployment.from_stage(stage,
            post=[step],
            pre=[step],
            stack_steps=[pipelines.StackSteps(
                stack=stack,
        
                # the properties below are optional
                change_set=[step],
                post=[step],
                pre=[step]
            )],
            stage_name="stageName"
        )
    '''

    @jsii.member(jsii_name="fromStage")
    @builtins.classmethod
    def from_stage(
        cls,
        stage: _Stage_7df8511b,
        *,
        post: typing.Optional[typing.Sequence["Step"]] = None,
        pre: typing.Optional[typing.Sequence["Step"]] = None,
        stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
        stage_name: typing.Optional[builtins.str] = None,
    ) -> "StageDeployment":
        '''Create a new ``StageDeployment`` from a ``Stage``.

        Synthesizes the target stage, and deployes the stacks found inside
        in dependency order.

        :param stage: -
        :param post: Additional steps to run after all of the stacks in the stage. Default: - No additional steps
        :param pre: Additional steps to run before any of the stacks in the stage. Default: - No additional steps
        :param stack_steps: Instructions for additional steps that are run at the stack level. Default: - No additional instructions
        :param stage_name: Stage name to use in the pipeline. Default: - Use Stage's construct ID
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a37efd4695086f03c4f48796707d94ae7caf71cecf52f15940e3a454ddce14cf)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        props = StageDeploymentProps(
            post=post, pre=pre, stack_steps=stack_steps, stage_name=stage_name
        )

        return typing.cast("StageDeployment", jsii.sinvoke(cls, "fromStage", [stage, props]))

    @jsii.member(jsii_name="addPost")
    def add_post(self, *steps: "Step") -> None:
        '''Add an additional step to run after all of the stacks in this stage.

        :param steps: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7963424ad1d642071b0d2ad14e4d5fc16fe9da5684fa99810d45cdd45456ff78)
            check_type(argname="argument steps", value=steps, expected_type=typing.Tuple[type_hints["steps"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addPost", [*steps]))

    @jsii.member(jsii_name="addPre")
    def add_pre(self, *steps: "Step") -> None:
        '''Add an additional step to run before any of the stacks in this stage.

        :param steps: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b5cab7f97e36643320ecd39f081f32d2abc1c31b1aaf8ce2dc42ca0656bd163)
            check_type(argname="argument steps", value=steps, expected_type=typing.Tuple[type_hints["steps"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addPre", [*steps]))

    @builtins.property
    @jsii.member(jsii_name="post")
    def post(self) -> typing.List["Step"]:
        '''Additional steps that are run after all of the stacks in the stage.'''
        return typing.cast(typing.List["Step"], jsii.get(self, "post"))

    @builtins.property
    @jsii.member(jsii_name="pre")
    def pre(self) -> typing.List["Step"]:
        '''Additional steps that are run before any of the stacks in the stage.'''
        return typing.cast(typing.List["Step"], jsii.get(self, "pre"))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[StackDeployment]:
        '''The stacks deployed in this stage.'''
        return typing.cast(typing.List[StackDeployment], jsii.get(self, "stacks"))

    @builtins.property
    @jsii.member(jsii_name="stackSteps")
    def stack_steps(self) -> typing.List[StackSteps]:
        '''Instructions for additional steps that are run at stack level.'''
        return typing.cast(typing.List[StackSteps], jsii.get(self, "stackSteps"))

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> builtins.str:
        '''The display name of this stage.'''
        return typing.cast(builtins.str, jsii.get(self, "stageName"))

    @builtins.property
    @jsii.member(jsii_name="prepareStep")
    def prepare_step(self) -> typing.Optional[builtins.bool]:
        '''Determine if all stacks in stage should be deployed with prepare step or not.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "prepareStep"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.StageDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "post": "post",
        "pre": "pre",
        "stack_steps": "stackSteps",
        "stage_name": "stageName",
    },
)
class StageDeploymentProps:
    def __init__(
        self,
        *,
        post: typing.Optional[typing.Sequence["Step"]] = None,
        pre: typing.Optional[typing.Sequence["Step"]] = None,
        stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
        stage_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a ``StageDeployment``.

        :param post: Additional steps to run after all of the stacks in the stage. Default: - No additional steps
        :param pre: Additional steps to run before any of the stacks in the stage. Default: - No additional steps
        :param stack_steps: Instructions for additional steps that are run at the stack level. Default: - No additional instructions
        :param stage_name: Stage name to use in the pipeline. Default: - Use Stage's construct ID

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import pipelines
            
            # stack: cdk.Stack
            # step: pipelines.Step
            
            stage_deployment_props = pipelines.StageDeploymentProps(
                post=[step],
                pre=[step],
                stack_steps=[pipelines.StackSteps(
                    stack=stack,
            
                    # the properties below are optional
                    change_set=[step],
                    post=[step],
                    pre=[step]
                )],
                stage_name="stageName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2996b2e68f1aa0af80a6355038a15e330c41d048b4db733659fb5dacf94c7fad)
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
            check_type(argname="argument pre", value=pre, expected_type=type_hints["pre"])
            check_type(argname="argument stack_steps", value=stack_steps, expected_type=type_hints["stack_steps"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if post is not None:
            self._values["post"] = post
        if pre is not None:
            self._values["pre"] = pre
        if stack_steps is not None:
            self._values["stack_steps"] = stack_steps
        if stage_name is not None:
            self._values["stage_name"] = stage_name

    @builtins.property
    def post(self) -> typing.Optional[typing.List["Step"]]:
        '''Additional steps to run after all of the stacks in the stage.

        :default: - No additional steps
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    @builtins.property
    def pre(self) -> typing.Optional[typing.List["Step"]]:
        '''Additional steps to run before any of the stacks in the stage.

        :default: - No additional steps
        '''
        result = self._values.get("pre")
        return typing.cast(typing.Optional[typing.List["Step"]], result)

    @builtins.property
    def stack_steps(self) -> typing.Optional[typing.List[StackSteps]]:
        '''Instructions for additional steps that are run at the stack level.

        :default: - No additional instructions
        '''
        result = self._values.get("stack_steps")
        return typing.cast(typing.Optional[typing.List[StackSteps]], result)

    @builtins.property
    def stage_name(self) -> typing.Optional[builtins.str]:
        '''Stage name to use in the pipeline.

        :default: - Use Stage's construct ID
        '''
        result = self._values.get("stage_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StageDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IFileSetProducer)
class Step(metaclass=jsii.JSIIAbstractClass, jsii_type="aws-cdk-lib.pipelines.Step"):
    '''A generic Step which can be added to a Pipeline.

    Steps can be used to add Sources, Build Actions and Validations
    to your pipeline.

    This class is abstract. See specific subclasses of Step for
    useful steps to add to your Pipeline

    :exampleMetadata: infused

    Example::

        @jsii.implements(pipelines.ICodePipelineActionFactory)
        class MyJenkinsStep(pipelines.Step):
            def __init__(self, provider, input):
                super().__init__("MyJenkinsStep")
        
                # This is necessary if your step accepts parameters, like environment variables,
                # that may contain outputs from other steps. It doesn't matter what the
                # structure is, as long as it contains the values that may contain outputs.
                self.discover_referenced_outputs({
                    "env": {}
                })
        
            def produce_action(self, stage, *, scope, actionName, runOrder, variablesNamespace=None, artifacts, fallbackArtifact=None, pipeline, codeBuildDefaults=None, beforeSelfMutation=None, stackOutputsMap):
        
                # This is where you control what type of Action gets added to the
                # CodePipeline
                stage.add_action(cpactions.JenkinsAction(
                    # Copy 'actionName' and 'runOrder' from the options
                    action_name=action_name,
                    run_order=run_order,
        
                    # Jenkins-specific configuration
                    type=cpactions.JenkinsActionType.TEST,
                    jenkins_provider=self.provider,
                    project_name="MyJenkinsProject",
        
                    # Translate the FileSet into a codepipeline.Artifact
                    inputs=[artifacts.to_code_pipeline(self.input)]
                ))
        
                return pipelines.CodePipelineActionFactoryResult(run_orders_consumed=1)
    '''

    def __init__(self, id: builtins.str) -> None:
        '''
        :param id: Identifier for this step.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68aaec030807cfbf351299f9c26e438985ce3f9e77a2ce6ee7cd9160ecaef59f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [id])

    @jsii.member(jsii_name="sequence")
    @builtins.classmethod
    def sequence(cls, steps: typing.Sequence["Step"]) -> typing.List["Step"]:
        '''Define a sequence of steps to be executed in order.

        If you need more fine-grained step ordering, use the ``addStepDependency()``
        API. For example, if you want ``secondStep`` to occur after ``firstStep``, call
        ``secondStep.addStepDependency(firstStep)``.

        :param steps: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fa8ee52263a2c85e05e23d26dc40cc78dfc1127b9b95c510f018a6cfed478c6)
            check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
        return typing.cast(typing.List["Step"], jsii.sinvoke(cls, "sequence", [steps]))

    @jsii.member(jsii_name="addDependencyFileSet")
    def _add_dependency_file_set(self, fs: "FileSet") -> None:
        '''Add an additional FileSet to the set of file sets required by this step.

        This will lead to a dependency on the producer of that file set.

        :param fs: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb3c0f82c71c42c1f93221292b7dbffbe572c7ea5a260f598cb89a5fa77db6f9)
            check_type(argname="argument fs", value=fs, expected_type=type_hints["fs"])
        return typing.cast(None, jsii.invoke(self, "addDependencyFileSet", [fs]))

    @jsii.member(jsii_name="addStepDependency")
    def add_step_dependency(self, step: "Step") -> None:
        '''Add a dependency on another step.

        :param step: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78f54be98abfd0174d463663607bb14370b7402ee77874895f6bfed4c698e909)
            check_type(argname="argument step", value=step, expected_type=type_hints["step"])
        return typing.cast(None, jsii.invoke(self, "addStepDependency", [step]))

    @jsii.member(jsii_name="configurePrimaryOutput")
    def _configure_primary_output(self, fs: "FileSet") -> None:
        '''Configure the given FileSet as the primary output of this step.

        :param fs: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a068aee785ec3c9e9f1809d52708b5df8f13355aa9740ec37f0a9ee74e1110d4)
            check_type(argname="argument fs", value=fs, expected_type=type_hints["fs"])
        return typing.cast(None, jsii.invoke(self, "configurePrimaryOutput", [fs]))

    @jsii.member(jsii_name="discoverReferencedOutputs")
    def _discover_referenced_outputs(self, structure: typing.Any) -> None:
        '''Crawl the given structure for references to StepOutputs and add dependencies on all steps found.

        Should be called in the constructor of subclasses based on what the user
        passes in as construction properties. The format of the structure passed in
        here does not have to correspond exactly to what gets rendered into the
        engine, it just needs to contain the same data.

        :param structure: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__861dc4a9082e25f4892e3dc0b3e109591bed56d6d69e131b65606d9ce139cfc4)
            check_type(argname="argument structure", value=structure, expected_type=type_hints["structure"])
        return typing.cast(None, jsii.invoke(self, "discoverReferencedOutputs", [structure]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Return a string representation of this Step.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="consumedStackOutputs")
    def consumed_stack_outputs(self) -> typing.List[StackOutputReference]:
        '''StackOutputReferences this step consumes.'''
        return typing.cast(typing.List[StackOutputReference], jsii.get(self, "consumedStackOutputs"))

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["Step"]:
        '''Return the steps this step depends on, based on the FileSets it requires.'''
        return typing.cast(typing.List["Step"], jsii.get(self, "dependencies"))

    @builtins.property
    @jsii.member(jsii_name="dependencyFileSets")
    def dependency_file_sets(self) -> typing.List["FileSet"]:
        '''The list of FileSets consumed by this Step.'''
        return typing.cast(typing.List["FileSet"], jsii.get(self, "dependencyFileSets"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Identifier for this step.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="isSource")
    def is_source(self) -> builtins.bool:
        '''Whether or not this is a Source step.

        What it means to be a Source step depends on the engine.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isSource"))

    @builtins.property
    @jsii.member(jsii_name="primaryOutput")
    def primary_output(self) -> typing.Optional["FileSet"]:
        '''The primary FileSet produced by this Step.

        Not all steps produce an output FileSet--if they do
        you can substitute the ``Step`` object for the ``FileSet`` object.
        '''
        return typing.cast(typing.Optional["FileSet"], jsii.get(self, "primaryOutput"))


class _StepProxy(Step):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Step).__jsii_proxy_class__ = lambda : _StepProxy


class Wave(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.pipelines.Wave"):
    '''Multiple stages that are deployed in parallel.

    :exampleMetadata: infused

    Example::

        # pipeline: pipelines.CodePipeline
        
        europe_wave = pipeline.add_wave("Europe")
        europe_wave.add_stage(MyApplicationStage(self, "Ireland",
            env=cdk.Environment(region="eu-west-1")
        ))
        europe_wave.add_stage(MyApplicationStage(self, "Germany",
            env=cdk.Environment(region="eu-central-1")
        ))
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        post: typing.Optional[typing.Sequence[Step]] = None,
        pre: typing.Optional[typing.Sequence[Step]] = None,
    ) -> None:
        '''
        :param id: Identifier for this Wave.
        :param post: Additional steps to run after all of the stages in the wave. Default: - No additional steps
        :param pre: Additional steps to run before any of the stages in the wave. Default: - No additional steps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19399be49c5895136165e92f8d4f261ada55bda465bbe03748a50eeb2565059)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WaveProps(post=post, pre=pre)

        jsii.create(self.__class__, self, [id, props])

    @jsii.member(jsii_name="addPost")
    def add_post(self, *steps: Step) -> None:
        '''Add an additional step to run after all of the stages in this wave.

        :param steps: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8581b4bbbe78eda4fb8dbcb1f3b771c7cf048db7cf5a72e03d64f96e57598299)
            check_type(argname="argument steps", value=steps, expected_type=typing.Tuple[type_hints["steps"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addPost", [*steps]))

    @jsii.member(jsii_name="addPre")
    def add_pre(self, *steps: Step) -> None:
        '''Add an additional step to run before any of the stages in this wave.

        :param steps: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66516b0f8ad368fac42e7dcdd790b28e1dfb19cb9b17305cf356abd5a2b9849a)
            check_type(argname="argument steps", value=steps, expected_type=typing.Tuple[type_hints["steps"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addPre", [*steps]))

    @jsii.member(jsii_name="addStage")
    def add_stage(
        self,
        stage: _Stage_7df8511b,
        *,
        post: typing.Optional[typing.Sequence[Step]] = None,
        pre: typing.Optional[typing.Sequence[Step]] = None,
        stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> StageDeployment:
        '''Add a Stage to this wave.

        It will be deployed in parallel with all other stages in this
        wave.

        :param stage: -
        :param post: Additional steps to run after all of the stacks in the stage. Default: - No additional steps
        :param pre: Additional steps to run before any of the stacks in the stage. Default: - No additional steps
        :param stack_steps: Instructions for stack level steps. Default: - No additional instructions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7590cd60f1f21f8e0847610459550f1b62de25d7e9041a32e959d55e075a7f62)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        options = AddStageOpts(post=post, pre=pre, stack_steps=stack_steps)

        return typing.cast(StageDeployment, jsii.invoke(self, "addStage", [stage, options]))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Identifier for this Wave.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="post")
    def post(self) -> typing.List[Step]:
        '''Additional steps that are run after all of the stages in the wave.'''
        return typing.cast(typing.List[Step], jsii.get(self, "post"))

    @builtins.property
    @jsii.member(jsii_name="pre")
    def pre(self) -> typing.List[Step]:
        '''Additional steps that are run before any of the stages in the wave.'''
        return typing.cast(typing.List[Step], jsii.get(self, "pre"))

    @builtins.property
    @jsii.member(jsii_name="stages")
    def stages(self) -> typing.List[StageDeployment]:
        '''The stages that are deployed in this wave.'''
        return typing.cast(typing.List[StageDeployment], jsii.get(self, "stages"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.WaveOptions",
    jsii_struct_bases=[],
    name_mapping={"post": "post", "pre": "pre"},
)
class WaveOptions:
    def __init__(
        self,
        *,
        post: typing.Optional[typing.Sequence[Step]] = None,
        pre: typing.Optional[typing.Sequence[Step]] = None,
    ) -> None:
        '''Options to pass to ``addWave``.

        :param post: Additional steps to run after all of the stages in the wave. Default: - No additional steps
        :param pre: Additional steps to run before any of the stages in the wave. Default: - No additional steps

        :exampleMetadata: infused

        Example::

            pipeline = pipelines.CodePipeline(self, "Pipeline",
                synth=pipelines.ShellStep("Synth",
                    input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                        connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                    ),
                    commands=["npm ci", "npm run build", "npx cdk synth"]
                ),
            
                # Turn this on because the pipeline uses Docker image assets
                docker_enabled_for_self_mutation=True
            )
            
            pipeline.add_wave("MyWave",
                post=[
                    pipelines.CodeBuildStep("RunApproval",
                        commands=["command-from-image"],
                        build_environment=codebuild.BuildEnvironment(
                            # The user of a Docker image asset in the pipeline requires turning on
                            # 'dockerEnabledForSelfMutation'.
                            build_image=codebuild.LinuxBuildImage.from_asset(self, "Image",
                                directory="./docker-image"
                            )
                        )
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2277271dc82c44ce8955ce65457db799bd6e52de92bcc11a17652ce9c46ab6a)
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
            check_type(argname="argument pre", value=pre, expected_type=type_hints["pre"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if post is not None:
            self._values["post"] = post
        if pre is not None:
            self._values["pre"] = pre

    @builtins.property
    def post(self) -> typing.Optional[typing.List[Step]]:
        '''Additional steps to run after all of the stages in the wave.

        :default: - No additional steps
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[typing.List[Step]], result)

    @builtins.property
    def pre(self) -> typing.Optional[typing.List[Step]]:
        '''Additional steps to run before any of the stages in the wave.

        :default: - No additional steps
        '''
        result = self._values.get("pre")
        return typing.cast(typing.Optional[typing.List[Step]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.WaveProps",
    jsii_struct_bases=[],
    name_mapping={"post": "post", "pre": "pre"},
)
class WaveProps:
    def __init__(
        self,
        *,
        post: typing.Optional[typing.Sequence[Step]] = None,
        pre: typing.Optional[typing.Sequence[Step]] = None,
    ) -> None:
        '''Construction properties for a ``Wave``.

        :param post: Additional steps to run after all of the stages in the wave. Default: - No additional steps
        :param pre: Additional steps to run before any of the stages in the wave. Default: - No additional steps

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import pipelines
            
            # step: pipelines.Step
            
            wave_props = pipelines.WaveProps(
                post=[step],
                pre=[step]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04297c0a279df0deb627a2db37c6345071a7dbd35ce5f96fbe3b3e08dacfc8a6)
            check_type(argname="argument post", value=post, expected_type=type_hints["post"])
            check_type(argname="argument pre", value=pre, expected_type=type_hints["pre"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if post is not None:
            self._values["post"] = post
        if pre is not None:
            self._values["pre"] = pre

    @builtins.property
    def post(self) -> typing.Optional[typing.List[Step]]:
        '''Additional steps to run after all of the stages in the wave.

        :default: - No additional steps
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[typing.List[Step]], result)

    @builtins.property
    def pre(self) -> typing.Optional[typing.List[Step]]:
        '''Additional steps to run before any of the stages in the wave.

        :default: - No additional steps
        '''
        result = self._values.get("pre")
        return typing.cast(typing.Optional[typing.List[Step]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaveProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.pipelines.CodeBuildStepProps",
    jsii_struct_bases=[ShellStepProps],
    name_mapping={
        "commands": "commands",
        "additional_inputs": "additionalInputs",
        "env": "env",
        "env_from_cfn_outputs": "envFromCfnOutputs",
        "input": "input",
        "install_commands": "installCommands",
        "primary_output_directory": "primaryOutputDirectory",
        "action_role": "actionRole",
        "build_environment": "buildEnvironment",
        "cache": "cache",
        "file_system_locations": "fileSystemLocations",
        "logging": "logging",
        "partial_build_spec": "partialBuildSpec",
        "project_name": "projectName",
        "role": "role",
        "role_policy_statements": "rolePolicyStatements",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class CodeBuildStepProps(ShellStepProps):
    def __init__(
        self,
        *,
        commands: typing.Sequence[builtins.str],
        additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
        input: typing.Optional[IFileSetProducer] = None,
        install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary_output_directory: typing.Optional[builtins.str] = None,
        action_role: typing.Optional[_IRole_235f5d8e] = None,
        build_environment: typing.Optional[typing.Union[_BuildEnvironment_4ee6fb51, typing.Dict[builtins.str, typing.Any]]] = None,
        cache: typing.Optional[_Cache_ed12d453] = None,
        file_system_locations: typing.Optional[typing.Sequence[_IFileSystemLocation_acb87263]] = None,
        logging: typing.Optional[typing.Union[_LoggingOptions_31668710, typing.Dict[builtins.str, typing.Any]]] = None,
        partial_build_spec: typing.Optional[_BuildSpec_4961ea5b] = None,
        project_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        role_policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
    ) -> None:
        '''Construction props for a CodeBuildStep.

        :param commands: Commands to run.
        :param additional_inputs: Additional FileSets to put in other directories. Specifies a mapping from directory name to FileSets. During the script execution, the FileSets will be available in the directories indicated. The directory names may be relative. For example, you can put the main input and an additional input side-by-side with the following configuration:: const script = new pipelines.ShellStep('MainScript', { commands: ['npm ci','npm run build','npx cdk synth'], input: pipelines.CodePipelineSource.gitHub('org/source1', 'main'), additionalInputs: { '../siblingdir': pipelines.CodePipelineSource.gitHub('org/source2', 'main'), } }); Default: - No additional inputs
        :param env: Environment variables to set. Default: - No environment variables
        :param env_from_cfn_outputs: Set environment variables based on Stack Outputs. ``ShellStep``s following stack or stage deployments may access the ``CfnOutput``s of those stacks to get access to --for example--automatically generated resource names or endpoint URLs. Default: - No environment variables created from stack outputs
        :param input: FileSet to run these scripts on. The files in the FileSet will be placed in the working directory when the script is executed. Use ``additionalInputs`` to download file sets to other directories as well. Default: - No input specified
        :param install_commands: Installation commands to run before the regular commands. For deployment engines that support it, install commands will be classified differently in the job history from the regular ``commands``. Default: - No installation commands
        :param primary_output_directory: The directory that will contain the primary output fileset. After running the script, the contents of the given directory will be treated as the primary output of this Step. Default: - No primary output
        :param action_role: Custom execution role to be used for the Code Build Action. Default: - A role is automatically created
        :param build_environment: Changes to environment. This environment will be combined with the pipeline's default environment. Default: - Use the pipeline's default build environment
        :param cache: Caching strategy to use. Default: - No cache
        :param file_system_locations: ProjectFileSystemLocation objects for CodeBuild build projects. A ProjectFileSystemLocation object specifies the identifier, location, mountOptions, mountPoint, and type of a file system created using Amazon Elastic File System. Default: - no file system locations
        :param logging: Information about logs for CodeBuild projects. A CodeBuild project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both. Default: - no log configuration is set
        :param partial_build_spec: Additional configuration that can only be configured via BuildSpec. You should not use this to specify output artifacts; those should be supplied via the other properties of this class, otherwise CDK Pipelines won't be able to inspect the artifacts. Set the ``commands`` to an empty array if you want to fully specify the BuildSpec using this field. The BuildSpec must be available inline--it cannot reference a file on disk. Default: - BuildSpec completely derived from other properties
        :param project_name: Name for the generated CodeBuild project. Default: - Automatically generated
        :param role: Custom execution role to be used for the CodeBuild project. Default: - A role is automatically created
        :param role_policy_statements: Policy statements to add to role used during the synth. Can be used to add acces to a CodeArtifact repository etc. Default: - No policy statements added to CodeBuild Project Role
        :param security_groups: Which security group to associate with the script's project network interfaces. If no security group is identified, one will be created automatically. Only used if 'vpc' is supplied. Default: - Security group will be automatically created.
        :param subnet_selection: Which subnets to use. Only used if 'vpc' is supplied. Default: - All private subnets.
        :param timeout: The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: The VPC where to execute the SimpleSynth. Default: - No VPC

        :exampleMetadata: infused

        Example::

            pipeline = pipelines.CodePipeline(self, "Pipeline",
                synth=pipelines.ShellStep("Synth",
                    input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                        connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                    ),
                    commands=["npm ci", "npm run build", "npx cdk synth"]
                ),
            
                # Turn this on because the pipeline uses Docker image assets
                docker_enabled_for_self_mutation=True
            )
            
            pipeline.add_wave("MyWave",
                post=[
                    pipelines.CodeBuildStep("RunApproval",
                        commands=["command-from-image"],
                        build_environment=codebuild.BuildEnvironment(
                            # The user of a Docker image asset in the pipeline requires turning on
                            # 'dockerEnabledForSelfMutation'.
                            build_image=codebuild.LinuxBuildImage.from_asset(self, "Image",
                                directory="./docker-image"
                            )
                        )
                    )
                ]
            )
        '''
        if isinstance(build_environment, dict):
            build_environment = _BuildEnvironment_4ee6fb51(**build_environment)
        if isinstance(logging, dict):
            logging = _LoggingOptions_31668710(**logging)
        if isinstance(subnet_selection, dict):
            subnet_selection = _SubnetSelection_e57d76df(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ea003fb723e489b2aa741146d04bb6e1e31bf776d6e79aadf14deb5a715643)
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument additional_inputs", value=additional_inputs, expected_type=type_hints["additional_inputs"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument env_from_cfn_outputs", value=env_from_cfn_outputs, expected_type=type_hints["env_from_cfn_outputs"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument install_commands", value=install_commands, expected_type=type_hints["install_commands"])
            check_type(argname="argument primary_output_directory", value=primary_output_directory, expected_type=type_hints["primary_output_directory"])
            check_type(argname="argument action_role", value=action_role, expected_type=type_hints["action_role"])
            check_type(argname="argument build_environment", value=build_environment, expected_type=type_hints["build_environment"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument file_system_locations", value=file_system_locations, expected_type=type_hints["file_system_locations"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument partial_build_spec", value=partial_build_spec, expected_type=type_hints["partial_build_spec"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument role_policy_statements", value=role_policy_statements, expected_type=type_hints["role_policy_statements"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "commands": commands,
        }
        if additional_inputs is not None:
            self._values["additional_inputs"] = additional_inputs
        if env is not None:
            self._values["env"] = env
        if env_from_cfn_outputs is not None:
            self._values["env_from_cfn_outputs"] = env_from_cfn_outputs
        if input is not None:
            self._values["input"] = input
        if install_commands is not None:
            self._values["install_commands"] = install_commands
        if primary_output_directory is not None:
            self._values["primary_output_directory"] = primary_output_directory
        if action_role is not None:
            self._values["action_role"] = action_role
        if build_environment is not None:
            self._values["build_environment"] = build_environment
        if cache is not None:
            self._values["cache"] = cache
        if file_system_locations is not None:
            self._values["file_system_locations"] = file_system_locations
        if logging is not None:
            self._values["logging"] = logging
        if partial_build_spec is not None:
            self._values["partial_build_spec"] = partial_build_spec
        if project_name is not None:
            self._values["project_name"] = project_name
        if role is not None:
            self._values["role"] = role
        if role_policy_statements is not None:
            self._values["role_policy_statements"] = role_policy_statements
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def commands(self) -> typing.List[builtins.str]:
        '''Commands to run.'''
        result = self._values.get("commands")
        assert result is not None, "Required property 'commands' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def additional_inputs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]]:
        '''Additional FileSets to put in other directories.

        Specifies a mapping from directory name to FileSets. During the
        script execution, the FileSets will be available in the directories
        indicated.

        The directory names may be relative. For example, you can put
        the main input and an additional input side-by-side with the
        following configuration::

           script = pipelines.ShellStep("MainScript",
               commands=["npm ci", "npm run build", "npx cdk synth"],
               input=pipelines.CodePipelineSource.git_hub("org/source1", "main"),
               additional_inputs={
                   "../siblingdir": pipelines.CodePipelineSource.git_hub("org/source2", "main")
               }
           )

        :default: - No additional inputs
        '''
        result = self._values.get("additional_inputs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Environment variables to set.

        :default: - No environment variables
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def env_from_cfn_outputs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]]:
        '''Set environment variables based on Stack Outputs.

        ``ShellStep``s following stack or stage deployments may
        access the ``CfnOutput``s of those stacks to get access to
        --for example--automatically generated resource names or
        endpoint URLs.

        :default: - No environment variables created from stack outputs
        '''
        result = self._values.get("env_from_cfn_outputs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]], result)

    @builtins.property
    def input(self) -> typing.Optional[IFileSetProducer]:
        '''FileSet to run these scripts on.

        The files in the FileSet will be placed in the working directory when
        the script is executed. Use ``additionalInputs`` to download file sets
        to other directories as well.

        :default: - No input specified
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[IFileSetProducer], result)

    @builtins.property
    def install_commands(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Installation commands to run before the regular commands.

        For deployment engines that support it, install commands will be classified
        differently in the job history from the regular ``commands``.

        :default: - No installation commands
        '''
        result = self._values.get("install_commands")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def primary_output_directory(self) -> typing.Optional[builtins.str]:
        '''The directory that will contain the primary output fileset.

        After running the script, the contents of the given directory
        will be treated as the primary output of this Step.

        :default: - No primary output
        '''
        result = self._values.get("primary_output_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Custom execution role to be used for the Code Build Action.

        :default: - A role is automatically created
        '''
        result = self._values.get("action_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def build_environment(self) -> typing.Optional[_BuildEnvironment_4ee6fb51]:
        '''Changes to environment.

        This environment will be combined with the pipeline's default
        environment.

        :default: - Use the pipeline's default build environment
        '''
        result = self._values.get("build_environment")
        return typing.cast(typing.Optional[_BuildEnvironment_4ee6fb51], result)

    @builtins.property
    def cache(self) -> typing.Optional[_Cache_ed12d453]:
        '''Caching strategy to use.

        :default: - No cache
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[_Cache_ed12d453], result)

    @builtins.property
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.List[_IFileSystemLocation_acb87263]]:
        '''ProjectFileSystemLocation objects for CodeBuild build projects.

        A ProjectFileSystemLocation object specifies the identifier, location, mountOptions, mountPoint,
        and type of a file system created using Amazon Elastic File System.

        :default: - no file system locations
        '''
        result = self._values.get("file_system_locations")
        return typing.cast(typing.Optional[typing.List[_IFileSystemLocation_acb87263]], result)

    @builtins.property
    def logging(self) -> typing.Optional[_LoggingOptions_31668710]:
        '''Information about logs for CodeBuild projects.

        A CodeBuild project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both.

        :default: - no log configuration is set
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[_LoggingOptions_31668710], result)

    @builtins.property
    def partial_build_spec(self) -> typing.Optional[_BuildSpec_4961ea5b]:
        '''Additional configuration that can only be configured via BuildSpec.

        You should not use this to specify output artifacts; those
        should be supplied via the other properties of this class, otherwise
        CDK Pipelines won't be able to inspect the artifacts.

        Set the ``commands`` to an empty array if you want to fully specify
        the BuildSpec using this field.

        The BuildSpec must be available inline--it cannot reference a file
        on disk.

        :default: - BuildSpec completely derived from other properties
        '''
        result = self._values.get("partial_build_spec")
        return typing.cast(typing.Optional[_BuildSpec_4961ea5b], result)

    @builtins.property
    def project_name(self) -> typing.Optional[builtins.str]:
        '''Name for the generated CodeBuild project.

        :default: - Automatically generated
        '''
        result = self._values.get("project_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Custom execution role to be used for the CodeBuild project.

        :default: - A role is automatically created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def role_policy_statements(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Policy statements to add to role used during the synth.

        Can be used to add acces to a CodeArtifact repository etc.

        :default: - No policy statements added to CodeBuild Project Role
        '''
        result = self._values.get("role_policy_statements")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''Which security group to associate with the script's project network interfaces.

        If no security group is identified, one will be created automatically.

        Only used if 'vpc' is supplied.

        :default: - Security group will be automatically created.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Which subnets to use.

        Only used if 'vpc' is supplied.

        :default: - All private subnets.
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The VPC where to execute the SimpleSynth.

        :default: - No VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildStepProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodePipeline(
    PipelineBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.CodePipeline",
):
    '''A CDK Pipeline that uses CodePipeline to deploy CDK apps.

    This is a ``Pipeline`` with its ``engine`` property set to
    ``CodePipelineEngine``, and exists for nicer ergonomics for
    users that don't need to switch out engines.

    :exampleMetadata: infused

    Example::

        # Modern API
        modern_pipeline = pipelines.CodePipeline(self, "Pipeline",
            self_mutation=False,
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"
                ]
            )
        )
        
        # Original API
        cloud_assembly_artifact = codepipeline.Artifact()
        original_pipeline = pipelines.CdkPipeline(self, "Pipeline",
            self_mutating=False,
            cloud_assembly_artifact=cloud_assembly_artifact
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        synth: IFileSetProducer,
        artifact_bucket: typing.Optional[_IBucket_42e086fd] = None,
        asset_publishing_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cli_version: typing.Optional[builtins.str] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        code_pipeline: typing.Optional[_Pipeline_ea38de84] = None,
        cross_account_keys: typing.Optional[builtins.bool] = None,
        cross_region_replication_buckets: typing.Optional[typing.Mapping[builtins.str, _IBucket_42e086fd]] = None,
        docker_credentials: typing.Optional[typing.Sequence[DockerCredential]] = None,
        docker_enabled_for_self_mutation: typing.Optional[builtins.bool] = None,
        docker_enabled_for_synth: typing.Optional[builtins.bool] = None,
        enable_key_rotation: typing.Optional[builtins.bool] = None,
        pipeline_name: typing.Optional[builtins.str] = None,
        publish_assets_in_parallel: typing.Optional[builtins.bool] = None,
        reuse_cross_region_support_stacks: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        self_mutation: typing.Optional[builtins.bool] = None,
        self_mutation_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        synth_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        use_change_sets: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param synth: The build step that produces the CDK Cloud Assembly. The primary output of this step needs to be the ``cdk.out`` directory generated by the ``cdk synth`` command. If you use a ``ShellStep`` here and you don't configure an output directory, the output directory will automatically be assumed to be ``cdk.out``.
        :param artifact_bucket: An existing S3 Bucket to use for storing the pipeline's artifact. Default: - A new S3 bucket will be created.
        :param asset_publishing_code_build_defaults: Additional customizations to apply to the asset publishing CodeBuild projects. Default: - Only ``codeBuildDefaults`` are applied
        :param cli_version: CDK CLI version to use in self-mutation and asset publishing steps. If you want to lock the CDK CLI version used in the pipeline, by steps that are automatically generated for you, specify the version here. We recommend you do not specify this value, as not specifying it always uses the latest CLI version which is backwards compatible with old versions. If you do specify it, be aware that this version should always be equal to or higher than the version of the CDK framework used by the CDK app, when the CDK commands are run during your pipeline execution. When you change this version, the *next time* the ``SelfMutate`` step runs it will still be using the CLI of the the *previous* version that was in this property: it will only start using the new version after ``SelfMutate`` completes successfully. That means that if you want to update both framework and CLI version, you should update the CLI version first, commit, push and deploy, and only then update the framework version. Default: - Latest version
        :param code_build_defaults: Customize the CodeBuild projects created for this pipeline. Default: - All projects run non-privileged build, SMALL instance, LinuxBuildImage.STANDARD_7_0
        :param code_pipeline: An existing Pipeline to be reused and built upon. [disable-awslint:ref-via-interface] Default: - a new underlying pipeline is created.
        :param cross_account_keys: Create KMS keys for the artifact buckets, allowing cross-account deployments. The artifact buckets have to be encrypted to support deploying CDK apps to another account, so if you want to do that or want to have your artifact buckets encrypted, be sure to set this value to ``true``. Be aware there is a cost associated with maintaining the KMS keys. Default: false
        :param cross_region_replication_buckets: A map of region to S3 bucket name used for cross-region CodePipeline. For every Action that you specify targeting a different region than the Pipeline itself, if you don't provide an explicit Bucket for that region using this property, the construct will automatically create a Stack containing an S3 Bucket in that region. Passed directly through to the {@link cp.Pipeline}. Default: - no cross region replication buckets.
        :param docker_credentials: A list of credentials used to authenticate to Docker registries. Specify any credentials necessary within the pipeline to build, synth, update, or publish assets. Default: []
        :param docker_enabled_for_self_mutation: Enable Docker for the self-mutate step. Set this to true if the pipeline itself uses Docker container assets (for example, if you use ``LinuxBuildImage.fromAsset()`` as the build image of a CodeBuild step in the pipeline). You do not need to set it if you build Docker image assets in the application Stages and Stacks that are *deployed* by this pipeline. Configures privileged mode for the self-mutation CodeBuild action. If you are about to turn this on in an already-deployed Pipeline, set the value to ``true`` first, commit and allow the pipeline to self-update, and only then use the Docker asset in the pipeline. Default: false
        :param docker_enabled_for_synth: Enable Docker for the 'synth' step. Set this to true if you are using file assets that require "bundling" anywhere in your application (meaning an asset compilation step will be run with the tools provided by a Docker image), both for the Pipeline stack as well as the application stacks. A common way to use bundling assets in your application is by using the ``aws-cdk-lib/aws-lambda-nodejs`` library. Configures privileged mode for the synth CodeBuild action. If you are about to turn this on in an already-deployed Pipeline, set the value to ``true`` first, commit and allow the pipeline to self-update, and only then use the bundled asset. Default: false
        :param enable_key_rotation: Enable KMS key rotation for the generated KMS keys. By default KMS key rotation is disabled, but will add additional costs when enabled. Default: - false (key rotation is disabled)
        :param pipeline_name: The name of the CodePipeline pipeline. Default: - Automatically generated
        :param publish_assets_in_parallel: Publish assets in multiple CodeBuild projects. If set to false, use one Project per type to publish all assets. Publishing in parallel improves concurrency and may reduce publishing latency, but may also increase overall provisioning time of the CodeBuild projects. Experiment and see what value works best for you. Default: true
        :param reuse_cross_region_support_stacks: Reuse the same cross region support stack for all pipelines in the App. Default: - true (Use the same support stack for all pipelines in App)
        :param role: The IAM role to be assumed by this Pipeline. Default: - A new role is created
        :param self_mutation: Whether the pipeline will update itself. This needs to be set to ``true`` to allow the pipeline to reconfigure itself when assets or stages are being added to it, and ``true`` is the recommended setting. You can temporarily set this to ``false`` while you are iterating on the pipeline itself and prefer to deploy changes using ``cdk deploy``. Default: true
        :param self_mutation_code_build_defaults: Additional customizations to apply to the self mutation CodeBuild projects. Default: - Only ``codeBuildDefaults`` are applied
        :param synth_code_build_defaults: Additional customizations to apply to the synthesize CodeBuild projects. Default: - Only ``codeBuildDefaults`` are applied
        :param use_change_sets: Deploy every stack by creating a change set and executing it. When enabled, creates a "Prepare" and "Execute" action for each stack. Disable to deploy the stack in one pipeline action. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b4b4a0bcbd5fab3e4b78aa07ff9504469ae96c16799604ca3345bcb94480fc3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CodePipelineProps(
            synth=synth,
            artifact_bucket=artifact_bucket,
            asset_publishing_code_build_defaults=asset_publishing_code_build_defaults,
            cli_version=cli_version,
            code_build_defaults=code_build_defaults,
            code_pipeline=code_pipeline,
            cross_account_keys=cross_account_keys,
            cross_region_replication_buckets=cross_region_replication_buckets,
            docker_credentials=docker_credentials,
            docker_enabled_for_self_mutation=docker_enabled_for_self_mutation,
            docker_enabled_for_synth=docker_enabled_for_synth,
            enable_key_rotation=enable_key_rotation,
            pipeline_name=pipeline_name,
            publish_assets_in_parallel=publish_assets_in_parallel,
            reuse_cross_region_support_stacks=reuse_cross_region_support_stacks,
            role=role,
            self_mutation=self_mutation,
            self_mutation_code_build_defaults=self_mutation_code_build_defaults,
            synth_code_build_defaults=synth_code_build_defaults,
            use_change_sets=use_change_sets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="doBuildPipeline")
    def _do_build_pipeline(self) -> None:
        '''Implemented by subclasses to do the actual pipeline construction.'''
        return typing.cast(None, jsii.invoke(self, "doBuildPipeline", []))

    @builtins.property
    @jsii.member(jsii_name="pipeline")
    def pipeline(self) -> _Pipeline_ea38de84:
        '''The CodePipeline pipeline that deploys the CDK app.

        Only available after the pipeline has been built.
        '''
        return typing.cast(_Pipeline_ea38de84, jsii.get(self, "pipeline"))

    @builtins.property
    @jsii.member(jsii_name="selfMutationEnabled")
    def self_mutation_enabled(self) -> builtins.bool:
        '''Whether SelfMutation is enabled for this CDK Pipeline.'''
        return typing.cast(builtins.bool, jsii.get(self, "selfMutationEnabled"))

    @builtins.property
    @jsii.member(jsii_name="selfMutationProject")
    def self_mutation_project(self) -> _IProject_aafae30a:
        '''The CodeBuild project that performs the SelfMutation.

        Will throw an error if this is accessed before ``buildPipeline()``
        is called, or if selfMutation has been disabled.
        '''
        return typing.cast(_IProject_aafae30a, jsii.get(self, "selfMutationProject"))

    @builtins.property
    @jsii.member(jsii_name="synthProject")
    def synth_project(self) -> _IProject_aafae30a:
        '''The CodeBuild project that performs the Synth.

        Only available after the pipeline has been built.
        '''
        return typing.cast(_IProject_aafae30a, jsii.get(self, "synthProject"))


@jsii.implements(ICodePipelineActionFactory)
class CodePipelineSource(
    Step,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.pipelines.CodePipelineSource",
):
    '''Factory for CodePipeline source steps.

    This class contains a number of factory methods for the different types
    of sources that CodePipeline supports.

    :exampleMetadata: infused

    Example::

        # Access the CommitId of a GitHub source in the synth
        source = pipelines.CodePipelineSource.git_hub("owner/repo", "main")
        
        pipeline = pipelines.CodePipeline(scope, "MyPipeline",
            synth=pipelines.ShellStep("Synth",
                input=source,
                commands=[],
                env={
                    "COMMIT_ID": source.source_attribute("CommitId")
                }
            )
        )
    '''

    def __init__(self, id: builtins.str) -> None:
        '''
        :param id: Identifier for this step.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62608213b8ca550c4cb784e6cfaa384d1ded1aad493897b1e7801849d41151a4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [id])

    @jsii.member(jsii_name="codeCommit")
    @builtins.classmethod
    def code_commit(
        cls,
        repository: _IRepository_e7c062a1,
        branch: builtins.str,
        *,
        action_name: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        trigger: typing.Optional[_CodeCommitTrigger_e1096919] = None,
    ) -> "CodePipelineSource":
        '''Returns a CodeCommit source.

        If you need access to symlinks or the repository history, be sure to set
        ``codeBuildCloneOutput``.

        :param repository: The CodeCommit repository.
        :param branch: The branch to use.
        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository name
        :param code_build_clone_output: If this is set, the next CodeBuild job clones the repository (instead of CodePipeline downloading the files). This provides access to repository history, and retains symlinks (symlinks would otherwise be removed by CodePipeline). **Note**: if this option is true, only CodeBuild jobs can use the output artifact. Default: false
        :param event_role: Role to be used by on commit event rule. Used only when trigger value is CodeCommitTrigger.EVENTS. Default: a new role will be created.
        :param trigger: How should CodePipeline detect source changes for this Action. Default: CodeCommitTrigger.EVENTS

        Example::

            # repository: codecommit.IRepository
            
            pipelines.CodePipelineSource.code_commit(repository, "main")
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f25220d63f26c49b4c196a3d31d631ccf312fd1e469b49c9f423dda4bedc6d69)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        props = CodeCommitSourceOptions(
            action_name=action_name,
            code_build_clone_output=code_build_clone_output,
            event_role=event_role,
            trigger=trigger,
        )

        return typing.cast("CodePipelineSource", jsii.sinvoke(cls, "codeCommit", [repository, branch, props]))

    @jsii.member(jsii_name="connection")
    @builtins.classmethod
    def connection(
        cls,
        repo_string: builtins.str,
        branch: builtins.str,
        *,
        connection_arn: builtins.str,
        action_name: typing.Optional[builtins.str] = None,
        code_build_clone_output: typing.Optional[builtins.bool] = None,
        trigger_on_push: typing.Optional[builtins.bool] = None,
    ) -> "CodePipelineSource":
        '''Returns a CodeStar connection source.

        A CodeStar connection allows AWS CodePipeline to
        access external resources, such as repositories in GitHub, GitHub Enterprise or
        BitBucket.

        To use this method, you first need to create a CodeStar connection
        using the AWS console. In the process, you may have to sign in to the external provider
        -- GitHub, for example -- to authorize AWS to read and modify your repository.
        Once you have done this, copy the connection ARN and use it to create the source.

        Example::

           pipelines.CodePipelineSource.connection("owner/repo", "main",
               connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
           )

        If you need access to symlinks or the repository history, be sure to set
        ``codeBuildCloneOutput``.

        :param repo_string: A string that encodes owner and repository separated by a slash (e.g. 'owner/repo'). The provided string must be resolvable at runtime.
        :param branch: The branch to use.
        :param connection_arn: The ARN of the CodeStar Connection created in the AWS console that has permissions to access this GitHub or BitBucket repository.
        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository string
        :param code_build_clone_output: If this is set, the next CodeBuild job clones the repository (instead of CodePipeline downloading the files). This provides access to repository history, and retains symlinks (symlinks would otherwise be removed by CodePipeline). **Note**: if this option is true, only CodeBuild jobs can use the output artifact. Default: false
        :param trigger_on_push: Controls automatically starting your pipeline when a new commit is made on the configured repository and branch. If unspecified, the default value is true, and the field does not display by default. Default: true

        :see: https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61f9c81f3f2616f051720bd0c8209831bc0b7aa25f736b93cc369f3dfecac29c)
            check_type(argname="argument repo_string", value=repo_string, expected_type=type_hints["repo_string"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        props = ConnectionSourceOptions(
            connection_arn=connection_arn,
            action_name=action_name,
            code_build_clone_output=code_build_clone_output,
            trigger_on_push=trigger_on_push,
        )

        return typing.cast("CodePipelineSource", jsii.sinvoke(cls, "connection", [repo_string, branch, props]))

    @jsii.member(jsii_name="ecr")
    @builtins.classmethod
    def ecr(
        cls,
        repository: _IRepository_e6004aa6,
        *,
        action_name: typing.Optional[builtins.str] = None,
        image_tag: typing.Optional[builtins.str] = None,
    ) -> "CodePipelineSource":
        '''Returns an ECR source.

        :param repository: The repository that will be watched for changes.
        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository name
        :param image_tag: The image tag that will be checked for changes. Default: latest

        Example::

            # repository: ecr.IRepository
            
            pipelines.CodePipelineSource.ecr(repository,
                image_tag="latest"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b33e9fc6a0d43b73cabe2ee725c5ebddcca32e8eb1b382e1e11a96004696b07)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
        props = ECRSourceOptions(action_name=action_name, image_tag=image_tag)

        return typing.cast("CodePipelineSource", jsii.sinvoke(cls, "ecr", [repository, props]))

    @jsii.member(jsii_name="gitHub")
    @builtins.classmethod
    def git_hub(
        cls,
        repo_string: builtins.str,
        branch: builtins.str,
        *,
        action_name: typing.Optional[builtins.str] = None,
        authentication: typing.Optional[_SecretValue_3dd0ddae] = None,
        trigger: typing.Optional[_GitHubTrigger_0029a9bb] = None,
    ) -> "CodePipelineSource":
        '''Returns a GitHub source, using OAuth tokens to authenticate with GitHub and a separate webhook to detect changes.

        This is no longer
        the recommended method. Please consider using ``connection()``
        instead.

        Pass in the owner and repository in a single string, like this::

           pipelines.CodePipelineSource.git_hub("owner/repo", "main")

        Authentication will be done by a secret called ``github-token`` in AWS
        Secrets Manager (unless specified otherwise).

        If you rotate the value in the Secret, you must also change at least one property
        on the Pipeline, to force CloudFormation to re-read the secret.

        The token should have these permissions:

        - **repo** - to read the repository
        - **admin:repo_hook** - if you plan to use webhooks (true by default)

        If you need access to symlinks or the repository history, use a source of type
        ``connection`` instead.

        :param repo_string: -
        :param branch: -
        :param action_name: The action name used for this source in the CodePipeline. Default: - The repository string
        :param authentication: A GitHub OAuth token to use for authentication. It is recommended to use a Secrets Manager ``Secret`` to obtain the token:: const oauth = cdk.SecretValue.secretsManager('my-github-token'); The GitHub Personal Access Token should have these scopes: - **repo** - to read the repository - **admin:repo_hook** - if you plan to use webhooks (true by default) Default: - SecretValue.secretsManager('github-token')
        :param trigger: How AWS CodePipeline should be triggered. With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action. With "POLL", CodePipeline periodically checks the source for changes. With "None", the action is not triggered through changes in the source. To use ``WEBHOOK``, your GitHub Personal Access Token should have **admin:repo_hook** scope (in addition to the regular **repo** scope). Default: GitHubTrigger.WEBHOOK
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dd7ae717610cf37a89d099e605a91936a55ac698e5cf82446ff150258850c98)
            check_type(argname="argument repo_string", value=repo_string, expected_type=type_hints["repo_string"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        props = GitHubSourceOptions(
            action_name=action_name, authentication=authentication, trigger=trigger
        )

        return typing.cast("CodePipelineSource", jsii.sinvoke(cls, "gitHub", [repo_string, branch, props]))

    @jsii.member(jsii_name="s3")
    @builtins.classmethod
    def s3(
        cls,
        bucket: _IBucket_42e086fd,
        object_key: builtins.str,
        *,
        action_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        trigger: typing.Optional[_S3Trigger_3ab49ad8] = None,
    ) -> "CodePipelineSource":
        '''Returns an S3 source.

        :param bucket: The bucket where the source code is located.
        :param object_key: -
        :param action_name: The action name used for this source in the CodePipeline. Default: - The bucket name
        :param role: The role that will be assumed by the pipeline prior to executing the ``S3Source`` action. Default: - a new role will be generated
        :param trigger: How should CodePipeline detect source changes for this Action. Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail, as otherwise the CloudWatch Events will not be emitted. Default: S3Trigger.POLL

        Example::

            # bucket: s3.Bucket
            
            pipelines.CodePipelineSource.s3(bucket, "path/to/file.zip")
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e839aa405e65eab030730a9018a88432d9e7ec389336d4a4ba152a629311f25)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
        props = S3SourceOptions(action_name=action_name, role=role, trigger=trigger)

        return typing.cast("CodePipelineSource", jsii.sinvoke(cls, "s3", [bucket, object_key, props]))

    @jsii.member(jsii_name="getAction")
    @abc.abstractmethod
    def _get_action(
        self,
        output: _Artifact_0cb05964,
        action_name: builtins.str,
        run_order: jsii.Number,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> _Action_20e074ce:
        '''
        :param output: -
        :param action_name: -
        :param run_order: -
        :param variables_namespace: -
        '''
        ...

    @jsii.member(jsii_name="produceAction")
    def produce_action(
        self,
        stage: _IStage_415fc571,
        *,
        action_name: builtins.str,
        artifacts: ArtifactMap,
        pipeline: CodePipeline,
        run_order: jsii.Number,
        scope: _constructs_77d1e7e8.Construct,
        stack_outputs_map: StackOutputsMap,
        before_self_mutation: typing.Optional[builtins.bool] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> CodePipelineActionFactoryResult:
        '''Create the desired Action and add it to the pipeline.

        :param stage: -
        :param action_name: Name the action should get.
        :param artifacts: Helper object to translate FileSets to CodePipeline Artifacts.
        :param pipeline: The pipeline the action is being generated for.
        :param run_order: RunOrder the action should get.
        :param scope: Scope in which to create constructs.
        :param stack_outputs_map: Helper object to produce variables exported from stack deployments. If your step references outputs from a stack deployment, use this to map the output references to Codepipeline variable names. Note - Codepipeline variables can only be referenced in action configurations.
        :param before_self_mutation: Whether or not this action is inserted before self mutation. If it is, the action should take care to reflect some part of its own definition in the pipeline action definition, to trigger a restart after self-mutation (if necessary). Default: false
        :param code_build_defaults: If this action factory creates a CodeBuild step, default options to inherit. Default: - No CodeBuild project defaults
        :param fallback_artifact: An input artifact that CodeBuild projects that don't actually need an input artifact can use. CodeBuild Projects MUST have an input artifact in order to be added to the Pipeline. If the Project doesn't actually care about its input (it can be anything), it can use the Artifact passed here. Default: - A fallback artifact does not exist
        :param variables_namespace: If this step is producing outputs, the variables namespace assigned to it. Pass this on to the Action you are creating. Default: - Step doesn't produce any outputs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17abe85d134a8dfe23ca785d7db647ce27d0bfe5c838b2b3d423bad11ec9023f)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        options = ProduceActionOptions(
            action_name=action_name,
            artifacts=artifacts,
            pipeline=pipeline,
            run_order=run_order,
            scope=scope,
            stack_outputs_map=stack_outputs_map,
            before_self_mutation=before_self_mutation,
            code_build_defaults=code_build_defaults,
            fallback_artifact=fallback_artifact,
            variables_namespace=variables_namespace,
        )

        return typing.cast(CodePipelineActionFactoryResult, jsii.invoke(self, "produceAction", [stage, options]))

    @jsii.member(jsii_name="sourceAttribute")
    def source_attribute(self, name: builtins.str) -> builtins.str:
        '''Return an attribute of the current source revision.

        These values can be passed into the environment variables of pipeline steps,
        so your steps can access information about the source revision.

        Pipeline synth step has some source attributes predefined in the environment.
        If these suffice, you don't need to use this method for the synth step.

        :param name: -

        :see: https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-variables.html#reference-variables-list

        Example::

            # Access the CommitId of a GitHub source in the synth
            source = pipelines.CodePipelineSource.git_hub("owner/repo", "main")
            
            pipeline = pipelines.CodePipeline(scope, "MyPipeline",
                synth=pipelines.ShellStep("Synth",
                    input=source,
                    commands=[],
                    env={
                        "COMMIT_ID": source.source_attribute("CommitId")
                    }
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efac8cbc7f0ca706a3968547b0a9c6e6ca8f0902b5d725b8bd9e1de07841c50f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(builtins.str, jsii.invoke(self, "sourceAttribute", [name]))

    @builtins.property
    @jsii.member(jsii_name="isSource")
    def is_source(self) -> builtins.bool:
        '''Whether or not this is a Source step.

        What it means to be a Source step depends on the engine.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isSource"))


class _CodePipelineSourceProxy(
    CodePipelineSource,
    jsii.proxy_for(Step), # type: ignore[misc]
):
    @jsii.member(jsii_name="getAction")
    def _get_action(
        self,
        output: _Artifact_0cb05964,
        action_name: builtins.str,
        run_order: jsii.Number,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> _Action_20e074ce:
        '''
        :param output: -
        :param action_name: -
        :param run_order: -
        :param variables_namespace: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350aa368c32d7a50a5693f64b5349e88b87a9978b26c084eb53efe0c9997aac8)
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument run_order", value=run_order, expected_type=type_hints["run_order"])
            check_type(argname="argument variables_namespace", value=variables_namespace, expected_type=type_hints["variables_namespace"])
        return typing.cast(_Action_20e074ce, jsii.invoke(self, "getAction", [output, action_name, run_order, variables_namespace]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, CodePipelineSource).__jsii_proxy_class__ = lambda : _CodePipelineSourceProxy


@jsii.implements(ICodePipelineActionFactory)
class ConfirmPermissionsBroadening(
    Step,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.ConfirmPermissionsBroadening",
):
    '''Pause the pipeline if a deployment would add IAM permissions or Security Group rules.

    This step is only supported in CodePipeline pipelines.

    :exampleMetadata: infused

    Example::

        # pipeline: pipelines.CodePipeline
        
        stage = MyApplicationStage(self, "MyApplication")
        pipeline.add_stage(stage,
            pre=[
                pipelines.ConfirmPermissionsBroadening("Check", stage=stage)
            ]
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        stage: _Stage_7df8511b,
        notification_topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''
        :param id: Identifier for this step.
        :param stage: The CDK Stage object to check the stacks of. This should be the same Stage object you are passing to ``addStage()``.
        :param notification_topic: Topic to send notifications when a human needs to give manual confirmation. Default: - no notification
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f8758700f34f1f08997282e6c9eeb3ec7f0a892a166ab9cb89261bd2c3400e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PermissionsBroadeningCheckProps(
            stage=stage, notification_topic=notification_topic
        )

        jsii.create(self.__class__, self, [id, props])

    @jsii.member(jsii_name="produceAction")
    def produce_action(
        self,
        stage: _IStage_415fc571,
        *,
        action_name: builtins.str,
        artifacts: ArtifactMap,
        pipeline: CodePipeline,
        run_order: jsii.Number,
        scope: _constructs_77d1e7e8.Construct,
        stack_outputs_map: StackOutputsMap,
        before_self_mutation: typing.Optional[builtins.bool] = None,
        code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
        variables_namespace: typing.Optional[builtins.str] = None,
    ) -> CodePipelineActionFactoryResult:
        '''Create the desired Action and add it to the pipeline.

        :param stage: -
        :param action_name: Name the action should get.
        :param artifacts: Helper object to translate FileSets to CodePipeline Artifacts.
        :param pipeline: The pipeline the action is being generated for.
        :param run_order: RunOrder the action should get.
        :param scope: Scope in which to create constructs.
        :param stack_outputs_map: Helper object to produce variables exported from stack deployments. If your step references outputs from a stack deployment, use this to map the output references to Codepipeline variable names. Note - Codepipeline variables can only be referenced in action configurations.
        :param before_self_mutation: Whether or not this action is inserted before self mutation. If it is, the action should take care to reflect some part of its own definition in the pipeline action definition, to trigger a restart after self-mutation (if necessary). Default: false
        :param code_build_defaults: If this action factory creates a CodeBuild step, default options to inherit. Default: - No CodeBuild project defaults
        :param fallback_artifact: An input artifact that CodeBuild projects that don't actually need an input artifact can use. CodeBuild Projects MUST have an input artifact in order to be added to the Pipeline. If the Project doesn't actually care about its input (it can be anything), it can use the Artifact passed here. Default: - A fallback artifact does not exist
        :param variables_namespace: If this step is producing outputs, the variables namespace assigned to it. Pass this on to the Action you are creating. Default: - Step doesn't produce any outputs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa29dc3adc01937291bcdc656033c2cb644deb0651cba6f7b8de5f368bd482e0)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        options = ProduceActionOptions(
            action_name=action_name,
            artifacts=artifacts,
            pipeline=pipeline,
            run_order=run_order,
            scope=scope,
            stack_outputs_map=stack_outputs_map,
            before_self_mutation=before_self_mutation,
            code_build_defaults=code_build_defaults,
            fallback_artifact=fallback_artifact,
            variables_namespace=variables_namespace,
        )

        return typing.cast(CodePipelineActionFactoryResult, jsii.invoke(self, "produceAction", [stage, options]))


@jsii.implements(IFileSetProducer)
class FileSet(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.pipelines.FileSet"):
    '''A set of files traveling through the deployment pipeline.

    Individual steps in the pipeline produce or consume
    ``FileSet``s.

    :exampleMetadata: infused

    Example::

        @jsii.implements(pipelines.ICodePipelineActionFactory)
        class MyJenkinsStep(pipelines.Step):
            def __init__(self, provider, input):
                super().__init__("MyJenkinsStep")
        
                # This is necessary if your step accepts parameters, like environment variables,
                # that may contain outputs from other steps. It doesn't matter what the
                # structure is, as long as it contains the values that may contain outputs.
                self.discover_referenced_outputs({
                    "env": {}
                })
        
            def produce_action(self, stage, *, scope, actionName, runOrder, variablesNamespace=None, artifacts, fallbackArtifact=None, pipeline, codeBuildDefaults=None, beforeSelfMutation=None, stackOutputsMap):
        
                # This is where you control what type of Action gets added to the
                # CodePipeline
                stage.add_action(cpactions.JenkinsAction(
                    # Copy 'actionName' and 'runOrder' from the options
                    action_name=action_name,
                    run_order=run_order,
        
                    # Jenkins-specific configuration
                    type=cpactions.JenkinsActionType.TEST,
                    jenkins_provider=self.provider,
                    project_name="MyJenkinsProject",
        
                    # Translate the FileSet into a codepipeline.Artifact
                    inputs=[artifacts.to_code_pipeline(self.input)]
                ))
        
                return pipelines.CodePipelineActionFactoryResult(run_orders_consumed=1)
    '''

    def __init__(
        self,
        id: builtins.str,
        producer: typing.Optional[Step] = None,
    ) -> None:
        '''
        :param id: Human-readable descriptor for this file set (does not need to be unique).
        :param producer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fb5c48bf8a3ffb83c6da98bbcea632055bb6515645a2fb39340bc9cb6e03c09)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument producer", value=producer, expected_type=type_hints["producer"])
        jsii.create(self.__class__, self, [id, producer])

    @jsii.member(jsii_name="producedBy")
    def produced_by(self, producer: typing.Optional[Step] = None) -> None:
        '''Mark the given Step as the producer for this FileSet.

        This method can only be called once.

        :param producer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba363185b6eb39cdcda445644f226596b25b652ee4119d4eefa0d240136413d)
            check_type(argname="argument producer", value=producer, expected_type=type_hints["producer"])
        return typing.cast(None, jsii.invoke(self, "producedBy", [producer]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Return a string representation of this FileSet.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Human-readable descriptor for this file set (does not need to be unique).'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="producer")
    def producer(self) -> Step:
        '''The Step that produces this FileSet.'''
        return typing.cast(Step, jsii.get(self, "producer"))

    @builtins.property
    @jsii.member(jsii_name="primaryOutput")
    def primary_output(self) -> typing.Optional["FileSet"]:
        '''The primary output of a file set producer.

        The primary output of a FileSet is itself.
        '''
        return typing.cast(typing.Optional["FileSet"], jsii.get(self, "primaryOutput"))


class ManualApprovalStep(
    Step,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.ManualApprovalStep",
):
    '''A manual approval step.

    If this step is added to a Pipeline, the Pipeline will
    be paused waiting for a human to resume it

    Only engines that support pausing the deployment will
    support this step type.

    :exampleMetadata: infused

    Example::

        # pipeline: pipelines.CodePipeline
        
        preprod = MyApplicationStage(self, "PreProd")
        prod = MyApplicationStage(self, "Prod")
        
        pipeline.add_stage(preprod,
            post=[
                pipelines.ShellStep("Validate Endpoint",
                    commands=["curl -Ssf https://my.webservice.com/"]
                )
            ]
        )
        pipeline.add_stage(prod,
            pre=[
                pipelines.ManualApprovalStep("PromoteToProd")
            ]
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Identifier for this step.
        :param comment: The comment to display with this manual approval. Default: - No comment
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1bf3ac4525b2831190c490c38deb9452f7e662bb66f5cb63ba43cdac1db0dc4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ManualApprovalStepProps(comment=comment)

        jsii.create(self.__class__, self, [id, props])

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[builtins.str]:
        '''The comment associated with this manual approval.

        :default: - No comment
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comment"))


class ShellStep(
    Step,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.ShellStep",
):
    '''Run shell script commands in the pipeline.

    This is a generic step designed
    to be deployment engine agnostic.

    :exampleMetadata: infused

    Example::

        # Modern API
        modern_pipeline = pipelines.CodePipeline(self, "Pipeline",
            self_mutation=False,
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"
                ]
            )
        )
        
        # Original API
        cloud_assembly_artifact = codepipeline.Artifact()
        original_pipeline = pipelines.CdkPipeline(self, "Pipeline",
            self_mutating=False,
            cloud_assembly_artifact=cloud_assembly_artifact
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        commands: typing.Sequence[builtins.str],
        additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
        input: typing.Optional[IFileSetProducer] = None,
        install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary_output_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Identifier for this step.
        :param commands: Commands to run.
        :param additional_inputs: Additional FileSets to put in other directories. Specifies a mapping from directory name to FileSets. During the script execution, the FileSets will be available in the directories indicated. The directory names may be relative. For example, you can put the main input and an additional input side-by-side with the following configuration:: const script = new pipelines.ShellStep('MainScript', { commands: ['npm ci','npm run build','npx cdk synth'], input: pipelines.CodePipelineSource.gitHub('org/source1', 'main'), additionalInputs: { '../siblingdir': pipelines.CodePipelineSource.gitHub('org/source2', 'main'), } }); Default: - No additional inputs
        :param env: Environment variables to set. Default: - No environment variables
        :param env_from_cfn_outputs: Set environment variables based on Stack Outputs. ``ShellStep``s following stack or stage deployments may access the ``CfnOutput``s of those stacks to get access to --for example--automatically generated resource names or endpoint URLs. Default: - No environment variables created from stack outputs
        :param input: FileSet to run these scripts on. The files in the FileSet will be placed in the working directory when the script is executed. Use ``additionalInputs`` to download file sets to other directories as well. Default: - No input specified
        :param install_commands: Installation commands to run before the regular commands. For deployment engines that support it, install commands will be classified differently in the job history from the regular ``commands``. Default: - No installation commands
        :param primary_output_directory: The directory that will contain the primary output fileset. After running the script, the contents of the given directory will be treated as the primary output of this Step. Default: - No primary output
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a785abe4e7e83733166c7ba3cf01e6c6113101a74eff2d69d5881d6938c75525)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ShellStepProps(
            commands=commands,
            additional_inputs=additional_inputs,
            env=env,
            env_from_cfn_outputs=env_from_cfn_outputs,
            input=input,
            install_commands=install_commands,
            primary_output_directory=primary_output_directory,
        )

        jsii.create(self.__class__, self, [id, props])

    @jsii.member(jsii_name="addOutputDirectory")
    def add_output_directory(self, directory: builtins.str) -> FileSet:
        '''Add an additional output FileSet based on a directory.

        After running the script, the contents of the given directory
        will be exported as a ``FileSet``. Use the ``FileSet`` as the
        input to another step.

        Multiple calls with the exact same directory name string (not normalized)
        will return the same FileSet.

        :param directory: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd1965487f88c208c06b31eeb633d22b994394aedb266876224cba07f470f523)
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
        return typing.cast(FileSet, jsii.invoke(self, "addOutputDirectory", [directory]))

    @jsii.member(jsii_name="primaryOutputDirectory")
    def primary_output_directory(self, directory: builtins.str) -> FileSet:
        '''Configure the given output directory as primary output.

        If no primary output has been configured yet, this directory
        will become the primary output of this ShellStep, otherwise this
        method will throw if the given directory is different than the
        currently configured primary output directory.

        :param directory: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d5ab0590ee60f9eff918af46389650a105120da24b50f6951d4ec1c317dd5e4)
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
        return typing.cast(FileSet, jsii.invoke(self, "primaryOutputDirectory", [directory]))

    @builtins.property
    @jsii.member(jsii_name="commands")
    def commands(self) -> typing.List[builtins.str]:
        '''Commands to run.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "commands"))

    @builtins.property
    @jsii.member(jsii_name="consumedStackOutputs")
    def consumed_stack_outputs(self) -> typing.List[StackOutputReference]:
        '''StackOutputReferences this step consumes.'''
        return typing.cast(typing.List[StackOutputReference], jsii.get(self, "consumedStackOutputs"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Environment variables to set.

        :default: - No environment variables
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="envFromCfnOutputs")
    def env_from_cfn_outputs(
        self,
    ) -> typing.Mapping[builtins.str, StackOutputReference]:
        '''Set environment variables based on Stack Outputs.

        :default: - No environment variables created from stack outputs
        '''
        return typing.cast(typing.Mapping[builtins.str, StackOutputReference], jsii.get(self, "envFromCfnOutputs"))

    @builtins.property
    @jsii.member(jsii_name="inputs")
    def inputs(self) -> typing.List[FileSetLocation]:
        '''Input FileSets.

        A list of ``(FileSet, directory)`` pairs, which are a copy of the
        input properties. This list should not be modified directly.
        '''
        return typing.cast(typing.List[FileSetLocation], jsii.get(self, "inputs"))

    @builtins.property
    @jsii.member(jsii_name="installCommands")
    def install_commands(self) -> typing.List[builtins.str]:
        '''Installation commands to run before the regular commands.

        For deployment engines that support it, install commands will be classified
        differently in the job history from the regular ``commands``.

        :default: - No installation commands
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "installCommands"))

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(self) -> typing.List[FileSetLocation]:
        '''Output FileSets.

        A list of ``(FileSet, directory)`` pairs, which are a copy of the
        input properties. This list should not be modified directly.
        '''
        return typing.cast(typing.List[FileSetLocation], jsii.get(self, "outputs"))


class CodeBuildStep(
    ShellStep,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.CodeBuildStep",
):
    '''Run a script as a CodeBuild Project.

    The BuildSpec must be available inline--it cannot reference a file
    on disk. If your current build instructions are in a file like
    ``buildspec.yml`` in your repository, extract them to a script
    (say, ``build.sh``) and invoke that script as part of the build::

       pipelines.CodeBuildStep("Synth",
           commands=["./build.sh"]
       )

    :exampleMetadata: infused

    Example::

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineSource.connection("my-org/my-app", "main",
                    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41"
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"]
            ),
        
            # Turn this on because the pipeline uses Docker image assets
            docker_enabled_for_self_mutation=True
        )
        
        pipeline.add_wave("MyWave",
            post=[
                pipelines.CodeBuildStep("RunApproval",
                    commands=["command-from-image"],
                    build_environment=codebuild.BuildEnvironment(
                        # The user of a Docker image asset in the pipeline requires turning on
                        # 'dockerEnabledForSelfMutation'.
                        build_image=codebuild.LinuxBuildImage.from_asset(self, "Image",
                            directory="./docker-image"
                        )
                    )
                )
            ]
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        action_role: typing.Optional[_IRole_235f5d8e] = None,
        build_environment: typing.Optional[typing.Union[_BuildEnvironment_4ee6fb51, typing.Dict[builtins.str, typing.Any]]] = None,
        cache: typing.Optional[_Cache_ed12d453] = None,
        file_system_locations: typing.Optional[typing.Sequence[_IFileSystemLocation_acb87263]] = None,
        logging: typing.Optional[typing.Union[_LoggingOptions_31668710, typing.Dict[builtins.str, typing.Any]]] = None,
        partial_build_spec: typing.Optional[_BuildSpec_4961ea5b] = None,
        project_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        role_policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        commands: typing.Sequence[builtins.str],
        additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
        input: typing.Optional[IFileSetProducer] = None,
        install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary_output_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Identifier for this step.
        :param action_role: Custom execution role to be used for the Code Build Action. Default: - A role is automatically created
        :param build_environment: Changes to environment. This environment will be combined with the pipeline's default environment. Default: - Use the pipeline's default build environment
        :param cache: Caching strategy to use. Default: - No cache
        :param file_system_locations: ProjectFileSystemLocation objects for CodeBuild build projects. A ProjectFileSystemLocation object specifies the identifier, location, mountOptions, mountPoint, and type of a file system created using Amazon Elastic File System. Default: - no file system locations
        :param logging: Information about logs for CodeBuild projects. A CodeBuild project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both. Default: - no log configuration is set
        :param partial_build_spec: Additional configuration that can only be configured via BuildSpec. You should not use this to specify output artifacts; those should be supplied via the other properties of this class, otherwise CDK Pipelines won't be able to inspect the artifacts. Set the ``commands`` to an empty array if you want to fully specify the BuildSpec using this field. The BuildSpec must be available inline--it cannot reference a file on disk. Default: - BuildSpec completely derived from other properties
        :param project_name: Name for the generated CodeBuild project. Default: - Automatically generated
        :param role: Custom execution role to be used for the CodeBuild project. Default: - A role is automatically created
        :param role_policy_statements: Policy statements to add to role used during the synth. Can be used to add acces to a CodeArtifact repository etc. Default: - No policy statements added to CodeBuild Project Role
        :param security_groups: Which security group to associate with the script's project network interfaces. If no security group is identified, one will be created automatically. Only used if 'vpc' is supplied. Default: - Security group will be automatically created.
        :param subnet_selection: Which subnets to use. Only used if 'vpc' is supplied. Default: - All private subnets.
        :param timeout: The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: The VPC where to execute the SimpleSynth. Default: - No VPC
        :param commands: Commands to run.
        :param additional_inputs: Additional FileSets to put in other directories. Specifies a mapping from directory name to FileSets. During the script execution, the FileSets will be available in the directories indicated. The directory names may be relative. For example, you can put the main input and an additional input side-by-side with the following configuration:: const script = new pipelines.ShellStep('MainScript', { commands: ['npm ci','npm run build','npx cdk synth'], input: pipelines.CodePipelineSource.gitHub('org/source1', 'main'), additionalInputs: { '../siblingdir': pipelines.CodePipelineSource.gitHub('org/source2', 'main'), } }); Default: - No additional inputs
        :param env: Environment variables to set. Default: - No environment variables
        :param env_from_cfn_outputs: Set environment variables based on Stack Outputs. ``ShellStep``s following stack or stage deployments may access the ``CfnOutput``s of those stacks to get access to --for example--automatically generated resource names or endpoint URLs. Default: - No environment variables created from stack outputs
        :param input: FileSet to run these scripts on. The files in the FileSet will be placed in the working directory when the script is executed. Use ``additionalInputs`` to download file sets to other directories as well. Default: - No input specified
        :param install_commands: Installation commands to run before the regular commands. For deployment engines that support it, install commands will be classified differently in the job history from the regular ``commands``. Default: - No installation commands
        :param primary_output_directory: The directory that will contain the primary output fileset. After running the script, the contents of the given directory will be treated as the primary output of this Step. Default: - No primary output
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f99ccfa38ab852946e7a199c4d87afa67da2d007eac373a7c3b7028da4fca8ff)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CodeBuildStepProps(
            action_role=action_role,
            build_environment=build_environment,
            cache=cache,
            file_system_locations=file_system_locations,
            logging=logging,
            partial_build_spec=partial_build_spec,
            project_name=project_name,
            role=role,
            role_policy_statements=role_policy_statements,
            security_groups=security_groups,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
            commands=commands,
            additional_inputs=additional_inputs,
            env=env,
            env_from_cfn_outputs=env_from_cfn_outputs,
            input=input,
            install_commands=install_commands,
            primary_output_directory=primary_output_directory,
        )

        jsii.create(self.__class__, self, [id, props])

    @jsii.member(jsii_name="exportedVariable")
    def exported_variable(self, variable_name: builtins.str) -> builtins.str:
        '''Reference a CodePipeline variable defined by the CodeBuildStep.

        The variable must be set in the shell of the CodeBuild step when
        it finishes its ``post_build`` phase.

        :param variable_name: the name of the variable for reference.

        Example::

            # Access the output of one CodeBuildStep in another CodeBuildStep
            # pipeline: pipelines.CodePipeline
            
            
            step1 = pipelines.CodeBuildStep("Step1",
                commands=["export MY_VAR=hello"]
            )
            
            step2 = pipelines.CodeBuildStep("Step2",
                env={
                    "IMPORTED_VAR": step1.exported_variable("MY_VAR")
                },
                commands=["echo $IMPORTED_VAR"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba510e4eda683498de32392bbad670fabf1cbc35027297fd070669464ed607cd)
            check_type(argname="argument variable_name", value=variable_name, expected_type=type_hints["variable_name"])
        return typing.cast(builtins.str, jsii.invoke(self, "exportedVariable", [variable_name]))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The CodeBuild Project's principal.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> _IProject_aafae30a:
        '''CodeBuild Project generated for the pipeline.

        Will only be available after the pipeline has been built.
        '''
        return typing.cast(_IProject_aafae30a, jsii.get(self, "project"))

    @builtins.property
    @jsii.member(jsii_name="actionRole")
    def action_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Custom execution role to be used for the Code Build Action.

        :default: - A role is automatically created
        '''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "actionRole"))

    @builtins.property
    @jsii.member(jsii_name="buildEnvironment")
    def build_environment(self) -> typing.Optional[_BuildEnvironment_4ee6fb51]:
        '''Build environment.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[_BuildEnvironment_4ee6fb51], jsii.get(self, "buildEnvironment"))

    @builtins.property
    @jsii.member(jsii_name="cache")
    def cache(self) -> typing.Optional[_Cache_ed12d453]:
        '''Caching strategy to use.

        :default: - No cache
        '''
        return typing.cast(typing.Optional[_Cache_ed12d453], jsii.get(self, "cache"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLocations")
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.List[_IFileSystemLocation_acb87263]]:
        '''ProjectFileSystemLocation objects for CodeBuild build projects.

        A ProjectFileSystemLocation object specifies the identifier, location, mountOptions, mountPoint,
        and type of a file system created using Amazon Elastic File System.

        :default: - no file system locations
        '''
        return typing.cast(typing.Optional[typing.List[_IFileSystemLocation_acb87263]], jsii.get(self, "fileSystemLocations"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> typing.Optional[_LoggingOptions_31668710]:
        '''Information about logs for CodeBuild projects.

        A CodeBuilde project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both.

        :default: - no log configuration is set
        '''
        return typing.cast(typing.Optional[_LoggingOptions_31668710], jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="partialBuildSpec")
    def partial_build_spec(self) -> typing.Optional[_BuildSpec_4961ea5b]:
        '''Additional configuration that can only be configured via BuildSpec.

        Contains exported variables

        :default: - Contains the exported variables
        '''
        return typing.cast(typing.Optional[_BuildSpec_4961ea5b], jsii.get(self, "partialBuildSpec"))

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> typing.Optional[builtins.str]:
        '''Name for the generated CodeBuild project.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Custom execution role to be used for the CodeBuild project.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="rolePolicyStatements")
    def role_policy_statements(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Policy statements to add to role used during the synth.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], jsii.get(self, "rolePolicyStatements"))

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''Which security group to associate with the script's project network interfaces.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], jsii.get(self, "securityGroups"))

    @builtins.property
    @jsii.member(jsii_name="subnetSelection")
    def subnet_selection(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Which subnets to use.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], jsii.get(self, "subnetSelection"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)
        '''
        return typing.cast(typing.Optional[_Duration_4839e8c3], jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The VPC where to execute the SimpleSynth.

        :default: - No value specified at construction time, use defaults
        '''
        return typing.cast(typing.Optional[_IVpc_f30d5663], jsii.get(self, "vpc"))


class CodePipelineFileSet(
    FileSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.pipelines.CodePipelineFileSet",
):
    '''A FileSet created from a CodePipeline artifact.

    You only need to use this if you want to add CDK Pipeline stages
    add the end of an existing CodePipeline, which should be very rare.

    :exampleMetadata: infused

    Example::

        # code_pipeline: codepipeline.Pipeline
        
        
        source_artifact = codepipeline.Artifact("MySourceArtifact")
        
        pipeline = pipelines.CodePipeline(self, "Pipeline",
            code_pipeline=code_pipeline,
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineFileSet.from_artifact(source_artifact),
                commands=["npm ci", "npm run build", "npx cdk synth"]
            )
        )
    '''

    @jsii.member(jsii_name="fromArtifact")
    @builtins.classmethod
    def from_artifact(cls, artifact: _Artifact_0cb05964) -> "CodePipelineFileSet":
        '''Turn a CodePipeline Artifact into a FileSet.

        :param artifact: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4050a951f11df379d3f03171015f338d23cc9145a854d86f45352dbc03d023f)
            check_type(argname="argument artifact", value=artifact, expected_type=type_hints["artifact"])
        return typing.cast("CodePipelineFileSet", jsii.sinvoke(cls, "fromArtifact", [artifact]))


__all__ = [
    "AddStageOpts",
    "ArtifactMap",
    "AssetType",
    "CodeBuildOptions",
    "CodeBuildStep",
    "CodeBuildStepProps",
    "CodeCommitSourceOptions",
    "CodePipeline",
    "CodePipelineActionFactoryResult",
    "CodePipelineFileSet",
    "CodePipelineProps",
    "CodePipelineSource",
    "ConfirmPermissionsBroadening",
    "ConnectionSourceOptions",
    "DockerCredential",
    "DockerCredentialUsage",
    "ECRSourceOptions",
    "EcrDockerCredentialOptions",
    "ExternalDockerCredentialOptions",
    "FileSet",
    "FileSetLocation",
    "GitHubSourceOptions",
    "ICodePipelineActionFactory",
    "IFileSetProducer",
    "ManualApprovalStep",
    "ManualApprovalStepProps",
    "PermissionsBroadeningCheckProps",
    "PipelineBase",
    "PipelineBaseProps",
    "ProduceActionOptions",
    "S3SourceOptions",
    "ShellStep",
    "ShellStepProps",
    "StackAsset",
    "StackDeployment",
    "StackDeploymentProps",
    "StackOutputReference",
    "StackOutputsMap",
    "StackSteps",
    "StageDeployment",
    "StageDeploymentProps",
    "Step",
    "Wave",
    "WaveOptions",
    "WaveProps",
]

publication.publish()

def _typecheckingstub__1b9c1bc74292ecb27724ef07a41dc8f1b1ee5d9dc268940f2ec578982b596b0a(
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
    stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25e392fc366b5e854a4d6ec5bf897ab0e51d041c4eae3089a12ab36474918e1(
    x: FileSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb14d0bc2bb7087520a3769dfb10a8c874fa4227208104c933f686486beec01c(
    *,
    build_environment: typing.Optional[typing.Union[_BuildEnvironment_4ee6fb51, typing.Dict[builtins.str, typing.Any]]] = None,
    cache: typing.Optional[_Cache_ed12d453] = None,
    file_system_locations: typing.Optional[typing.Sequence[_IFileSystemLocation_acb87263]] = None,
    logging: typing.Optional[typing.Union[_LoggingOptions_31668710, typing.Dict[builtins.str, typing.Any]]] = None,
    partial_build_spec: typing.Optional[_BuildSpec_4961ea5b] = None,
    role_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e17ff0fc6dc5e2614664c26c6bd947f6c7d12e7871a3cb4f169cdb8abc431ab0(
    *,
    action_name: typing.Optional[builtins.str] = None,
    code_build_clone_output: typing.Optional[builtins.bool] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    trigger: typing.Optional[_CodeCommitTrigger_e1096919] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9624d5022538eedc98a469f78de5916fac4ee13ff0d2f5f9a5e9d447ce9f909f(
    *,
    run_orders_consumed: jsii.Number,
    project: typing.Optional[_IProject_aafae30a] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46bc21ca63efb27c935c31017ebbc8c85b3b93ae1798e54892dd3eae41d99aa(
    *,
    synth: IFileSetProducer,
    artifact_bucket: typing.Optional[_IBucket_42e086fd] = None,
    asset_publishing_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cli_version: typing.Optional[builtins.str] = None,
    code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    code_pipeline: typing.Optional[_Pipeline_ea38de84] = None,
    cross_account_keys: typing.Optional[builtins.bool] = None,
    cross_region_replication_buckets: typing.Optional[typing.Mapping[builtins.str, _IBucket_42e086fd]] = None,
    docker_credentials: typing.Optional[typing.Sequence[DockerCredential]] = None,
    docker_enabled_for_self_mutation: typing.Optional[builtins.bool] = None,
    docker_enabled_for_synth: typing.Optional[builtins.bool] = None,
    enable_key_rotation: typing.Optional[builtins.bool] = None,
    pipeline_name: typing.Optional[builtins.str] = None,
    publish_assets_in_parallel: typing.Optional[builtins.bool] = None,
    reuse_cross_region_support_stacks: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    self_mutation: typing.Optional[builtins.bool] = None,
    self_mutation_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    synth_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    use_change_sets: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14ea58b20f21cf64b1c4567507d80ce40ed1cdc8e5831d98bd00ec1322a9ab5(
    *,
    connection_arn: builtins.str,
    action_name: typing.Optional[builtins.str] = None,
    code_build_clone_output: typing.Optional[builtins.bool] = None,
    trigger_on_push: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4796d36763a8311889ba388377df25c49f4d460f74af5013bbfd7374dadc940(
    usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c646af2493265594a1cf787d9e1152d57f57cc81c6c36614a8c7b6cd36d441(
    registry_domain: builtins.str,
    secret: _ISecret_6e020e6a,
    *,
    assume_role: typing.Optional[_IRole_235f5d8e] = None,
    secret_password_field: typing.Optional[builtins.str] = None,
    secret_username_field: typing.Optional[builtins.str] = None,
    usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e01732750f5b98b4a7cb4b141a1ef2d0c5e2042c8754d0cb0f829f0a2219577(
    secret: _ISecret_6e020e6a,
    *,
    assume_role: typing.Optional[_IRole_235f5d8e] = None,
    secret_password_field: typing.Optional[builtins.str] = None,
    secret_username_field: typing.Optional[builtins.str] = None,
    usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44075e2f8f9f423076a4b55e04677bdcd7ac2a9a1018ab4dc8116173bd7e1cf5(
    repositories: typing.Sequence[_IRepository_e6004aa6],
    *,
    assume_role: typing.Optional[_IRole_235f5d8e] = None,
    usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__554247a15294fead54d7e6a1adaddf130cd8f655b45d31098bee6ef197e7f6b6(
    grantee: _IGrantable_71c4f5de,
    usage: DockerCredentialUsage,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833a04c7f2e7f664e66a7534f73736d4c5911188c503aaf662baf8c6f39cf208(
    *,
    action_name: typing.Optional[builtins.str] = None,
    image_tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b8aaeef2e17487ef54d1992c6a3a7e2349b4c4a5d93c775a043f2db02c5287(
    *,
    assume_role: typing.Optional[_IRole_235f5d8e] = None,
    usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c359b9b78870cd0768aec95eba517b31efce3c0139487e9574671e537d4d9c8a(
    *,
    assume_role: typing.Optional[_IRole_235f5d8e] = None,
    secret_password_field: typing.Optional[builtins.str] = None,
    secret_username_field: typing.Optional[builtins.str] = None,
    usages: typing.Optional[typing.Sequence[DockerCredentialUsage]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cf7e83b5d5ed6c40f4a63f11e08a6255275802428d4153f786e83b3477442f2(
    *,
    directory: builtins.str,
    file_set: FileSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92035a41f512b5c8f05e89aaf8eff67c15b38e88a96495de7594813674d59c85(
    *,
    action_name: typing.Optional[builtins.str] = None,
    authentication: typing.Optional[_SecretValue_3dd0ddae] = None,
    trigger: typing.Optional[_GitHubTrigger_0029a9bb] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99773084b7df122e2f7df8455d5966ec674016081ec53bbdb52b9a758a61641f(
    stage: _IStage_415fc571,
    *,
    action_name: builtins.str,
    artifacts: ArtifactMap,
    pipeline: CodePipeline,
    run_order: jsii.Number,
    scope: _constructs_77d1e7e8.Construct,
    stack_outputs_map: StackOutputsMap,
    before_self_mutation: typing.Optional[builtins.bool] = None,
    code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0a42f985a6aa39b8db8606833d899bd8c93567a96ac5acb2c9407bde8793ed(
    *,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a493d3747f3c71b362bc21e20cdcb176192a8ddabde715a88ac4943a53a03e8(
    *,
    stage: _Stage_7df8511b,
    notification_topic: typing.Optional[_ITopic_9eca4852] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d184a64a4ab9776e0cde448a4015acadcea743c3fc3b48f622df0afb4024c6e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    synth: IFileSetProducer,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f67cf9a317d65ff87cbc38b2a72ad26c2ee3899fb8a0b5068ccdc87b2c46b2da(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cfb2052bce20c2fa202ea358095de4d8c0da42de12b0481096f461291c33ee4(
    stage: _Stage_7df8511b,
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
    stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad54c6253f19ba3a870e05ab1a3c0f4069394612e1bb5e45764182211f8ce8f(
    id: builtins.str,
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79842ef214ef2802f8ca77d0d6f69188566d39e1953e2067e21825205ad4e2d0(
    *,
    synth: IFileSetProducer,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93aef9a478cf51d0a19344db9575ea0a8f1c4048021aae6ecbd679f0230708cb(
    *,
    action_name: builtins.str,
    artifacts: ArtifactMap,
    pipeline: CodePipeline,
    run_order: jsii.Number,
    scope: _constructs_77d1e7e8.Construct,
    stack_outputs_map: StackOutputsMap,
    before_self_mutation: typing.Optional[builtins.bool] = None,
    code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cae2e2afdaad184f628a943e938bcc586f2ec9060bde2ab497f96efaf7c265a7(
    *,
    action_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    trigger: typing.Optional[_S3Trigger_3ab49ad8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__672600085b4c1f54d7e497f605a0be2945f1a2759aaf8632197707da6d73a55c(
    *,
    commands: typing.Sequence[builtins.str],
    additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
    input: typing.Optional[IFileSetProducer] = None,
    install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary_output_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b53846c07332af34759787d6881e8bb143a9ccedff4818aa7909126839e2a09(
    *,
    asset_id: builtins.str,
    asset_manifest_path: builtins.str,
    asset_selector: builtins.str,
    asset_type: AssetType,
    is_template: builtins.bool,
    asset_publishing_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e4b846e8d3dadc7378b689c2dab6fb92e7f2100aef448009c9ec434fe88e2e(
    stack_artifact: _CloudFormationStackArtifact_97533dc8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ba0ab32a6826cbb7060a998d3ac3da2d06cd442d144b5ecf691e35278bb3a0(
    stack_deployment: StackDeployment,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee2fbbf15668f466092e120cac329bba8450a234aeb44ff69f7e6d6118482210(
    pre: typing.Sequence[Step],
    change_set: typing.Sequence[Step],
    post: typing.Sequence[Step],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee959d9efa16dfdb6813c606cf8d87ccf20db0aa7716242deca0a8be262c6f75(
    *,
    absolute_template_path: builtins.str,
    construct_path: builtins.str,
    stack_artifact_id: builtins.str,
    stack_name: builtins.str,
    account: typing.Optional[builtins.str] = None,
    assets: typing.Optional[typing.Sequence[typing.Union[StackAsset, typing.Dict[builtins.str, typing.Any]]]] = None,
    assume_role_arn: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8745bc64df0b3aa6e7dfd1168c6139f2c024dac1d882f0d4af23b942b5ec34(
    output: _CfnOutput_7273f911,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b335ec5f93b8ed0338c0e4961948e8606ff0d3b66288aad78ffdd955b373584c(
    stack: StackDeployment,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50e71bc676eac9027f6ea818ba4d747ff0c565ffd3d254888a264b4c946d9bc(
    pipeline: PipelineBase,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6208cae78a5089ece754de6bca07ee8e0f93d368525e449cb62ab9aa02d5387d(
    x: StackOutputReference,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca5d40f3edb2136fa92aadc52d7d0d639af5efa3c3907aa21900a78546472e9(
    *,
    stack: _Stack_2866e57f,
    change_set: typing.Optional[typing.Sequence[Step]] = None,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37efd4695086f03c4f48796707d94ae7caf71cecf52f15940e3a454ddce14cf(
    stage: _Stage_7df8511b,
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
    stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
    stage_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7963424ad1d642071b0d2ad14e4d5fc16fe9da5684fa99810d45cdd45456ff78(
    *steps: Step,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b5cab7f97e36643320ecd39f081f32d2abc1c31b1aaf8ce2dc42ca0656bd163(
    *steps: Step,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2996b2e68f1aa0af80a6355038a15e330c41d048b4db733659fb5dacf94c7fad(
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
    stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
    stage_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68aaec030807cfbf351299f9c26e438985ce3f9e77a2ce6ee7cd9160ecaef59f(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa8ee52263a2c85e05e23d26dc40cc78dfc1127b9b95c510f018a6cfed478c6(
    steps: typing.Sequence[Step],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3c0f82c71c42c1f93221292b7dbffbe572c7ea5a260f598cb89a5fa77db6f9(
    fs: FileSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f54be98abfd0174d463663607bb14370b7402ee77874895f6bfed4c698e909(
    step: Step,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a068aee785ec3c9e9f1809d52708b5df8f13355aa9740ec37f0a9ee74e1110d4(
    fs: FileSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__861dc4a9082e25f4892e3dc0b3e109591bed56d6d69e131b65606d9ce139cfc4(
    structure: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19399be49c5895136165e92f8d4f261ada55bda465bbe03748a50eeb2565059(
    id: builtins.str,
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8581b4bbbe78eda4fb8dbcb1f3b771c7cf048db7cf5a72e03d64f96e57598299(
    *steps: Step,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66516b0f8ad368fac42e7dcdd790b28e1dfb19cb9b17305cf356abd5a2b9849a(
    *steps: Step,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7590cd60f1f21f8e0847610459550f1b62de25d7e9041a32e959d55e075a7f62(
    stage: _Stage_7df8511b,
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
    stack_steps: typing.Optional[typing.Sequence[typing.Union[StackSteps, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2277271dc82c44ce8955ce65457db799bd6e52de92bcc11a17652ce9c46ab6a(
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04297c0a279df0deb627a2db37c6345071a7dbd35ce5f96fbe3b3e08dacfc8a6(
    *,
    post: typing.Optional[typing.Sequence[Step]] = None,
    pre: typing.Optional[typing.Sequence[Step]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ea003fb723e489b2aa741146d04bb6e1e31bf776d6e79aadf14deb5a715643(
    *,
    commands: typing.Sequence[builtins.str],
    additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
    input: typing.Optional[IFileSetProducer] = None,
    install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary_output_directory: typing.Optional[builtins.str] = None,
    action_role: typing.Optional[_IRole_235f5d8e] = None,
    build_environment: typing.Optional[typing.Union[_BuildEnvironment_4ee6fb51, typing.Dict[builtins.str, typing.Any]]] = None,
    cache: typing.Optional[_Cache_ed12d453] = None,
    file_system_locations: typing.Optional[typing.Sequence[_IFileSystemLocation_acb87263]] = None,
    logging: typing.Optional[typing.Union[_LoggingOptions_31668710, typing.Dict[builtins.str, typing.Any]]] = None,
    partial_build_spec: typing.Optional[_BuildSpec_4961ea5b] = None,
    project_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    role_policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b4b4a0bcbd5fab3e4b78aa07ff9504469ae96c16799604ca3345bcb94480fc3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    synth: IFileSetProducer,
    artifact_bucket: typing.Optional[_IBucket_42e086fd] = None,
    asset_publishing_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cli_version: typing.Optional[builtins.str] = None,
    code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    code_pipeline: typing.Optional[_Pipeline_ea38de84] = None,
    cross_account_keys: typing.Optional[builtins.bool] = None,
    cross_region_replication_buckets: typing.Optional[typing.Mapping[builtins.str, _IBucket_42e086fd]] = None,
    docker_credentials: typing.Optional[typing.Sequence[DockerCredential]] = None,
    docker_enabled_for_self_mutation: typing.Optional[builtins.bool] = None,
    docker_enabled_for_synth: typing.Optional[builtins.bool] = None,
    enable_key_rotation: typing.Optional[builtins.bool] = None,
    pipeline_name: typing.Optional[builtins.str] = None,
    publish_assets_in_parallel: typing.Optional[builtins.bool] = None,
    reuse_cross_region_support_stacks: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    self_mutation: typing.Optional[builtins.bool] = None,
    self_mutation_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    synth_code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    use_change_sets: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62608213b8ca550c4cb784e6cfaa384d1ded1aad493897b1e7801849d41151a4(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25220d63f26c49b4c196a3d31d631ccf312fd1e469b49c9f423dda4bedc6d69(
    repository: _IRepository_e7c062a1,
    branch: builtins.str,
    *,
    action_name: typing.Optional[builtins.str] = None,
    code_build_clone_output: typing.Optional[builtins.bool] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    trigger: typing.Optional[_CodeCommitTrigger_e1096919] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f9c81f3f2616f051720bd0c8209831bc0b7aa25f736b93cc369f3dfecac29c(
    repo_string: builtins.str,
    branch: builtins.str,
    *,
    connection_arn: builtins.str,
    action_name: typing.Optional[builtins.str] = None,
    code_build_clone_output: typing.Optional[builtins.bool] = None,
    trigger_on_push: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b33e9fc6a0d43b73cabe2ee725c5ebddcca32e8eb1b382e1e11a96004696b07(
    repository: _IRepository_e6004aa6,
    *,
    action_name: typing.Optional[builtins.str] = None,
    image_tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd7ae717610cf37a89d099e605a91936a55ac698e5cf82446ff150258850c98(
    repo_string: builtins.str,
    branch: builtins.str,
    *,
    action_name: typing.Optional[builtins.str] = None,
    authentication: typing.Optional[_SecretValue_3dd0ddae] = None,
    trigger: typing.Optional[_GitHubTrigger_0029a9bb] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e839aa405e65eab030730a9018a88432d9e7ec389336d4a4ba152a629311f25(
    bucket: _IBucket_42e086fd,
    object_key: builtins.str,
    *,
    action_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    trigger: typing.Optional[_S3Trigger_3ab49ad8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17abe85d134a8dfe23ca785d7db647ce27d0bfe5c838b2b3d423bad11ec9023f(
    stage: _IStage_415fc571,
    *,
    action_name: builtins.str,
    artifacts: ArtifactMap,
    pipeline: CodePipeline,
    run_order: jsii.Number,
    scope: _constructs_77d1e7e8.Construct,
    stack_outputs_map: StackOutputsMap,
    before_self_mutation: typing.Optional[builtins.bool] = None,
    code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efac8cbc7f0ca706a3968547b0a9c6e6ca8f0902b5d725b8bd9e1de07841c50f(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350aa368c32d7a50a5693f64b5349e88b87a9978b26c084eb53efe0c9997aac8(
    output: _Artifact_0cb05964,
    action_name: builtins.str,
    run_order: jsii.Number,
    variables_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f8758700f34f1f08997282e6c9eeb3ec7f0a892a166ab9cb89261bd2c3400e(
    id: builtins.str,
    *,
    stage: _Stage_7df8511b,
    notification_topic: typing.Optional[_ITopic_9eca4852] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa29dc3adc01937291bcdc656033c2cb644deb0651cba6f7b8de5f368bd482e0(
    stage: _IStage_415fc571,
    *,
    action_name: builtins.str,
    artifacts: ArtifactMap,
    pipeline: CodePipeline,
    run_order: jsii.Number,
    scope: _constructs_77d1e7e8.Construct,
    stack_outputs_map: StackOutputsMap,
    before_self_mutation: typing.Optional[builtins.bool] = None,
    code_build_defaults: typing.Optional[typing.Union[CodeBuildOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    fallback_artifact: typing.Optional[_Artifact_0cb05964] = None,
    variables_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fb5c48bf8a3ffb83c6da98bbcea632055bb6515645a2fb39340bc9cb6e03c09(
    id: builtins.str,
    producer: typing.Optional[Step] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba363185b6eb39cdcda445644f226596b25b652ee4119d4eefa0d240136413d(
    producer: typing.Optional[Step] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1bf3ac4525b2831190c490c38deb9452f7e662bb66f5cb63ba43cdac1db0dc4(
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a785abe4e7e83733166c7ba3cf01e6c6113101a74eff2d69d5881d6938c75525(
    id: builtins.str,
    *,
    commands: typing.Sequence[builtins.str],
    additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
    input: typing.Optional[IFileSetProducer] = None,
    install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary_output_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd1965487f88c208c06b31eeb633d22b994394aedb266876224cba07f470f523(
    directory: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d5ab0590ee60f9eff918af46389650a105120da24b50f6951d4ec1c317dd5e4(
    directory: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99ccfa38ab852946e7a199c4d87afa67da2d007eac373a7c3b7028da4fca8ff(
    id: builtins.str,
    *,
    action_role: typing.Optional[_IRole_235f5d8e] = None,
    build_environment: typing.Optional[typing.Union[_BuildEnvironment_4ee6fb51, typing.Dict[builtins.str, typing.Any]]] = None,
    cache: typing.Optional[_Cache_ed12d453] = None,
    file_system_locations: typing.Optional[typing.Sequence[_IFileSystemLocation_acb87263]] = None,
    logging: typing.Optional[typing.Union[_LoggingOptions_31668710, typing.Dict[builtins.str, typing.Any]]] = None,
    partial_build_spec: typing.Optional[_BuildSpec_4961ea5b] = None,
    project_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    role_policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    commands: typing.Sequence[builtins.str],
    additional_inputs: typing.Optional[typing.Mapping[builtins.str, IFileSetProducer]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    env_from_cfn_outputs: typing.Optional[typing.Mapping[builtins.str, _CfnOutput_7273f911]] = None,
    input: typing.Optional[IFileSetProducer] = None,
    install_commands: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary_output_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba510e4eda683498de32392bbad670fabf1cbc35027297fd070669464ed607cd(
    variable_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4050a951f11df379d3f03171015f338d23cc9145a854d86f45352dbc03d023f(
    artifact: _Artifact_0cb05964,
) -> None:
    """Type checking stubs"""
    pass
