import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class SrcStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // get account id
    const account = cdk.Stack.of(this).account;

    // create an sqs queue starting with account id
    const srcSqs = new cdk.aws_sqs.Queue(this, 'SrcQueue', {
      queueName: `${account}-src-queue`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // create the destination queue
    const destSqs = new cdk.aws_sqs.Queue(this, 'DestQueue', {
      queueName: `${account}-dest-queue`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // create a dynamodb table to aggregate messages
    const srcTable = new cdk.aws_dynamodb.Table(this, 'SrcTable', {
      partitionKey: { name: 'id', type: cdk.aws_dynamodb.AttributeType.STRING },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      tableName: `${account}-events-table`
    });

    // create a lambda using the file code/lambda.handler.js
    const srcLambda = new cdk.aws_lambda.Function(this, 'SrcLambda', {
      code: cdk.aws_lambda.Code.fromAsset('code'),
      handler: 'handler.handler',
      runtime: cdk.aws_lambda.Runtime.NODEJS_14_X,
      environment: {
        DYNAMODB_TABLE_NAME: srcTable.tableName,
        DESTINATION_QUEUE_URL: destSqs.queueUrl,
      },
      functionName: `${account}-aggregator-lambda`
    });

    // grant permissions
    srcSqs.grantConsumeMessages(srcLambda);
    srcTable.grantReadWriteData(srcLambda);
    destSqs.grantSendMessages(srcLambda);

    // register src queue as a trigger of the lambda
    srcLambda.addEventSource(new cdk.aws_lambda_event_sources.SqsEventSource(srcSqs, { batchSize: 10 }));
  }
}
