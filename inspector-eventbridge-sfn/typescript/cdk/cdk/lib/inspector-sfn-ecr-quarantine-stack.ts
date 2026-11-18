// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import {
  Stack,
  StackProps,
  RemovalPolicy,
  Duration,
  CfnOutput,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ecr from 'aws-cdk-lib/aws-ecr';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as kms from 'aws-cdk-lib/aws-kms';

/**
 * Inspector -> EventBridge -> Step Functions -> ECR quarantine + SNS.
 *
 * When Amazon Inspector raises a HIGH or CRITICAL finding on an Amazon ECR
 * container image, Amazon EventBridge routes the finding to an AWS Step
 * Functions STANDARD workflow that QUARANTINES the offending image by applying
 * a per-image `quarantine-<digest>` tag to it, then sends an Amazon SNS notification.
 *
 * How the ECR "quarantine tag" is implemented (verified against the ECR API):
 *   An OCI/Docker image in Amazon ECR is identified by its content-addressable
 *   digest (imageHash, e.g. sha256:...). A "tag" is just a named pointer to a
 *   manifest. To add a tag to an EXISTING image WITHOUT rebuilding or copying
 *   image data you:
 *     1. ecr:BatchGetImage  - read the image manifest by its digest.
 *     2. ecr:PutImage       - write the SAME manifest bytes back under a new
 *                             imageTag (`quarantine-<digest hex>`). This is a
 *                             pure control-plane call; no layers are moved.
 *   Both calls are available as Step Functions optimized AWS SDK service
 *   integrations (arn:aws:states:::aws-sdk:ecr:batchGetImage / :putImage), so
 *   the whole quarantine action runs from the state machine with no AWS
 *   Lambda function.
 *
 *   The tag is derived from the image digest (`quarantine-<sha256 hex>`), so
 *   each quarantined image gets its own marker and a tag never moves from one
 *   image to another. Because Amazon Inspector emits one event per finding (and
 *   another on each state change), the same image can start several executions;
 *   a repeat PutImage with the identical manifest and tag fails with
 *   ImageAlreadyExistsException, which the workflow treats as "already
 *   quarantined".
 *
 *   Note on tag mutability: the demo repository is created with MUTABLE tags so
 *   the PutImage re-tag can succeed. PutImageTagMutability is a REPOSITORY-level
 *   setting (not per-image), so flipping the repo to IMMUTABLE mid-workflow
 *   would block the very re-tag we depend on. The `quarantine-<digest>` tag is
 *   therefore the durable per-image marker; downstream lifecycle policies or
 *   admission controllers can key off the `quarantine-` prefix. See README
 *   "Design decisions".
 */
export class InspectorSfnEcrQuarantineStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // ---------------------------------------------------------------------
    // Demo target: an Amazon ECR repository.
    // Tags are MUTABLE so the quarantine re-tag (PutImage) can succeed.
    // scanOnPush requests a scan on push; enhanced scanning by Amazon
    // Inspector must additionally be ENABLED AT THE ACCOUNT LEVEL (see README).
    // ---------------------------------------------------------------------
    const repository = new ecr.Repository(this, 'DemoRepository', {
      // A static, lowercase, valid ECR repository name. Aws.STACK_NAME cannot be
      // used here: it is an unresolved CloudFormation token at synth time and
      // fails ECR's synth-time repositoryName validation.
      repositoryName: 'inspector-quarantine-demo',
      imageTagMutability: ecr.TagMutability.MUTABLE,
      imageScanOnPush: true,
      emptyOnDelete: true, // allow the repo (and its images) to be removed on cleanup
      removalPolicy: RemovalPolicy.DESTROY, // DEMO ONLY - deletes the repo + images on `cdk destroy`
    });

    // ---------------------------------------------------------------------
    // Amazon SNS topic for quarantine notifications.
    // Encrypted at rest with the AWS-managed KMS key for Amazon SNS
    // (alias/aws/sns) - no extra cost and no customer key to manage.
    // ---------------------------------------------------------------------
    const topic = new sns.Topic(this, 'QuarantineTopic', {
      displayName: 'ECR image quarantine notifications',
      masterKey: kms.Alias.fromAliasName(this, 'SnsManagedKey', 'alias/aws/sns'),
    });

    // ---------------------------------------------------------------------
    // Step Functions tasks.
    //
    // The EventBridge event delivers the finding under $.detail. The fields we
    // rely on (verified against the Inspector2 Finding event schema):
    //   $.detail.severity
    //   $.detail.resources[0].details.awsEcrContainerImage.repositoryName
    //   $.detail.resources[0].details.awsEcrContainerImage.imageHash   (sha256:...)
    // ---------------------------------------------------------------------

    // 1) Read the image manifest by digest (BatchGetImage).
    const getManifest = new tasks.CallAwsService(this, 'GetImageManifest', {
      service: 'ecr',
      action: 'batchGetImage',
      // ACCEPTED media types cover both Docker v2 and OCI manifests.
      parameters: {
        RepositoryName: sfn.JsonPath.stringAt(
          '$.detail.resources[0].details.awsEcrContainerImage.repositoryName',
        ),
        ImageIds: [
          {
            ImageDigest: sfn.JsonPath.stringAt(
              '$.detail.resources[0].details.awsEcrContainerImage.imageHash',
            ),
          },
        ],
        AcceptedMediaTypes: [
          'application/vnd.docker.distribution.manifest.v2+json',
          'application/vnd.oci.image.manifest.v1+json',
          'application/vnd.oci.image.index.v1+json',
          'application/vnd.docker.distribution.manifest.list.v2+json',
        ],
      },
      iamResources: [repository.repositoryArn],
      resultPath: '$.manifest',
    });

    // 2) Re-tag the SAME manifest under a per-image quarantine tag (PutImage).
    //    ImageManifest and ImageManifestMediaType are returned by BatchGetImage
    //    above. The tag is derived from the digest (sha256:<hex> -> hex) so every
    //    quarantined image keeps its own tag.
    const digestHex = sfn.JsonPath.arrayGetItem(
      sfn.JsonPath.stringSplit(
        sfn.JsonPath.stringAt(
          '$.detail.resources[0].details.awsEcrContainerImage.imageHash',
        ),
        ':',
      ),
      1,
    );
    const applyQuarantineTag = new tasks.CallAwsService(
      this,
      'ApplyQuarantineTag',
      {
        service: 'ecr',
        action: 'putImage',
        parameters: {
          RepositoryName: sfn.JsonPath.stringAt(
            '$.detail.resources[0].details.awsEcrContainerImage.repositoryName',
          ),
          ImageManifest: sfn.JsonPath.stringAt(
            '$.manifest.Images[0].ImageManifest',
          ),
          ImageManifestMediaType: sfn.JsonPath.stringAt(
            '$.manifest.Images[0].ImageManifestMediaType',
          ),
          ImageTag: sfn.JsonPath.format('quarantine-{}', digestHex),
        },
        iamResources: [repository.repositoryArn],
        resultPath: '$.putImage',
      },
    );

    // Retry only transient ECR errors (server-side faults and throttling) on
    // the two ECR calls. Permanent errors such as Ecr.RepositoryNotFoundException
    // or Ecr.ImageAlreadyExistsException go straight to the Catch.
    const retryProps: sfn.RetryProps = {
      errors: ['Ecr.ServerException', 'Ecr.ThrottlingException', 'States.Timeout'],
      interval: Duration.seconds(2),
      maxAttempts: 3,
      backoffRate: 2,
    };
    getManifest.addRetry(retryProps);
    applyQuarantineTag.addRetry(retryProps);

    // 3) Success notification via Amazon SNS.
    const notifyQuarantined = new tasks.SnsPublish(this, 'NotifyQuarantined', {
      topic,
      subject: 'ECR image quarantined',
      message: sfn.TaskInput.fromObject({
        status: 'QUARANTINED',
        repository: sfn.JsonPath.stringAt(
          '$.detail.resources[0].details.awsEcrContainerImage.repositoryName',
        ),
        imageDigest: sfn.JsonPath.stringAt(
          '$.detail.resources[0].details.awsEcrContainerImage.imageHash',
        ),
        severity: sfn.JsonPath.stringAt('$.detail.severity'),
        quarantineTag: sfn.JsonPath.format('quarantine-{}', digestHex),
        findingTitle: sfn.JsonPath.stringAt('$.detail.title'),
      }),
    });

    // 4) Failure notification path (Catch target for the quarantine steps).
    const notifyFailure = new tasks.SnsPublish(this, 'NotifyFailure', {
      topic,
      subject: 'ECR image quarantine FAILED',
      message: sfn.TaskInput.fromObject({
        status: 'QUARANTINE_FAILED',
        severity: sfn.JsonPath.stringAt('$.detail.severity'),
        error: sfn.JsonPath.stringAt('$.error'),
        detail: sfn.JsonPath.stringAt('$.detail'),
      }),
    });
    const fail = new sfn.Fail(this, 'QuarantineFailed', {
      cause: 'ECR image quarantine failed. See the Amazon SNS failure notification.',
      error: 'QuarantineError',
    });
    notifyFailure.next(fail);

    // 5) Optional rebuild/patch branch placeholder. This pattern quarantines;
    //    a real deployment would trigger a CI rebuild here (e.g. start a
    //    CodeBuild project or notify a pipeline). Kept as a documented no-op
    //    so the composition stays focused on the remediation headline.
    const rebuildHint = new sfn.Pass(this, 'RebuildBranchHint', {
      comment:
        'Extension point: kick off a patched-image rebuild (CodeBuild / pipeline) here.',
      result: sfn.Result.fromObject({
        note: 'Rebuild/patch branch is an intentional extension point. See README.',
      }),
      resultPath: '$.rebuild',
    });

    // BatchGetImage returns HTTP 200 with an empty `images` array (and the
    // image under `failures`) when the image no longer exists, for example if
    // it was deleted between the finding and this execution. Referencing
    // $.manifest.Images[0] would then raise States.Runtime, which a
    // States.ALL Catch does not catch, so check for the manifest first and
    // route the missing case to the failure notification.
    const manifestMissing = new sfn.Pass(this, 'ImageManifestMissing', {
      comment: 'BatchGetImage returned no usable manifest (image deleted or no media type).',
      result: sfn.Result.fromObject({
        Error: 'ImageManifestMissing',
        Cause: 'BatchGetImage returned no image manifest for the finding. The image may have been deleted.',
      }),
      resultPath: '$.error',
    });
    manifestMissing.next(notifyFailure);

    const hasManifest = new sfn.Choice(this, 'HasImageManifest')
      .when(
        sfn.Condition.and(
          sfn.Condition.isPresent('$.manifest.Images[0].ImageManifest'),
          sfn.Condition.isPresent('$.manifest.Images[0].ImageManifestMediaType'),
        ),
        applyQuarantineTag,
      )
      .otherwise(manifestMissing);

    // Wire the quarantine happy path, attaching a Catch to the failure path.
    const quarantineFlow = getManifest.next(hasManifest);
    applyQuarantineTag.next(rebuildHint).next(notifyQuarantined);

    getManifest.addCatch(notifyFailure, { resultPath: '$.error' });

    // Inspector emits one event per finding, so repeat executions for the same
    // image call PutImage with an identical manifest and tag and get
    // Ecr.ImageAlreadyExistsException. Treat that as success. This Catch is
    // added BEFORE the States.ALL one so it is evaluated first.
    const alreadyQuarantined = new sfn.Pass(this, 'AlreadyQuarantined', {
      comment: 'Image already carries its quarantine tag; nothing to do.',
    });
    applyQuarantineTag.addCatch(alreadyQuarantined, {
      errors: ['Ecr.ImageAlreadyExistsException'],
      resultPath: '$.putImage',
    });
    applyQuarantineTag.addCatch(notifyFailure, { resultPath: '$.error' });

    // Severity Choice: act only on HIGH/CRITICAL; otherwise skip.
    const skip = new sfn.Pass(this, 'SkipLowSeverity', {
      comment: 'Severity below HIGH - no quarantine action taken.',
    });

    const definition = new sfn.Choice(this, 'IsHighOrCritical')
      .when(
        sfn.Condition.or(
          sfn.Condition.stringEquals('$.detail.severity', 'HIGH'),
          sfn.Condition.stringEquals('$.detail.severity', 'CRITICAL'),
        ),
        quarantineFlow,
      )
      .otherwise(skip);

    // ---------------------------------------------------------------------
    // STANDARD state machine with full execution logging.
    // ---------------------------------------------------------------------
    const logGroup = new logs.LogGroup(this, 'StateMachineLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY, // DEMO ONLY
    });

    const stateMachine = new sfn.StateMachine(this, 'QuarantineStateMachine', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      stateMachineType: sfn.StateMachineType.STANDARD,
      timeout: Duration.minutes(5),
      logs: {
        destination: logGroup,
        level: sfn.LogLevel.ALL,
        includeExecutionData: true,
      },
      tracingEnabled: true,
    });

    // Least-privilege: the CallAwsService tasks already added ECR actions
    // scoped to the repository ARN via `iamResources`. SnsPublish grants
    // publish scoped to the topic automatically. No wildcards are used.

    // ---------------------------------------------------------------------
    // Amazon EventBridge rule: ACTIVE Inspector2 HIGH/CRITICAL findings on images
    // in the demo ECR repository.
    // ---------------------------------------------------------------------
    const rule = new events.Rule(this, 'InspectorEcrFindingRule', {
      description:
        'Route ACTIVE HIGH/CRITICAL Amazon Inspector findings on container images in the demo Amazon ECR repository to the quarantine workflow',
      eventPattern: {
        source: ['aws.inspector2'],
        detailType: ['Inspector2 Finding'],
        detail: {
          severity: ['HIGH', 'CRITICAL'],
          // Skip events for findings that moved to CLOSED or SUPPRESSED.
          status: ['ACTIVE'],
          resources: {
            type: ['AWS_ECR_CONTAINER_IMAGE'],
            // Only the demo repository: the state machine role has ECR
            // permissions on this repository alone.
            details: {
              awsEcrContainerImage: {
                repositoryName: [repository.repositoryName],
              },
            },
          },
        },
      },
    });

    // EventBridge -> Step Functions. The construct creates a scoped role that
    // may only StartExecution on THIS state machine. A dead-letter queue
    // captures any event that Amazon EventBridge cannot deliver to the
    // workflow (for example, a transient StartExecution throttle) so no
    // finding is silently lost.
    const dlq = new sqs.Queue(this, 'InspectorRuleDlq', {
      retentionPeriod: Duration.days(14),
      enforceSSL: true,
    });
    rule.addTarget(
      new targets.SfnStateMachine(stateMachine, {
        deadLetterQueue: dlq,
      }),
    );

    // ---------------------------------------------------------------------
    // Outputs.
    // ---------------------------------------------------------------------
    new CfnOutput(this, 'RepositoryName', {
      value: repository.repositoryName,
      description: 'Push a vulnerable image here to trigger the workflow',
    });
    new CfnOutput(this, 'RepositoryUri', { value: repository.repositoryUri });
    new CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new CfnOutput(this, 'SnsTopicArn', {
      value: topic.topicArn,
      description: 'Subscribe to this topic to receive quarantine notifications',
    });
  }
}
