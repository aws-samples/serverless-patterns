import * as cdk from 'aws-cdk-lib';
import { CfnOutput } from 'aws-cdk-lib';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { CfnSchedule, CfnScheduleGroup } from 'aws-cdk-lib/aws-scheduler';
import { Effect, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class EventbridgeScheduleGroupTaggingCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Deploy-time configuration. These drive both the schedule group's tags
    // and the intentional schedule name prefix.
    const environment = this.node.tryGetContext('environment') ?? 'production';
    const owner = this.node.tryGetContext('owner') ?? 'payments-team';
    const costCenter = this.node.tryGetContext('costCenter') ?? 'cc-1234';
    const application = this.node.tryGetContext('application') ?? 'payments';

    // <application>-<environment>-<task>: a sliceable prefix so schedules can
    // be filtered with the NamePrefix parameter of ListSchedules — the native
    // partial-match lever that exact-match tag search cannot provide.
    const namePrefix = `${application}-${environment}-`;

    // The benign target. One SQS queue both schedules send to.
    const targetQueue = new Queue(this, 'TargetQueue', {
      queueName: 'schedule-group-tagging-target',
    });

    // The organization unit. Tags are applied to the GROUP (not to individual
    // schedules) and are set AT CREATION TIME, so there is never an untagged
    // window. Deleting this group cascades to every schedule it contains.
    const scheduleGroup = new CfnScheduleGroup(this, 'WorkloadScheduleGroup', {
      name: `${application}-${environment}`,
      tags: [
        { key: 'environment', value: environment },
        { key: 'owner', value: owner },
        { key: 'cost-center', value: costCenter },
        { key: 'application', value: application },
      ],
    });

    // Least-privilege role the scheduler assumes to call the target. Scoped to
    // sqs:SendMessage on the single queue ARN, trusted only by the scheduler
    // service. The repo's check-iam.js rejects wildcard actions/resources.
    const schedulerRole = new Role(this, 'SchedulerRole', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });
    schedulerRole.addToPolicy(new PolicyStatement({
      effect: Effect.ALLOW,
      actions: ['sqs:SendMessage'],
      resources: [targetQueue.queueArn],
    }));

    // First schedule inside the group, named with the intentional convention.
    const invoiceSweep = new CfnSchedule(this, 'InvoiceSweepSchedule', {
      groupName: scheduleGroup.name,
      name: `${namePrefix}invoice-sweep`,
      description: 'Enqueues the invoice sweep task.',
      scheduleExpression: 'rate(5 minutes)',
      flexibleTimeWindow: { mode: 'OFF' },
      target: {
        arn: targetQueue.queueArn,
        roleArn: schedulerRole.roleArn,
        input: '{"task": "invoice-sweep"}',
      },
    });
    invoiceSweep.node.addDependency(scheduleGroup);

    // Second schedule inside the SAME group, same naming convention. Both
    // inherit the group's organizational context and tags.
    const ledgerRollup = new CfnSchedule(this, 'LedgerRollupSchedule', {
      groupName: scheduleGroup.name,
      name: `${namePrefix}ledger-rollup`,
      description: 'Enqueues the ledger rollup task.',
      scheduleExpression: 'rate(10 minutes)',
      flexibleTimeWindow: { mode: 'OFF' },
      target: {
        arn: targetQueue.queueArn,
        roleArn: schedulerRole.roleArn,
        input: '{"task": "ledger-rollup"}',
      },
    });
    ledgerRollup.node.addDependency(scheduleGroup);

    // CloudFormation Stack Outputs used for testing.
    new CfnOutput(this, 'ScheduleGroupName', {
      description: 'Name of the tagged EventBridge Scheduler schedule group.',
      value: scheduleGroup.name!,
    });
    new CfnOutput(this, 'ScheduleGroupArn', {
      description: 'ARN of the schedule group (use with list-tags-for-resource).',
      value: scheduleGroup.attrArn,
    });
    new CfnOutput(this, 'TargetQueueUrl', {
      description: 'URL of the target SQS queue.',
      value: targetQueue.queueUrl,
    });
    new CfnOutput(this, 'SchedulerRoleArn', {
      description: 'ARN of the least-privilege scheduler execution role.',
      value: schedulerRole.roleArn,
    });
    new CfnOutput(this, 'ScheduleNamePrefix', {
      description: 'Prefix for filtering schedules via ListSchedules NamePrefix.',
      value: namePrefix,
    });
  }
}
