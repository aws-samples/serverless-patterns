import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as sqsevts from 'aws-cdk-lib/aws-lambda-event-sources';
import * as iam from 'aws-cdk-lib/aws-iam'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

export class MyCdkProjectStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
     // Create an S3 bucket
    const bucket = new s3.Bucket(this, 'MyBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Create an SQS queue
    const queue = new sqs.Queue(this, 'MyQueue', {
      visibilityTimeout: cdk.Duration.seconds(300),
    });

    // Add S3 object created event notification to the SQS queue
    bucket.addObjectCreatedNotification(new s3n.SqsDestination(queue));
    
    // Create DynamoDB table
    const table = new dynamodb.Table(this, 'EmployeeInfoTable', {
      tableName: 'employeeInfoNew',
      partitionKey: { name: 'email', type: dynamodb.AttributeType.STRING },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    
    // Create a Lambda function
    const lambdaFn = new lambda.Function(this, 'MyLambdaFunction', {
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: 'index.lambda_handler',
      code: lambda.Code.fromAsset('lambda'),
    });

    // Add SQS queue as an event source for the Lambda function
    lambdaFn.addEventSource(new sqsevts.SqsEventSource(queue));
    
        // Grant S3 read permission to the Lambda function
    const s3ReadWritePolicy = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['s3:GetObject'],
      resources: [bucket.bucketArn + '/*'],
    });
    lambdaFn.addToRolePolicy(s3ReadWritePolicy);
    
    // Grant read/write permissions to the DynamoDB table
    table.grantReadWriteData(lambdaFn);
    
    // Output the resource names
    new cdk.CfnOutput(this, 'BucketNameOutput', {
      value: bucket.bucketName,
      description: 'S3 Bucket Name',
    });
    new cdk.CfnOutput(this, 'QueueNameOutput', {
      value: queue.queueName,
      description: 'SQS Queue Name',
    });
    new cdk.CfnOutput(this, 'TableNameOutput', {
      value: table.tableName,
      description: 'DynamoDB Table Name',
    });
    new cdk.CfnOutput(this, 'FunctionNameOutput', {
      value: lambdaFn.functionName,
      description: 'Lambda Function Name',
    });


  }
}
