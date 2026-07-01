import * as cdk from 'aws-cdk-lib';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as destinations from 'aws-cdk-lib/aws-lambda-destinations';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as cloudtrail from 'aws-cdk-lib/aws-cloudtrail';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';

export class EventbridgeCloudtrailDataplaneStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 access logs bucket
    const accessLogsBucket = new s3.Bucket(this, 'AccessLogsBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      enforceSSL: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    });

    // S3 bucket for CloudTrail logs
    const trailBucket = new s3.Bucket(this, 'TrailBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      enforceSSL: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      serverAccessLogsBucket: accessLogsBucket,
      serverAccessLogsPrefix: 'trail-bucket-logs/',
    });

    // CloudTrail trail with data events for EventBridge
    const trail = new cloudtrail.Trail(this, 'EventBridgeDataPlaneTrail', {
      bucket: trailBucket,
      isMultiRegionTrail: true,
    });

    // Enable EventBridge data plane events logging using advanced event selectors.
    // CDK L2 addEventSelector only supports S3/Lambda/DynamoDB basic selectors,
    // so we use the CfnTrail escape hatch for AWS::Events::EventBus.
    const cfnTrail = trail.node.defaultChild as cloudtrail.CfnTrail;
    cfnTrail.addPropertyOverride('AdvancedEventSelectors', [
      {
        Name: 'Log EventBridge PutEvents data events',
        FieldSelectors: [
          { Field: 'eventCategory', Equals: ['Data'] },
          { Field: 'resources.type', Equals: ['AWS::Events::EventBus'] },
        ],
      },
    ]);

    // DLQ for EventBridge target and Lambda async failures
    const dlq = new sqs.Queue(this, 'TargetDLQ', {
      retentionPeriod: cdk.Duration.days(14),
    });

    // Lambda function to process CloudTrail events
    const processor = new lambda.Function(this, 'EventProcessor', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(10),
      loggingFormat: lambda.LoggingFormat.JSON,
      logRetention: logs.RetentionDays.ONE_WEEK,
      retryAttempts: 2,
      onFailure: new destinations.SqsDestination(dlq),
    });

    // EventBridge rule to capture EventBridge PutEvents API calls from CloudTrail
    const rule = new events.Rule(this, 'DataPlaneRule', {
      eventPattern: {
        source: ['aws.events'],
        detailType: ['AWS API Call via CloudTrail'],
        detail: {
          eventSource: ['events.amazonaws.com'],
          eventName: ['PutEvents'],
        },
      },
    });

    rule.addTarget(new targets.LambdaFunction(processor, {
      deadLetterQueue: dlq,
    }));

    new cdk.CfnOutput(this, 'ProcessorFunctionName', { value: processor.functionName });
    new cdk.CfnOutput(this, 'TrailBucketName', { value: trailBucket.bucketName });
    new cdk.CfnOutput(this, 'RuleName', { value: rule.ruleName });
  }
}
