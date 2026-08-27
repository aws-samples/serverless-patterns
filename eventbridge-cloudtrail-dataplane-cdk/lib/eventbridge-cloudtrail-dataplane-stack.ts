import * as cdk from 'aws-cdk-lib';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as cloudtrail from 'aws-cdk-lib/aws-cloudtrail';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class EventbridgeCloudtrailDataplaneStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket for CloudTrail logs
    const trailBucket = new s3.Bucket(this, 'TrailBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      enforceSSL: true,
    });

    // CloudTrail trail with data events for EventBridge
    const trail = new cloudtrail.Trail(this, 'EventBridgeDataPlaneTrail', {
      bucket: trailBucket,
      trailName: 'eventbridge-dataplane-trail',
      isMultiRegionTrail: false,
    });

    // Enable EventBridge data plane events logging
    trail.addEventSelector(cloudtrail.DataResourceType.LAMBDA_FUNCTION, ['arn:aws:lambda']);

    // Lambda function to process CloudTrail events
    const processor = new lambda.Function(this, 'EventProcessor', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(10),
      loggingFormat: lambda.LoggingFormat.JSON,
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

    rule.addTarget(new targets.LambdaFunction(processor));

    new cdk.CfnOutput(this, 'ProcessorFunctionName', { value: processor.functionName });
    new cdk.CfnOutput(this, 'TrailBucketName', { value: trailBucket.bucketName });
    new cdk.CfnOutput(this, 'RuleName', { value: rule.ruleName });
  }
}
