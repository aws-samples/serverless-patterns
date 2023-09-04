import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';
import { Function, AssetCode, Architecture } from 'aws-cdk-lib/aws-lambda';
import { Runtime, StartingPosition } from 'aws-cdk-lib/aws-lambda';
import { Stream } from 'aws-cdk-lib/aws-kinesis';
import { KinesisEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';


export class AppStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const prefix = 'test-';

    const kStream = new Stream(this, prefix + 'Kinesis-Stream', {
      streamName: prefix + 'KinesisLambda-Stream',
      retentionPeriod: cdk.Duration.days(7),
      shardCount: 1,
    });

    // write lambda cdk construct to pick from lambda_code folder
    const lambdaFn = new Function(this, prefix + 'Lambda-Function', {
      functionName: prefix + 'KinesisLambda-Function',
      runtime: Runtime.NODEJS_18_X,
      handler: 'app.lambdaHandler',
      code: new AssetCode(path.join(__dirname, '../lambda_code')),
      environment: {
        'STREAM_NAME': prefix + 'KinesisLambda-Stream',
        'STRAM_ARN': kStream.streamArn,
      },
      architecture: Architecture.ARM_64,
      memorySize: 128,
      logRetention: RetentionDays.FIVE_DAYS,
    });

    // add lambda eventsouce to lambdaFn with kinesis stream
    lambdaFn.addEventSource(new KinesisEventSource(kStream, {
      startingPosition: StartingPosition.TRIM_HORIZON,
      batchSize: 1,
      maxBatchingWindow: cdk.Duration.seconds(1),
      bisectBatchOnError: false,
      retryAttempts: 0,
      maxRecordAge: cdk.Duration.seconds(120),
      enabled: true,
      parallelizationFactor: 1,
      reportBatchItemFailures: false,
    }));
  }
}