import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as path from 'path';

export class PatternStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket for document uploads
    const documentBucket = new s3.Bucket(this, 'DocumentBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
    });

    // DynamoDB table for processing results
    const resultsTable = new dynamodb.Table(this, 'ResultsTable', {
      partitionKey: { name: 'documentKey', type: dynamodb.AttributeType.STRING },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
    });

    // CloudWatch Log Group for the durable function
    const logGroup = new logs.LogGroup(this, 'ProcessorLogGroup', {
      logGroupName: `/aws/lambda/doc-processor-durable`,
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Durable Lambda function for document processing
    const processorFunction = new lambda.Function(this, 'ProcessorFunction', {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'processor.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../lambda')),
      timeout: cdk.Duration.minutes(15),
      memorySize: 512,
      logGroup,
      environment: {
        RESULTS_TABLE_NAME: resultsTable.tableName,
        DOCUMENT_BUCKET_NAME: documentBucket.bucketName,
        BEDROCK_MODEL_ID: 'us.amazon.nova-lite-v1:0',
      },
    });

    // Enable durable execution via L1 escape hatch
    const cfnFunction = processorFunction.node.defaultChild as cdk.CfnResource;
    cfnFunction.addPropertyOverride('DurableConfig', {
      ExecutionTimeout: 3600,       // 1 hour max execution time
      RetentionPeriodInDays: 3,     // Keep execution state for 3 days
    });

    // Grant the durable execution managed policy
    processorFunction.role?.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        'service-role/AWSLambdaBasicDurableExecutionRolePolicy'
      )
    );

    // Grant S3 read access for Textract and the Lambda function
    documentBucket.grantRead(processorFunction);

    // Grant DynamoDB write access
    resultsTable.grantWriteData(processorFunction);

    // Grant Amazon Textract permissions
    // Textract does not support resource-level permissions — wildcard is required.
    // Actions are scoped to only the two operations needed by this handler.
    // See: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontextract.html
    processorFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'textract:StartDocumentTextDetection',
        'textract:GetDocumentTextDetection',
      ],
      resources: ['*'],
    }));

    // Grant Amazon Bedrock invoke model permission
    // Cross-region inference profiles route to any region in the geo area,
    // so we allow the foundation model in all regions via wildcard
    processorFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:*::foundation-model/amazon.nova-lite-v1:0`,
        `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/eu.amazon.nova-lite-v1:0`,
      ],
    }));

    // Create a version and alias for durable function invocation
    // Durable functions require qualified ARNs (version or alias)
    const version = processorFunction.currentVersion;
    const alias = new lambda.Alias(this, 'ProcessorAlias', {
      aliasName: 'live',
      version,
    });

    // S3 event notification triggers the durable Lambda alias on object creation
    documentBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(alias),
      { suffix: '.pdf' }
    );

    documentBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(alias),
      { suffix: '.png' }
    );

    documentBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(alias),
      { suffix: '.jpg' }
    );

    // Outputs
    new cdk.CfnOutput(this, 'DocumentBucketName', {
      value: documentBucket.bucketName,
      description: 'S3 bucket for document uploads',
    });

    new cdk.CfnOutput(this, 'ResultsTableName', {
      value: resultsTable.tableName,
      description: 'DynamoDB table for processing results',
    });

    new cdk.CfnOutput(this, 'ProcessorFunctionName', {
      value: processorFunction.functionName,
      description: 'Durable Lambda function name',
    });

    new cdk.CfnOutput(this, 'ProcessorFunctionArn', {
      value: processorFunction.functionArn,
      description: 'Durable Lambda function ARN',
    });
  }
}
