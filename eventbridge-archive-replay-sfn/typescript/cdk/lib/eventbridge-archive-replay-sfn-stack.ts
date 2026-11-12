import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as sqs from 'aws-cdk-lib/aws-sqs';

const REPLAY_PREFIX = 'sfn-replay';
const LOOKBACK_MS = 5 * 60 * 1000; // failures start before the alarm reaches ALARM
const END_MARGIN_MS = 2 * 60 * 1000; // covers late metric data after the OK transition
const ARCHIVE_DELAY = cdk.Duration.minutes(10); // EventBridge recommends waiting 10 minutes before a replay
const POLL_INTERVAL = cdk.Duration.seconds(30);
const MAX_POLLS = 60;
// One name per outage: the second at which the alarm entered ALARM.
const REPLAY_NAME = `{% '${REPLAY_PREFIX}-' & $string($floor($alarmMs / 1000)) %}`;
// Newest transition into ALARM at or before the OK event. Timestamps are read as epoch seconds or ISO 8601.
const ALARM_START_MS = `{% ($ms := function($t) { $type($t) = 'number' ? $t * 1000 : $toMillis($t) };
  $up := $states.result.AlarmHistoryItems[$contains(HistorySummary, 'to ALARM') and $ms(Timestamp) <= $okMs];
  $exists($up) ? $ms($up[0].Timestamp) : 0) %}`;
const MESSAGE = `{% 'Replay ' & $replayName & ' ended in state ' & $replayState & '.' & ($replayReason != '' ? ' ' & $replayReason : '')
  & ' Alarm: ' & $alarmName & '. Window: ' & $fromMillis($alarmMs - ${LOOKBACK_MS}) & ' to ' & $fromMillis($okMs + ${END_MARGIN_MS}) %}`;
const TRANSIENT = ['States.Timeout', 'EventBridge.InternalException', 'EventBridge.ThrottlingException'];

export class EventbridgeArchiveReplaySfnStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Custom bus, archive and the rule whose target is made to fail
    const bus = new events.EventBus(this, 'Bus');
    const archive = new events.Archive(this, 'Archive', {
      sourceEventBus: bus,
      eventPattern: { source: ['demo.orders'] },
      retention: cdk.Duration.days(1),
    });
    archive.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);

    // No enforceSSL on purpose: it would add a queue policy, and this queue must have none that allows EventBridge.
    const queue = new sqs.Queue(this, 'DemoTargetQueue', {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    // Deliberately not events.targets.SqsQueue: that class adds the queue policy that lets EventBridge
    // deliver. Without it every delivery fails, and with no retries and no DLQ the events are lost.
    const brokenTarget: events.IRuleTarget = {
      bind: () => ({
        id: 'DemoTargetQueue',
        arn: queue.queueArn,
        retryPolicy: { maximumRetryAttempts: 0, maximumEventAgeInSeconds: 60 },
      }),
    };
    const ordersRule = new events.Rule(this, 'OrdersRule', {
      eventBus: bus,
      eventPattern: { source: ['demo.orders'] },
      targets: [brokenTarget],
    });

    // Alarm on failed deliveries of that one rule
    const alarm = new cloudwatch.Alarm(this, 'FailedInvocationsAlarm', {
      metric: new cloudwatch.Metric({
        namespace: 'AWS/Events',
        metricName: 'FailedInvocations',
        // ruleName is Ref, which can include the bus name for a custom bus; use the RuleName attribute
        dimensionsMap: { EventBusName: bus.eventBusName, RuleName: (ordersRule.node.defaultChild as events.CfnRule).attrRuleName },
        statistic: 'Sum',
        period: cdk.Duration.seconds(60),
      }),
      threshold: 1,
      evaluationPeriods: 1,
      comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
      treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING,
    });

    // Workflow: find outage window -> wait for archive -> StartReplay -> poll DescribeReplay -> SNS
    const topic = new sns.Topic(this, 'ResultTopic', { enforceSSL: true });
    const replayArn = this.formatArn({ service: 'events', resource: 'replay', resourceName: `${REPLAY_PREFIX}-*` });
    const errorToResult = {
      errors: ['States.ALL'],
      assign: {
        replayState: 'ERROR',
        replayReason: "{% $substring($states.errorOutput.Error & ': ' & $states.errorOutput.Cause, 0, 1000) %}",
      },
    };

    const publish = tasks.SnsPublish.jsonata(this, 'PublishResult', {
      topic,
      subject: 'EventBridge replay result',
      message: sfn.TaskInput.fromText(MESSAGE),
      outputs: { replayName: '{% $replayName %}', replayState: '{% $replayState %}', messageId: '{% $states.result.MessageId %}' },
    });
    const done = new sfn.Choice(this, 'ReplayCompleted?', { queryLanguage: sfn.QueryLanguage.JSONATA })
      .when(sfn.Condition.jsonata("{% $replayState = 'COMPLETED' %}"), sfn.Succeed.jsonata(this, 'Completed'))
      .otherwise(sfn.Fail.jsonata(this, 'ReplayNotCompleted', { error: 'ReplayNotCompleted', cause: 'The replay did not reach COMPLETED. See the Amazon SNS message.' }));
    publish.next(done);

    const poll = new sfn.Wait(this, 'WaitForReplay', { queryLanguage: sfn.QueryLanguage.JSONATA, time: sfn.WaitTime.duration(POLL_INTERVAL) });
    const describeReplay = tasks.CallAwsService.jsonata(this, 'DescribeReplay', {
      service: 'eventbridge',
      action: 'describeReplay',
      parameters: { ReplayName: '{% $replayName %}' },
      iamAction: 'events:DescribeReplay',
      iamResources: [replayArn],
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(30)),
      assign: {
        replayState: '{% $states.result.State %}',
        replayReason: "{% $exists($states.result.StateReason) ? $states.result.StateReason : '' %}",
        polls: '{% $polls + 1 %}',
      },
    });
    describeReplay.addRetry({ errors: TRANSIENT, interval: cdk.Duration.seconds(5), maxAttempts: 3 });
    describeReplay.addCatch(publish, errorToResult);
    poll.next(describeReplay);
    describeReplay.next(
      new sfn.Choice(this, 'StillRunning?', { queryLanguage: sfn.QueryLanguage.JSONATA })
        .when(sfn.Condition.jsonata(`{% $replayState in ['STARTING', 'RUNNING', 'CANCELLING'] and $polls < ${MAX_POLLS} %}`), poll)
        .otherwise(publish),
    );

    const startReplay = tasks.CallAwsService.jsonata(this, 'StartReplay', {
      service: 'eventbridge',
      action: 'startReplay',
      parameters: {
        ReplayName: REPLAY_NAME,
        EventSourceArn: archive.archiveArn,
        // Only the failing rule receives the replayed events
        Destination: { Arn: bus.eventBusArn, FilterArns: [ordersRule.ruleArn] },
        EventStartTime: `{% $fromMillis($alarmMs - ${LOOKBACK_MS}) %}`, // the SDK integration needs timestamp strings, not epoch numbers
        EventEndTime: `{% $fromMillis($okMs + ${END_MARGIN_MS}) %}`,
        Description: 'Started by AWS Step Functions after the failed-delivery alarm returned to OK',
      },
      iamAction: 'events:StartReplay',
      iamResources: [archive.archiveArn, bus.eventBusArn, replayArn],
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(30)),
      assign: { replayName: REPLAY_NAME },
    });
    // Permanent errors first, with no retry; a second run for the same outage hits ResourceAlreadyExists
    startReplay.addRetry({
      errors: ['EventBridge.ResourceAlreadyExistsException', 'EventBridge.ResourceNotFoundException', 'EventBridge.LimitExceededException', 'States.Permissions'],
      maxAttempts: 0,
    });
    startReplay.addRetry({ errors: TRANSIENT, interval: cdk.Duration.seconds(5), maxAttempts: 3 });
    startReplay.addCatch(sfn.Succeed.jsonata(this, 'ReplayAlreadyStarted'), { errors: ['EventBridge.ResourceAlreadyExistsException'] });
    startReplay.addCatch(publish, errorToResult);
    startReplay.next(poll);

    const noAlarmStart = sfn.Pass.jsonata(this, 'NoAlarmStart', {
      assign: { replayState: 'NO_ALARM_START', replayReason: 'No transition into ALARM was found in the alarm history before the OK event.' },
    }).next(publish);
    const archiveDelay = new sfn.Wait(this, 'WaitForArchive', { queryLanguage: sfn.QueryLanguage.JSONATA, time: sfn.WaitTime.duration(ARCHIVE_DELAY) });
    archiveDelay.next(startReplay);

    const alarmHistory = tasks.CallAwsService.jsonata(this, 'GetAlarmHistory', {
      service: 'cloudwatch',
      action: 'describeAlarmHistory',
      parameters: { AlarmName: '{% $alarmName %}', HistoryItemType: 'StateUpdate', ScanBy: 'TimestampDescending', MaxRecords: 100 },
      iamAction: 'cloudwatch:DescribeAlarmHistory',
      iamResources: [alarm.alarmArn],
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(30)),
      assign: { alarmMs: ALARM_START_MS },
    });
    alarmHistory.addRetry({ errors: ['States.Timeout', 'CloudWatch.ThrottlingException'], interval: cdk.Duration.seconds(5), maxAttempts: 3 });
    alarmHistory.addCatch(publish, errorToResult);
    alarmHistory.next(
      new sfn.Choice(this, 'AlarmStartFound?', { queryLanguage: sfn.QueryLanguage.JSONATA })
        .when(sfn.Condition.jsonata('{% $alarmMs > 0 %}'), archiveDelay)
        .otherwise(noAlarmStart),
    );

    const init = sfn.Pass.jsonata(this, 'Initialize', {
      assign: {
        alarmName: '{% $states.input.detail.alarmName %}',
        okMs: '{% $toMillis($states.input.time) %}',
        alarmMs: 0,
        polls: 0,
        replayName: 'not-started',
        replayState: 'NOT_STARTED',
        replayReason: '',
      },
    }).next(alarmHistory);

    const logGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const stateMachine = new sfn.StateMachine(this, 'ReplayStateMachine', {
      queryLanguage: sfn.QueryLanguage.JSONATA,
      definitionBody: sfn.DefinitionBody.fromChainable(init),
      timeout: cdk.Duration.hours(1),
      logs: { destination: logGroup, level: sfn.LogLevel.ERROR, includeExecutionData: false },
    });

    // Default bus: start the workflow only when the alarm goes from ALARM to OK
    const startDlq = new sqs.Queue(this, 'StartRuleDlq', { enforceSSL: true, removalPolicy: cdk.RemovalPolicy.DESTROY });
    const startRole = new iam.Role(this, 'StartExecutionRole', {
      assumedBy: new iam.ServicePrincipal('events.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': this.formatArn({ service: 'events', resource: 'rule', resourceName: '*' }) },
        },
      }),
    });
    new events.Rule(this, 'AlarmReturnedToOkRule', {
      eventPattern: {
        source: ['aws.cloudwatch'],
        detailType: ['CloudWatch Alarm State Change'],
        detail: { alarmName: [alarm.alarmName], previousState: { value: ['ALARM'] }, state: { value: ['OK'] } },
      },
      targets: [new targets.SfnStateMachine(stateMachine, { role: startRole, deadLetterQueue: startDlq, retryAttempts: 3 })],
    });

    new cdk.CfnOutput(this, 'EventBusName', { value: bus.eventBusName });
    new cdk.CfnOutput(this, 'ArchiveName', { value: archive.archiveName });
    new cdk.CfnOutput(this, 'QueueUrl', { value: queue.queueUrl });
    new cdk.CfnOutput(this, 'QueueArn', { value: queue.queueArn });
    new cdk.CfnOutput(this, 'OrdersRuleArn', { value: ordersRule.ruleArn });
    new cdk.CfnOutput(this, 'AlarmName', { value: alarm.alarmName });
    new cdk.CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new cdk.CfnOutput(this, 'ResultTopicArn', { value: topic.topicArn });
    new cdk.CfnOutput(this, 'StateMachineLogGroupName', { value: logGroup.logGroupName });
  }
}
