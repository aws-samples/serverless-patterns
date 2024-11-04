import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class SrcStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // get account id
    const account = cdk.Stack.of(this).account;

    // create an SQS source queue starting with account id
    const srcQueue = new cdk.aws_sqs.Queue(this, 'SrcQueue', {
      queueName: `${account}-src-queue`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // create a destination queue starting with account id, of type FIFO
    const destQueue = new cdk.aws_sqs.Queue(this, 'DestQueue', {
      queueName: `${account}-dest-queue.fifo`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      fifo: true,
    });

    // create a dynamodb table to aggregate messages
    const srcTable = new cdk.aws_dynamodb.Table(this, 'SrcTable', {
      partitionKey: { name: 'id', type: cdk.aws_dynamodb.AttributeType.STRING },
      sortKey: { name: 'correlationId', type: cdk.aws_dynamodb.AttributeType.STRING },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      tableName: `${account}-events-table`
    });

    // create a local secondary index for dynamo, based on correlationId
    srcTable.addLocalSecondaryIndex({
      indexName: 'correlationIdIndex',
      sortKey: { name: 'correlationId', type: cdk.aws_dynamodb.AttributeType.STRING },
    });
    // create a local secondary index for dynamo, based on order field
    srcTable.addLocalSecondaryIndex({
      indexName: 'orderIndex',
      sortKey: { name: 'order', type: cdk.aws_dynamodb.AttributeType.NUMBER },
    });

    // create a lambda using the file code/lambda.handler.js
    const srcLambda = new cdk.aws_lambda.Function(this, 'SrcLambda', {
      code: cdk.aws_lambda.Code.fromAsset('code'),
      handler: 'handler.handler',
      runtime: cdk.aws_lambda.Runtime.NODEJS_14_X,
      environment: {
        DYNAMODB_TABLE_NAME: srcTable.tableName,
        DESTINATION_QUEUE_URL: destQueue.queueUrl,
      },
      functionName: `${account}-aggregator-lambda`
    });

    // grant permissions
    srcQueue.grantConsumeMessages(srcLambda);
    srcTable.grantReadWriteData(srcLambda);
    destQueue.grantSendMessages(srcLambda);

    // register src queue as a trigger of the lambda
    srcLambda.addEventSource(new cdk.aws_lambda_event_sources.SqsEventSource(srcQueue, { batchSize: 1 }));

    // output the source queue
    new cdk.CfnOutput(this, 'SrcQueueOutput', { value: srcQueue.queueName });
    new cdk.CfnOutput(this, 'DestQueueOutput', { value: destQueue.queueName });

    // output the dynamoDB
    new cdk.CfnOutput(this, 'DynamoDBOutput', { value: srcTable.tableName });
  }
}
