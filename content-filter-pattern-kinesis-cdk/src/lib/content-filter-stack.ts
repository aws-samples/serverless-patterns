import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as kinesis from 'aws-cdk-lib/aws-kinesis';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as iam from 'aws-cdk-lib/aws-iam';

export class ContentFilterStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const sourceStream = new kinesis.Stream(this, 'FilterSourceStream', {
      encryption: kinesis.StreamEncryption.MANAGED,
    });
    const targetStream = new kinesis.Stream(this, 'FilterTargetStream', {
      encryption: kinesis.StreamEncryption.MANAGED,
    });

    // create IAM role with permission to read from sourceStream and write to targetStream
    const pipeRole = new iam.Role(this, 'FilterPipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });
    sourceStream.grantRead(pipeRole);
    targetStream.grantWrite(pipeRole);

    // create an Amazon EventBridge Pipe which connects sourceStream to targetStream and 
    //  - filters to only forward events with event_type = ORDER
    //  - transforms the event to only include event_type, currency, and sum
    const filterPipe = new pipes.CfnPipe(this, 'FilterPipe', {
      roleArn: pipeRole.roleArn,
      source: sourceStream.streamArn,
      target: targetStream.streamArn,
      sourceParameters: {
        filterCriteria: {
          filters: [{
            pattern: '{"data" : {"event_type" : ["ORDER"] }}',
          }],
        },
        kinesisStreamParameters: {
          startingPosition: "LATEST",
        },
      },
      targetParameters: {
        inputTemplate: '{"event_type": <$.data.event_type>, "currency": <$.data.currency>, "sum": <$.data.sum>}',
        kinesisStreamParameters: {
          partitionKey: 'event_type',
        },
      },
    });

    // AWS Lambda function that writes to the SourceStream to easily test the pipe
    const sourceLambda = new lambda.Function(this, 'ContentFilterTestLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'contentFilterSampleDataCreator.handler',
      environment: {
        SOURCE_STREAM: sourceStream.streamName
      }
    });
    sourceStream.grantWrite(sourceLambda);

    // Relevant outputs so that the user can trigger this pattern and watch it in action.
    new cdk.CfnOutput(this, "ContentFilterTestLambdaArn", {
      value: sourceLambda.functionArn,
      exportName: "ContentFilterTestLambdaArn",
      description: "The ARN of the Lambda function that can be used to test the Content Filter Pipe. Invoke this function to see the pipe in action.",
    });
    new cdk.CfnOutput(this, "SourceStreamArn", {
      value: sourceStream.streamArn,
      exportName: "sourceStreamArn",
      description: "The ARN of the source stream for the Content Filter Pipe. On this stream, you will find two records per ContentFilterTestLambda-execution, including PII-data.",
    });
    new cdk.CfnOutput(this, "TargetStreamArn", {
      value: targetStream.streamArn,
      exportName: "targetStreamArn",
      description: "The ARN of the target stream for the Content Filter Pipe. On this stream, you will find only one record per ContentFilterTestLambda-execution, and no PII-data.",
    });
  }
}
