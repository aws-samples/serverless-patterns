import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as firehose from 'aws-cdk-lib/aws-kinesisfirehose';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as opensearch from 'aws-cdk-lib/aws-opensearchservice';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

/**
 * EventBridge -> Amazon Data Firehose -> OpenSearch (Event Monitor pattern)
 *
 * A catch-all EventBridge rule captures every event on a custom bus and
 * streams it to an OpenSearch domain through Amazon Data Firehose, giving
 * full-text search over event payloads within about 60 seconds.
 *
 * Flow:
 *   Any producer -> EventBridge custom bus
 *     -> Rule (matches ALL events)
 *       -> Firehose delivery stream
 *         -> transform Lambda (flattens the EventBridge envelope)
 *         -> OpenSearch domain, daily-rotated index
 *         -> S3 bucket (backup + transform/delivery failures)
 *
 * Auth model:
 * - Rule -> Firehose: the rule target's IAM role holds firehose:PutRecord
 *   and firehose:PutRecordBatch, scoped to this delivery stream.
 * - Firehose -> OpenSearch: SigV4 with the Firehose delivery role. Access
 *   is granted on both sides -- an identity policy on the role AND a
 *   domain access policy naming the role as principal. A managed domain
 *   authorizes every request against its access policy, so the identity
 *   policy alone is not enough.
 * - Firehose -> Lambda / S3 / CloudWatch Logs: same delivery role.
 * - Operator -> Dashboards: browsers cannot sign requests with SigV4, so
 *   Dashboards access is granted to an optional IP CIDR instead. Omit the
 *   `dashboardAccessIp` context value and the domain stays closed to
 *   everything except Firehose.
 *
 * Context values:
 *   -c dashboardAccessIp=1.2.3.4/32   grant Dashboards access to a CIDR
 *   -c enableTransform=false          index the raw EventBridge envelope
 */
export class EventBridgeOpenSearchStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Accepts one CIDR or a comma-separated list, so several operator
    // addresses can be allowed without widening the range.
    const dashboardAccessIpRaw = this.node.tryGetContext('dashboardAccessIp') as string | undefined;
    const dashboardAccessIps = dashboardAccessIpRaw
      ? dashboardAccessIpRaw
          .split(',')
          .map((cidr) => cidr.trim())
          .filter((cidr) => cidr.length > 0)
      : [];

    // Transform is on by default; it is what makes the data pleasant to query.
    const enableTransform = this.node.tryGetContext('enableTransform') !== 'false';

    const domainName = 'event-monitor';
    const indexName = 'events';

    // The domain ARN is built by hand rather than read off the Domain
    // construct. The domain's own access policy has to name the Firehose
    // role, and the Firehose role's policy has to name the domain -- going
    // through the construct in both directions would be a circular
    // reference. The name is fixed, so the ARN is knowable up front.
    const domainArn = this.formatArn({
      service: 'es',
      resource: 'domain',
      resourceName: domainName,
    });

    // -------------------------------------------------------------------
    // 1. EventBridge custom bus
    // -------------------------------------------------------------------
    const eventBus = new events.EventBus(this, 'EventMonitorBus', {
      eventBusName: 'event-monitor-bus',
    });

    // -------------------------------------------------------------------
    // 2. S3 backup bucket
    //
    // Firehose requires an S3 configuration on the OpenSearch destination
    // even when backing up only failures, so this bucket is not optional.
    // -------------------------------------------------------------------
    const backupBucket = new s3.Bucket(this, 'BackupBucket', {
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      enforceSSL: true,
      lifecycleRules: [
        {
          id: 'archive-then-expire',
          transitions: [
            {
              storageClass: s3.StorageClass.GLACIER,
              transitionAfter: cdk.Duration.days(30),
            },
          ],
          expiration: cdk.Duration.days(365),
        },
      ],
      // Demo pattern: leave nothing behind on `cdk destroy`.
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // -------------------------------------------------------------------
    // 3. Firehose delivery role
    //
    // Created before the domain so the domain access policy can name it.
    // Its permissions are attached further down, once the resources it
    // needs to reach actually exist.
    // -------------------------------------------------------------------
    const firehoseRole = new iam.Role(this, 'FirehoseDeliveryRole', {
      assumedBy: new iam.ServicePrincipal('firehose.amazonaws.com'),
      description: 'Lets Firehose deliver EventBridge events to OpenSearch and back them up to S3',
    });

    // -------------------------------------------------------------------
    // 4. OpenSearch domain
    // -------------------------------------------------------------------
    const domainAccessPolicies = [
      // Firehose delivery role: write documents and read index metadata.
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        principals: [new iam.ArnPrincipal(firehoseRole.roleArn)],
        actions: ['es:ESHttpPost', 'es:ESHttpPut', 'es:ESHttpGet', 'es:ESHttpHead'],
        resources: [domainArn, `${domainArn}/*`],
      }),
    ];

    if (dashboardAccessIps.length > 0) {
      // Dashboards runs in a browser, which cannot SigV4-sign requests.
      // Anonymous access narrowed to known CIDRs is the standard way in when
      // fine-grained access control is off.
      domainAccessPolicies.push(
        new iam.PolicyStatement({
          effect: iam.Effect.ALLOW,
          principals: [new iam.AnyPrincipal()],
          actions: ['es:ESHttp*'],
          resources: [domainArn, `${domainArn}/*`],
          conditions: {
            IpAddress: { 'aws:SourceIp': dashboardAccessIps },
          },
        }),
      );
    }

    const domain = new opensearch.Domain(this, 'EventMonitorDomain', {
      domainName,
      version: opensearch.EngineVersion.OPENSEARCH_2_19,
      capacity: {
        dataNodes: 1,
        dataNodeInstanceType: 't3.small.search',
        // t3 instance types cannot run Multi-AZ with standby, and CDK
        // turns it on by default. Leaving this unset fails synthesis.
        multiAzWithStandbyEnabled: false,
      },
      ebs: {
        volumeSize: 20,
        volumeType: ec2.EbsDeviceVolumeType.GP3,
      },
      // Single node, so no zone awareness and no dedicated master.
      zoneAwareness: { enabled: false },
      enforceHttps: true,
      nodeToNodeEncryption: true,
      encryptionAtRest: { enabled: true },
      accessPolicies: domainAccessPolicies,
      logging: {
        appLogEnabled: true,
        appLogGroup: new logs.LogGroup(this, 'DomainAppLogs', {
          retention: logs.RetentionDays.ONE_WEEK,
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
      },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // -------------------------------------------------------------------
    // 5. Transform Lambda (flattens the EventBridge envelope)
    // -------------------------------------------------------------------
    let transformFn: lambda.Function | undefined;

    if (enableTransform) {
      transformFn = new lambda.Function(this, 'TransformFunction', {
        functionName: 'event-monitor-transform',
        runtime: lambda.Runtime.PYTHON_3_12,
        handler: 'handler.handler',
        code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'src', 'transform')),
        // Firehose gives a transform 60s before it counts as a failure.
        timeout: cdk.Duration.seconds(60),
        memorySize: 256,
        description: 'Flattens the EventBridge envelope before documents are indexed in OpenSearch',
        logGroup: new logs.LogGroup(this, 'TransformLogs', {
          retention: logs.RetentionDays.ONE_WEEK,
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
      });
    }

    // -------------------------------------------------------------------
    // 6. Firehose error logging
    //
    // Delivery failures surface nowhere else -- without this, a rejected
    // document is invisible.
    // -------------------------------------------------------------------
    const firehoseLogGroup = new logs.LogGroup(this, 'FirehoseLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const openSearchLogStream = new logs.LogStream(this, 'OpenSearchDeliveryLogStream', {
      logGroup: firehoseLogGroup,
      logStreamName: 'OpenSearchDelivery',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const backupLogStream = new logs.LogStream(this, 'BackupDeliveryLogStream', {
      logGroup: firehoseLogGroup,
      logStreamName: 'BackupDelivery',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // -------------------------------------------------------------------
    // 7. Firehose delivery role permissions
    // -------------------------------------------------------------------
    // es:ESHttp* writes the documents. The Describe* actions are separate
    // and easy to miss: Firehose calls them to resolve the domain endpoint
    // before it can deliver anything, and `grantIndexWrite` does not
    // include them.
    firehoseRole.addToPolicy(
      new iam.PolicyStatement({
        sid: 'OpenSearchDescribe',
        actions: ['es:DescribeDomain', 'es:DescribeDomainConfig', 'es:DescribeDomains'],
        resources: [domainArn],
      }),
    );

    firehoseRole.addToPolicy(
      new iam.PolicyStatement({
        sid: 'OpenSearchWrite',
        actions: ['es:ESHttpPost', 'es:ESHttpPut', 'es:ESHttpGet'],
        resources: [domainArn, `${domainArn}/*`],
      }),
    );

    backupBucket.grantWrite(firehoseRole);
    firehoseRole.addToPolicy(
      new iam.PolicyStatement({
        sid: 'S3BackupRead',
        actions: ['s3:GetBucketLocation', 's3:ListBucket', 's3:ListBucketMultipartUploads'],
        resources: [backupBucket.bucketArn],
      }),
    );

    firehoseRole.addToPolicy(
      new iam.PolicyStatement({
        sid: 'FirehoseErrorLogging',
        actions: ['logs:PutLogEvents'],
        resources: [firehoseLogGroup.logGroupArn, `${firehoseLogGroup.logGroupArn}:*`],
      }),
    );

    if (transformFn) {
      firehoseRole.addToPolicy(
        new iam.PolicyStatement({
          sid: 'InvokeTransform',
          actions: ['lambda:InvokeFunction', 'lambda:GetFunctionConfiguration'],
          resources: [transformFn.functionArn, `${transformFn.functionArn}:*`],
        }),
      );
    }

    // -------------------------------------------------------------------
    // 8. Firehose delivery stream
    //
    // L1 by design: the L2 DeliveryStream only accepts destinations that
    // implement IDestination, and the only one shipped is S3. OpenSearch
    // has to be configured through CfnDeliveryStream.
    // -------------------------------------------------------------------
    const deliveryStreamName = 'event-monitor-stream';

    const cfnStream = new firehose.CfnDeliveryStream(this, 'EventDeliveryStream', {
      deliveryStreamName,
      deliveryStreamType: 'DirectPut',
      amazonopensearchserviceDestinationConfiguration: {
        // Combined with OneDay rotation this yields events-YYYY-MM-DD.
        indexName,
        indexRotationPeriod: 'OneDay',
        // domainArn and clusterEndpoint are mutually exclusive.
        domainArn: domain.domainArn,
        roleArn: firehoseRole.roleArn,
        // 60s / 1MB is the floor Firehose allows, and it sets the
        // end-to-end latency of this pattern.
        bufferingHints: {
          intervalInSeconds: 60,
          sizeInMBs: 1,
        },
        retryOptions: {
          durationInSeconds: 300,
        },
        // AllDocuments keeps a durable copy of everything indexed, which
        // makes the S3 bucket an audit trail rather than just a dead
        // letter destination.
        s3BackupMode: 'AllDocuments',
        s3Configuration: {
          bucketArn: backupBucket.bucketArn,
          roleArn: firehoseRole.roleArn,
          prefix: 'events/',
          errorOutputPrefix: 'errors/',
          bufferingHints: {
            intervalInSeconds: 300,
            sizeInMBs: 5,
          },
          compressionFormat: 'GZIP',
          cloudWatchLoggingOptions: {
            enabled: true,
            logGroupName: firehoseLogGroup.logGroupName,
            logStreamName: backupLogStream.logStreamName,
          },
        },
        cloudWatchLoggingOptions: {
          enabled: true,
          logGroupName: firehoseLogGroup.logGroupName,
          logStreamName: openSearchLogStream.logStreamName,
        },
        processingConfiguration: transformFn
          ? {
              enabled: true,
              processors: [
                {
                  type: 'Lambda',
                  parameters: [
                    { parameterName: 'LambdaArn', parameterValue: transformFn.functionArn },
                    { parameterName: 'RoleArn', parameterValue: firehoseRole.roleArn },
                    // Lambda processor buffer must stay within 0.2-3 MB.
                    { parameterName: 'BufferSizeInMBs', parameterValue: '1' },
                    { parameterName: 'BufferIntervalInSeconds', parameterValue: '60' },
                    { parameterName: 'NumberOfRetries', parameterValue: '3' },
                  ],
                },
              ],
            }
          : undefined,
      },
    });

    // The stream is only usable once the role's policies are attached and
    // the domain access policy has been applied. Neither shows up as a
    // CloudFormation reference, so the ordering has to be explicit.
    cfnStream.node.addDependency(firehoseRole);
    cfnStream.node.addDependency(domain);

    // -------------------------------------------------------------------
    // 9. Catch-all EventBridge rule
    // -------------------------------------------------------------------
    // Wrapping the L1 stream as an L2 lets the event target construct
    // build the rule's IAM role for us.
    const deliveryStream = firehose.DeliveryStream.fromDeliveryStreamArn(
      this,
      'ImportedDeliveryStream',
      cfnStream.attrArn,
    );

    const rule = new events.Rule(this, 'CatchAllRule', {
      eventBus,
      ruleName: 'event-monitor-catch-all',
      description: 'Captures every event on the bus and streams it to OpenSearch via Data Firehose',
      // Every event carries a source, so an empty prefix matches all of
      // them. An empty event pattern is rejected by EventBridge.
      eventPattern: {
        source: events.Match.prefix(''),
      },
    });

    rule.addTarget(new targets.FirehoseDeliveryStream(deliveryStream));

    // Imported constructs carry no dependency edge of their own.
    rule.node.addDependency(cfnStream);

    // -------------------------------------------------------------------
    // Outputs
    // -------------------------------------------------------------------
    new cdk.CfnOutput(this, 'DashboardsUrl', {
      value: `https://${domain.domainEndpoint}/_dashboards/`,
      description:
        dashboardAccessIps.length > 0
          ? `OpenSearch Dashboards URL (reachable from: ${dashboardAccessIps.join(', ')})`
          : 'OpenSearch Dashboards URL (no public access granted -- redeploy with -c dashboardAccessIp=YOUR_IP/32)',
    });

    new cdk.CfnOutput(this, 'DomainEndpoint', {
      value: domain.domainEndpoint,
      description: 'OpenSearch domain endpoint',
    });

    new cdk.CfnOutput(this, 'EventBusName', {
      value: eventBus.eventBusName,
      description: 'EventBridge custom bus being monitored',
    });

    new cdk.CfnOutput(this, 'DeliveryStreamName', {
      value: deliveryStreamName,
      description: 'Firehose delivery stream carrying events to OpenSearch',
    });

    new cdk.CfnOutput(this, 'BackupBucketName', {
      value: backupBucket.bucketName,
      description: 'S3 bucket holding the event backup and any delivery failures',
    });

    new cdk.CfnOutput(this, 'FirehoseLogGroup', {
      value: firehoseLogGroup.logGroupName,
      description: 'CloudWatch log group for Firehose delivery errors',
    });

    new cdk.CfnOutput(this, 'IndexPattern', {
      value: `${indexName}-*`,
      description: 'Index pattern to create in OpenSearch Dashboards (time field: time)',
    });
  }
}
