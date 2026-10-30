import * as cdk from 'aws-cdk-lib';
import * as codebuild from 'aws-cdk-lib/aws-codebuild';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as subscriptions from 'aws-cdk-lib/aws-sns-subscriptions';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import { Construct } from 'constructs';

// The state machine may only touch stacks whose name starts with this prefix.
const TARGET_STACK_PREFIX = 'release-gate-';
// Change sets created by the state machine are named gate-<uuid>.
const CHANGE_SET_PREFIX = 'gate-';

// Policy check run by CodeBuild against the template that the change set will deploy.
// Rule 1: no IAM resources. Rule 2: every Amazon SQS queue states its DeletionPolicy.
const POLICY_CHECK = `python3 - <<'PY'
import json, os, sys
resources = json.loads(os.environ["TEMPLATE_BODY"]).get("Resources", {})
errors = []
for name, res in resources.items():
    if res.get("Type", "").startswith("AWS::IAM::"):
        errors.append(name + ": IAM resources are not allowed in this release gate")
    if res.get("Type") == "AWS::SQS::Queue" and "DeletionPolicy" not in res:
        errors.append(name + ": set DeletionPolicy explicitly (Delete or Retain)")
if errors:
    print("POLICY CHECK FAILED")
    for e in errors:
        print(" - " + e)
    sys.exit(1)
print("Policy check passed for " + str(len(resources)) + " resource(s)")
PY`;

export class SfnCodebuildReleaseGateStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Optional settings: -c approverEmail=you@example.com, -c approvalTimeoutSeconds=600
    const approverEmail = this.node.tryGetContext('approverEmail') as string | undefined;
    const approvalTimeoutSeconds = Number(this.node.tryGetContext('approvalTimeoutSeconds') ?? 3600);
    if (!Number.isInteger(approvalTimeoutSeconds) || approvalTimeoutSeconds < 60 || approvalTimeoutSeconds > 86400) {
      throw new Error('approvalTimeoutSeconds must be an integer between 60 and 86400');
    }

    const stackArns = this.formatArn({ service: 'cloudformation', resource: 'stack', resourceName: `${TARGET_STACK_PREFIX}*/*` });

    // CloudFormation service role for the target stacks: Amazon SQS queues named release-gate-* only.
    const deploymentRole = new iam.Role(this, 'DeploymentRole', {
      assumedBy: new iam.PrincipalWithConditions(new iam.ServicePrincipal('cloudformation.amazonaws.com'), {
        StringEquals: { 'aws:SourceAccount': this.account },
        ArnLike: { 'aws:SourceArn': stackArns },
      }),
      inlinePolicies: {
        Queues: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: [
                'sqs:CreateQueue', 'sqs:DeleteQueue', 'sqs:GetQueueUrl', 'sqs:GetQueueAttributes',
                'sqs:SetQueueAttributes', 'sqs:ListQueueTags', 'sqs:TagQueue', 'sqs:UntagQueue',
              ],
              resources: [this.formatArn({ service: 'sqs', resource: `${TARGET_STACK_PREFIX}*`, arnFormat: cdk.ArnFormat.NO_RESOURCE_NAME })],
            }),
          ],
        }),
      },
    });

    // CodeBuild project with no source: the template arrives as an environment variable override.
    const buildLogGroup = new logs.LogGroup(this, 'BuildLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const project = new codebuild.Project(this, 'PolicyCheckProject', {
      environment: { buildImage: codebuild.LinuxBuildImage.STANDARD_8_0, computeType: codebuild.ComputeType.SMALL },
      timeout: cdk.Duration.minutes(5),
      logging: { cloudWatch: { logGroup: buildLogGroup } },
      buildSpec: codebuild.BuildSpec.fromObject({
        version: '0.2',
        phases: {
          install: { 'runtime-versions': { python: '3.13' } },
          build: { commands: [POLICY_CHECK] },
        },
      }),
    });

    const topic = new sns.Topic(this, 'ApprovalTopic', { enforceSSL: true });
    if (approverEmail) topic.addSubscription(new subscriptions.EmailSubscription(approverEmail));

    // Terminal states
    const policyCheckFailed = new sfn.Fail(this, 'PolicyCheckFailed', {
      error: 'PolicyCheckFailed',
      cause: 'The CodeBuild policy check failed or did not finish. No change set was created. Read the BuildLogGroupName log group.',
    });
    const awsCallFailed = new sfn.Fail(this, 'AwsCallFailed', { errorPath: '$.error.Error', causePath: '$.error.Cause' });
    const changeSetFailed = new sfn.Fail(this, 'ChangeSetFailed', { error: 'ChangeSetFailed', causePath: '$.cs.StatusReason' });
    const unexpectedChangeSetStatus = new sfn.Fail(this, 'UnexpectedChangeSetStatus', {
      error: 'UnexpectedChangeSetStatus',
      cause: 'The change set ended in a status this workflow does not handle. See the DescribeChangeSet event in the execution history.',
    });
    const notApproved = new sfn.Fail(this, 'NotApproved', {
      error: 'NotApproved',
      cause: 'The approver rejected the release or the approval request failed. The change set was deleted.',
    });
    const approvalTimedOut = new sfn.Fail(this, 'ApprovalTimedOut', {
      error: 'ApprovalTimedOut',
      cause: 'No approval arrived before the timeout. The change set was deleted.',
    });
    const stackFailed = new sfn.Fail(this, 'StackOperationFailed', { error: 'StackOperationFailed', causePath: '$.stack.status' });
    const nothingToDeploy = new sfn.Succeed(this, 'NothingToDeploy');
    const released = new sfn.Succeed(this, 'Released');

    // CloudFormation through the AWS SDK integration. No wait-for-completion exists, so the workflow polls.
    const cfnTask = (idName: string, action: string, parameters: Record<string, unknown>, resources: string[], extra: Partial<tasks.CallAwsServiceProps> = {}) =>
      new tasks.CallAwsService(this, idName, {
        service: 'cloudformation',
        action,
        parameters,
        iamAction: `cloudformation:${action[0].toUpperCase()}${action.slice(1)}`,
        iamResources: resources,
        taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(30)), // SDK integrations have no timeout unless set
        ...extra,
      });
    const stackName = sfn.JsonPath.stringAt('$.stackName');
    const changeSetId = sfn.JsonPath.stringAt('$.changeSet.id');
    // Read-only calls: permanent errors first with no retry, then retry task failures and timeouts.
    const retryReads = (t: tasks.CallAwsService, permanent: string[]) => {
      t.addRetry({ errors: ['States.Permissions', ...permanent], maxAttempts: 0 });
      t.addRetry({ errors: ['States.TaskFailed', 'States.Timeout'], interval: cdk.Duration.seconds(2), maxAttempts: 3, backoffRate: 2 });
      return t;
    };
    const deleteChangeSet = (idName: string) =>
      cfnTask(idName, 'deleteChangeSet', { ChangeSetName: changeSetId }, [stackArns], { resultPath: sfn.JsonPath.DISCARD });

    const prepare = new sfn.Pass(this, 'PrepareChangeSetName', {
      parameters: { changeSetName: sfn.JsonPath.format(`${CHANGE_SET_PREFIX}{}`, sfn.JsonPath.uuid()) },
      resultPath: '$.release',
    });

    // 1. CodeBuild runs the policy check on the same template body the change set will use.
    const policyCheck = new tasks.CodeBuildStartBuild(this, 'RunPolicyCheck', {
      project,
      integrationPattern: sfn.IntegrationPattern.RUN_JOB,
      environmentVariablesOverride: {
        TEMPLATE_BODY: { type: codebuild.BuildEnvironmentVariableType.PLAINTEXT, value: sfn.JsonPath.stringAt('$.templateBody') },
      },
      taskTimeout: sfn.Timeout.duration(cdk.Duration.minutes(10)),
      resultSelector: { 'buildStatus.$': '$.Build.BuildStatus' },
      resultPath: '$.build',
    });
    policyCheck.addCatch(policyCheckFailed, { errors: ['States.ALL'], resultPath: '$.error' });

    // 2. Create the change set and poll until CloudFormation finishes computing it.
    const createChangeSet = cfnTask('CreateChangeSet', 'createChangeSet', {
      StackName: stackName,
      ChangeSetName: sfn.JsonPath.stringAt('$.release.changeSetName'),
      ChangeSetType: sfn.JsonPath.stringAt('$.changeSetType'),
      TemplateBody: sfn.JsonPath.stringAt('$.templateBody'),
      RoleARN: deploymentRole.roleArn,
    }, [stackArns], { resultSelector: { 'id.$': '$.Id' }, resultPath: '$.changeSet' });
    createChangeSet.addCatch(awsCallFailed, { errors: ['States.ALL'], resultPath: '$.error' });
    const waitForChangeSet = new sfn.Wait(this, 'WaitForChangeSet', { time: sfn.WaitTime.duration(cdk.Duration.seconds(5)) });
    const describeChangeSet = retryReads(cfnTask('DescribeChangeSet', 'describeChangeSet', { ChangeSetName: changeSetId }, [stackArns], { resultPath: '$.cs' }), ['CloudFormation.ChangeSetNotFoundException']);

    // 3. Human approval: the task token travels in an Amazon SNS message. No retry here: a rejection is also a task failure.
    const requestApproval = new tasks.SnsPublish(this, 'RequestApproval', {
      topic,
      integrationPattern: sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
      subject: 'Release gate: approval needed',
      message: sfn.TaskInput.fromObject({
        taskToken: sfn.JsonPath.taskToken,
        stackName,
        changeSetId,
        changes: sfn.JsonPath.listAt('$.cs.Changes'),
        approve: 'aws stepfunctions send-task-success --task-token <taskToken> --task-output \'{}\'',
        reject: 'aws stepfunctions send-task-failure --task-token <taskToken> --error Rejected --cause <reason>',
      }),
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(approvalTimeoutSeconds)),
      resultPath: '$.approval',
    });
    const deleteAfterTimeout = deleteChangeSet('DeleteChangeSetAfterTimeout');
    const deleteAfterRejection = deleteChangeSet('DeleteChangeSetAfterRejection');
    requestApproval.addCatch(deleteAfterTimeout, { errors: ['States.Timeout'], resultPath: '$.approval' });
    requestApproval.addCatch(deleteAfterRejection, { errors: ['States.TaskFailed'], resultPath: '$.approval' });
    deleteAfterTimeout.next(approvalTimedOut);
    deleteAfterRejection.next(notApproved);

    // 4. Execute, wait until the change set reports EXECUTE_COMPLETE or EXECUTE_FAILED, then read the stack status.
    // Reading the stack alone could return the status from before the update started (false success).
    const executeChangeSet = cfnTask('ExecuteChangeSet', 'executeChangeSet', { ChangeSetName: changeSetId }, [stackArns], { resultPath: sfn.JsonPath.DISCARD });
    executeChangeSet.addCatch(awsCallFailed, { errors: ['States.ALL'], resultPath: '$.error' });
    const waitForExecution = new sfn.Wait(this, 'WaitForExecution', { time: sfn.WaitTime.duration(cdk.Duration.seconds(10)) });
    const describeExecution = retryReads(cfnTask('DescribeExecution', 'describeChangeSet', { ChangeSetName: changeSetId }, [stackArns], {
      resultSelector: { 'status.$': '$.ExecutionStatus' },
      resultPath: '$.exec',
    }), ['CloudFormation.ChangeSetNotFoundException']);
    const describeStack = retryReads(cfnTask('DescribeStack', 'describeStacks', { StackName: stackName }, [stackArns], {
      resultSelector: { 'status.$': '$.Stacks[0].StackStatus' },
      resultPath: '$.stack',
    }), []);

    const noChanges = sfn.Condition.and(
      sfn.Condition.stringEquals('$.cs.Status', 'FAILED'),
      sfn.Condition.isPresent('$.cs.StatusReason'), // guard: States.Runtime is not caught by States.ALL
      sfn.Condition.or(
        sfn.Condition.stringMatches('$.cs.StatusReason', '*contain changes*'),
        sfn.Condition.stringMatches('$.cs.StatusReason', '*No updates are to be performed*'),
      ),
    );
    const changeSetChoice = new sfn.Choice(this, 'ChangeSetReady')
      .when(sfn.Condition.stringEquals('$.cs.Status', 'CREATE_COMPLETE'), requestApproval)
      .when(noChanges, deleteChangeSet('DeleteEmptyChangeSet').next(nothingToDeploy))
      .when(sfn.Condition.and(sfn.Condition.stringEquals('$.cs.Status', 'FAILED'), sfn.Condition.isPresent('$.cs.StatusReason')), changeSetFailed)
      .when(sfn.Condition.or(
        sfn.Condition.stringEquals('$.cs.Status', 'CREATE_PENDING'),
        sfn.Condition.stringEquals('$.cs.Status', 'CREATE_IN_PROGRESS'),
      ), waitForChangeSet)
      .otherwise(unexpectedChangeSetStatus);
    const executionChoice = new sfn.Choice(this, 'ExecutionSettled')
      .when(sfn.Condition.or(
        sfn.Condition.stringEquals('$.exec.status', 'EXECUTE_COMPLETE'),
        sfn.Condition.stringEquals('$.exec.status', 'EXECUTE_FAILED'),
      ), describeStack)
      .when(sfn.Condition.or(
        sfn.Condition.stringEquals('$.exec.status', 'AVAILABLE'),
        sfn.Condition.stringEquals('$.exec.status', 'EXECUTE_IN_PROGRESS'),
      ), waitForExecution)
      .otherwise(unexpectedChangeSetStatus);
    const stackChoice = new sfn.Choice(this, 'StackSettled')
      .when(sfn.Condition.or(
        sfn.Condition.stringEquals('$.stack.status', 'CREATE_COMPLETE'),
        sfn.Condition.stringEquals('$.stack.status', 'UPDATE_COMPLETE'),
      ), released)
      .when(sfn.Condition.stringMatches('$.stack.status', '*_IN_PROGRESS'), waitForExecution)
      .otherwise(stackFailed);

    prepare.next(policyCheck).next(createChangeSet).next(waitForChangeSet).next(describeChangeSet).next(changeSetChoice);
    requestApproval.next(executeChangeSet);
    executeChangeSet.next(waitForExecution).next(describeExecution).next(executionChoice);
    describeStack.next(stackChoice);

    // Logs avoid execution data on purpose: the task token and the template body stay out of Amazon CloudWatch Logs.
    const stateMachineLogGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const stateMachine = new sfn.StateMachine(this, 'ReleaseGate', {
      definitionBody: sfn.DefinitionBody.fromChainable(prepare),
      timeout: cdk.Duration.seconds(approvalTimeoutSeconds + 3600),
      logs: { destination: stateMachineLogGroup, level: sfn.LogLevel.ERROR, includeExecutionData: false },
    });
    stateMachine.addToRolePolicy(new iam.PolicyStatement({
      actions: ['iam:PassRole'],
      resources: [deploymentRole.roleArn],
      conditions: { StringEquals: { 'iam:PassedToService': 'cloudformation.amazonaws.com' } },
    }));

    new cdk.CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new cdk.CfnOutput(this, 'ApprovalTopicArn', { value: topic.topicArn });
    new cdk.CfnOutput(this, 'BuildLogGroupName', { value: buildLogGroup.logGroupName });
    new cdk.CfnOutput(this, 'StateMachineLogGroupName', { value: stateMachineLogGroup.logGroupName });
  }
}
