import { AttributeType, BillingMode, StreamViewType, Table } from '@aws-cdk/aws-dynamodb';
import * as cdk from '@aws-cdk/core';
import { Stream } from '@aws-cdk/aws-kinesis';

export class DynamodbKinesisCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    //Kinesis Data Stream
    const stream = new Stream(this, "KinesisStream", {
      streamName: "kinesis-stream",
      shardCount: 1,
    });

    // DynamoDB table
    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'id', type: AttributeType.STRING},
      kinesisStream: stream,
      readCapacity: 5,
      writeCapacity: 5,
    });

  }
}
