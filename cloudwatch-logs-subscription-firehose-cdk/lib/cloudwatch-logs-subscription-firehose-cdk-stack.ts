import {
  aws_s3 as s3,
  aws_iam as iam,
  aws_logs as logs,
  CfnOutput,
  RemovalPolicy,
  aws_kinesisfirehose as firehose,
  Stack,
  StackProps
} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';

export class CloudwatchLogsSubscriptionFirehoseCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const myLogsBucket = new s3.Bucket(this, 'MyLogsBucket', {
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const myLogGroup = new logs.LogGroup(this, 'MyLogGroup', {
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.ONE_DAY,
    });

    const myLogStream = new logs.LogStream(this, 'MyLogStream', {
      logGroup: myLogGroup,
      removalPolicy: RemovalPolicy.DESTROY
    });

    const destinationRole = new iam.Role(this, 'Destination Role', {
      assumedBy: new iam.ServicePrincipal('firehose.amazonaws.com'),
    });

    destinationRole.attachInlinePolicy(
      new iam.Policy(this, 'S3Permission', {
        statements: [
          new iam.PolicyStatement({
            actions: [
              's3:AbortMultipartUpload',
              's3:GetBucketLocation',
              's3:GetObject',
              's3:ListBucket',
              's3:ListBucketMultipartUploads',
              's3:PutObject'
            ],
            resources: [myLogsBucket.bucketArn, myLogsBucket.arnForObjects('*')],
          }),
        ],
      }),
    );

    // Firehose delivey stream
    const firehoseDeliveryStream = new firehose.CfnDeliveryStream(this, 'FirehoseDeliveryStream', {
      extendedS3DestinationConfiguration: {
        bucketArn: myLogsBucket.bucketArn,
        roleArn: destinationRole.roleArn,
        bufferingHints: {
          intervalInSeconds: 60,
          sizeInMBs: 1,
        },
      }
    });

    const cwLogIngestionRole = new iam.Role(this, 'cwlogIngestionRole', {
      assumedBy: new iam.ServicePrincipal('logs.' + Stack.of(this).region + '.amazonaws.com'),
    });

    cwLogIngestionRole.attachInlinePolicy(
      new iam.Policy(this, 'putLogsPermission', {
        statements: [
          new iam.PolicyStatement({
            actions: ['firehose:*'],
            resources: ['arn:aws:firehose:' + Stack.of(this).region + ':' + Stack.of(this).account + ':*'],
          }),
        ],
      }),
    );

    // Cloudwatch subscription
    new logs.CfnSubscriptionFilter(this, 'LogGroupSubscription', {
      destinationArn: firehoseDeliveryStream.attrArn,
      filterPattern: "ERROR WARNING",
      logGroupName: myLogGroup.logGroupName,
      roleArn: cwLogIngestionRole.roleArn,
    });

    // Output
    new CfnOutput(this, 'logGroupName', {
      value: myLogGroup.logGroupName,
      description: 'Log group name',
      exportName: 'LogGroupName',
    });

    new CfnOutput(this, 'logStreamName', {
      value: myLogStream.logStreamName,
      description: 'Log stream name',
      exportName: 'LogStreamName',
    });

    new CfnOutput(this, 'S3Bucket', {
      value: myLogsBucket.bucketName,
      description: 'S3Bucket',
      exportName: 'S3Bucket',
    });
  }
}
