import * as path from 'path';
import { Construct } from 'constructs';
import { aws_s3 as s3 } from 'aws-cdk-lib';
import { aws_sns as sns } from 'aws-cdk-lib';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { aws_lambda as lambda } from 'aws-cdk-lib';
import { aws_kinesisvideo as kvs } from 'aws-cdk-lib';
import { aws_iam as iam, CfnOutput } from 'aws-cdk-lib';
import { aws_rekognition as rekognition } from 'aws-cdk-lib';
import { SnsEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';

export class KvsRekognitionStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const event_storage = new s3.Bucket(this, 'event-storage-bucket');

    const inputKinesisVideoStream = new kvs.CfnStream(this, 'input-video-stream', {
      dataRetentionInHours: 1,
      name: 'input-video-stream'
    });

    const connectedHomeEventNotification = new sns.Topic(this, 'connected-home-topic', {
     topicName: 'connected-home-topic',
     displayName: 'Connected_Home_Notifications' 
    })

    const streamProcessorPolicy = new iam.Policy(this, 'kinesis-video-read', {
      statements: [
        new iam.PolicyStatement({
          actions: [
            'kinesisvideo:GetDataEndpoint',
            'kinesisvideo:GetMedia'
          ],
          resources: [
            inputKinesisVideoStream.attrArn
          ],
        }),
        new iam.PolicyStatement({
          actions: [
            'sns:Publish'
          ],
          resources: [
            connectedHomeEventNotification.topicArn
          ]
        }),
        new iam.PolicyStatement({
          actions:[
            's3:PutObject'
          ],
          resources: [
            event_storage.bucketArn
          ]
        })
      ],
    });

    const streamProcessorRole = new iam.Role(this, 'stream-processor-role', {
      assumedBy: new iam.ServicePrincipal('rekognition.amazonaws.com'),
      description: 'Service role for Rekognition Stream Processor to ingest from KVS and output to Kinesis Data Streams'
    });

    // Attaches our least privillege policy to our service role for rekognition stream processor
    streamProcessorPolicy.attachToRole(streamProcessorRole);

    const rekognitionStreamProcessor = new rekognition.CfnStreamProcessor(this, 'MyCfnStreamProcessor', {
      kinesisVideoStream: {
        arn: inputKinesisVideoStream.attrArn,
      },
      roleArn: streamProcessorRole.roleArn,
      name: `${ inputKinesisVideoStream.name }-stream-processor`,
      connectedHomeSettings: {
        'labels': [
          "PET",
          "PERSON"
        ],
        'minConfidence': 80
      },
      notificationChannel: {
        arn: connectedHomeEventNotification.topicArn
      },
      s3Destination: {
        bucketName: event_storage.bucketName,
      }
    });

    const processingLambda = new lambda.Function(this, 'processing-lambda', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'index.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, 'lambda/'))
    });

    // deliver all notification from topic to our lambda
    const processingSource = new SnsEventSource(connectedHomeEventNotification);

    processingLambda.addEventSource(processingSource);

    new CfnOutput(this, 'Rekognition Stream Processor', { value: rekognitionStreamProcessor.name! })
  }
}
