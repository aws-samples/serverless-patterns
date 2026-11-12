import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';

// The job role may tag only objects under this prefix. Objects elsewhere in the
// source bucket produce failed tasks, which is how the README forces the failure branch.
const TAGGABLE_PREFIX = 'data/';
const POLL_SECONDS = 15;
const MAX_POLLS = 40; // 40 x 15 s = 10 minutes, then the workflow reports the last known status
const BATCH_OPS_PRINCIPAL = 'batchoperations.s3.amazonaws.com';

export class S3SfnBatchOperationsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucketProps: s3.BucketProps = {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      enforceSSL: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // demo data only
      autoDeleteObjects: true, // CDK helper function (not part of the workflow) empties the bucket on destroy
    };
    const sourceBucket = new s3.Bucket(this, 'SourceBucket', bucketProps);
    const reportBucket = new s3.Bucket(this, 'ReportBucket', bucketProps);
    const topic = new sns.Topic(this, 'ResultTopic', { enforceSSL: true });

    // Role that S3 Batch Operations assumes to run the job. The S3 documentation shows no
    // aws:SourceAccount or aws:SourceArn condition for this trust policy, so none is added.
    const jobRole = new iam.Role(this, 'BatchJobRole', {
      assumedBy: new iam.ServicePrincipal(BATCH_OPS_PRINCIPAL),
    });
    jobRole.addToPolicy(new iam.PolicyStatement({
      actions: ['s3:PutObjectTagging', 's3:PutObjectVersionTagging'],
      resources: [sourceBucket.arnForObjects(`${TAGGABLE_PREFIX}*`)],
    }));
    jobRole.addToPolicy(new iam.PolicyStatement({
      // Documented for jobs that use an S3 generated manifest
      actions: ['s3:PutInventoryConfiguration'],
      resources: [sourceBucket.bucketArn],
    }));
    jobRole.addToPolicy(new iam.PolicyStatement({
      actions: ['s3:PutObject'],
      resources: [reportBucket.arnForObjects('manifests/*'), reportBucket.arnForObjects('reports/*')],
    }));
    jobRole.addToPolicy(new iam.PolicyStatement({
      actions: ['s3:GetObject', 's3:GetObjectVersion'],
      resources: [reportBucket.arnForObjects('manifests/*')],
    }));
    jobRole.addToPolicy(new iam.PolicyStatement({
      actions: ['s3:ListBucket'],
      resources: [reportBucket.bucketArn],
    }));

    // Step Functions has no .sync integration for S3 Control, so the workflow starts the job
    // with CreateJob and polls DescribeJob. ClientRequestToken is the execution name, so a
    // retried CreateJob returns the same job instead of creating a second one.
    const createJob = tasks.CallAwsService.jsonata(this, 'CreateJob', {
      service: 's3control',
      action: 'createJob',
      iamAction: 's3:CreateJob',
      iamResources: ['*'], // CreateJob is an account-level action with no resource type
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(30)),
      parameters: {
        AccountId: this.account,
        ClientRequestToken: '{% $states.context.Execution.Name %}',
        ConfirmationRequired: false,
        Priority: 10,
        RoleArn: jobRole.roleArn,
        Description: 'Tag objects by key prefix, started by AWS Step Functions',
        Operation: {
          S3PutObjectTagging: {
            TagSet: [{
              Key: "{% $exists($states.input.tagKey) ? $states.input.tagKey : 'processed' %}",
              Value: "{% $exists($states.input.tagValue) ? $states.input.tagValue : 'true' %}",
            }],
          },
        },
        ManifestGenerator: {
          S3JobManifestGenerator: {
            SourceBucket: sourceBucket.bucketArn,
            ExpectedBucketOwner: this.account,
            EnableManifestOutput: true,
            ManifestOutputLocation: {
              Bucket: reportBucket.bucketArn,
              ExpectedManifestBucketOwner: this.account,
              ManifestPrefix: 'manifests',
              ManifestFormat: 'S3InventoryReport_CSV_20211130',
            },
            Filter: { KeyNameConstraint: { MatchAnyPrefix: ['{% $states.input.prefix %}'] } },
          },
        },
        Report: {
          Bucket: reportBucket.bucketArn,
          ExpectedBucketOwner: this.account,
          Enabled: true,
          Format: 'Report_CSV_20180820',
          Prefix: 'reports',
          ReportScope: 'FailedTasksOnly',
        },
      },
      assign: { jobId: '{% $states.result.JobId %}', attempts: 0 },
    });

    // NumberOfTasksFailed can be absent while the job is still preparing, so each read is guarded
    const count = (field: string) =>
      `{% $exists($states.result.Job.ProgressSummary.${field}) ? $states.result.Job.ProgressSummary.${field} : 0 %}`;
    const describeJob = tasks.CallAwsService.jsonata(this, 'DescribeJob', {
      service: 's3control',
      action: 'describeJob',
      iamAction: 's3:DescribeJob',
      iamResources: [`arn:${this.partition}:s3:${this.region}:${this.account}:job/*`],
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(30)),
      parameters: { AccountId: this.account, JobId: '{% $jobId %}' },
      assign: {
        status: '{% $states.result.Job.Status %}',
        failed: count('NumberOfTasksFailed'),
        succeeded: count('NumberOfTasksSucceeded'),
        total: count('TotalNumberOfTasks'),
        attempts: '{% $attempts + 1 %}',
      },
    });

    // Permanent errors first with no retry, then the transient errors from the API reference
    const addRetries = (task: tasks.CallAwsService, permanentError: string) => {
      task
        .addRetry({ errors: ['States.Permissions', 'S3Control.BadRequestException', `S3Control.${permanentError}`], maxAttempts: 0 })
        .addRetry({
          errors: ['S3Control.TooManyRequestsException', 'S3Control.InternalServiceException', 'States.Timeout'],
          interval: cdk.Duration.seconds(2), maxAttempts: 3, backoffRate: 2,
        });
    };
    addRetries(createJob, 'IdempotencyException');
    addRetries(describeJob, 'NotFoundException');

    const notifySuccess = tasks.SnsPublish.jsonata(this, 'NotifySuccess', {
      topic,
      subject: 'S3 Batch Operations job succeeded',
      message: sfn.TaskInput.fromText(
        '{% "Job " & $jobId & " completed: " & $string($succeeded) & " of " & $string($total) & " tasks succeeded, 0 failed." %}'),
      outputs: { JobId: '{% $jobId %}', Status: '{% $status %}', TasksSucceeded: '{% $succeeded %}', TasksFailed: '{% $failed %}' },
    });
    const notifyJobFailure = tasks.SnsPublish.jsonata(this, 'NotifyJobFailure', {
      topic,
      subject: 'S3 Batch Operations job needs attention',
      // A job still Preparing, Ready or Active when the poll budget runs out has not ended: say so
      message: sfn.TaskInput.fromText(
        '{% $status in ["Complete", "Failed", "Cancelled"] ' +
        '? "Job " & $jobId & " ended with status " & $status & ": " & $string($failed) & " of " & $string($total) & " tasks failed." ' +
        ': "Job " & $jobId & " was still " & $status & " after " & $string($attempts) & " status checks, so the workflow stopped waiting. ' +
        'The job may still be running. " & $string($failed) & " of " & $string($total) & " tasks had failed at the last check." %}'),
    });
    const notifyError = tasks.SnsPublish.jsonata(this, 'NotifyError', {
      topic,
      subject: 'S3 Batch Operations workflow error',
      message: sfn.TaskInput.fromText('{% "The workflow could not run the job: " & $states.input.Error & " " & $states.input.Cause %}'),
    });
    createJob.addCatch(notifyError, { errors: ['States.ALL'] });
    describeJob.addCatch(notifyError, { errors: ['States.ALL'] });

    const jobFailed = sfn.Fail.jsonata(this, 'JobNotSuccessful', {
      error: 'JobNotSuccessful',
      cause: 'The job did not end Complete with zero failed tasks, or it was still running when the poll budget ran out. Read the Amazon SNS message and the completion report.',
    });
    const workflowError = sfn.Fail.jsonata(this, 'WorkflowError', {
      error: 'WorkflowError',
      cause: 'CreateJob or DescribeJob failed. The Amazon SNS message has the error name and cause.',
    });
    const invalidInput = sfn.Fail.jsonata(this, 'InvalidInput', {
      error: 'InvalidInput',
      cause: 'The execution input needs a non-empty string field named prefix.',
    });

    // Poll until the job reaches a terminal status, then branch on the failed-task count
    const wait = sfn.Wait.jsonata(this, 'WaitForJob', { time: sfn.WaitTime.duration(cdk.Duration.seconds(POLL_SECONDS)) });
    const evaluate = sfn.Choice.jsonata(this, 'EvaluateJob')
      .when(sfn.Condition.jsonata("{% $status = 'Complete' and $failed = 0 %}"), notifySuccess.next(new sfn.Succeed(this, 'Done')))
      .when(
        sfn.Condition.jsonata(`{% $status in ['Complete', 'Failed', 'Cancelled'] or $attempts >= ${MAX_POLLS} %}`),
        notifyJobFailure.next(jobFailed))
      .otherwise(wait);
    notifyError.next(workflowError);

    const validate = sfn.Choice.jsonata(this, 'ValidateInput')
      .when(
        sfn.Condition.jsonata("{% $exists($states.input.prefix) and $type($states.input.prefix) = 'string' and $length($states.input.prefix) > 0 %}"),
        createJob.next(wait).next(describeJob).next(evaluate))
      .otherwise(invalidInput);

    const logGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const stateMachine = new sfn.StateMachine(this, 'BatchOperationsWorkflow', {
      queryLanguage: sfn.QueryLanguage.JSONATA,
      definitionBody: sfn.DefinitionBody.fromChainable(validate),
      timeout: cdk.Duration.minutes(20), // longer than the 10 minute poll budget
      logs: { destination: logGroup, level: sfn.LogLevel.ERROR, includeExecutionData: false },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    stateMachine.addToRolePolicy(new iam.PolicyStatement({
      // Documented for jobs that use an S3 generated manifest
      actions: ['s3:PutInventoryConfiguration'],
      resources: [sourceBucket.bucketArn],
    }));
    // The role is passed to S3 with PassedToService s3.amazonaws.com, not the batchoperations principal
    // that the job role trusts (a sandbox run with the batchoperations value was denied at CreateJob).
    stateMachine.addToRolePolicy(new iam.PolicyStatement({
      actions: ['iam:PassRole'],
      resources: [jobRole.roleArn],
      conditions: { StringEquals: { 'iam:PassedToService': 's3.amazonaws.com' } },
    }));

    new cdk.CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new cdk.CfnOutput(this, 'StateMachineLogGroupName', { value: logGroup.logGroupName });
    new cdk.CfnOutput(this, 'SourceBucketName', { value: sourceBucket.bucketName });
    new cdk.CfnOutput(this, 'ReportBucketName', { value: reportBucket.bucketName });
    new cdk.CfnOutput(this, 'TopicArn', { value: topic.topicArn });
  }
}
