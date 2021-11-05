import * as cdk from '@aws-cdk/core';
import * as sqs from '@aws-cdk/aws-sqs';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const sqsQueue = new sqs.Queue(this, 'Queue', {
      encryption: sqs.QueueEncryption.KMS_MANAGED,
    });
  }
}
