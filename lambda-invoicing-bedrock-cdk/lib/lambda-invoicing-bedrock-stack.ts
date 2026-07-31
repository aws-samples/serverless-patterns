import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as path from 'path';

export class LambdaInvoicingBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon S3 bucket for invoice PDF archive
    const invoiceBucket = new s3.Bucket(this, 'InvoiceBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      lifecycleRules: [
        {
          transitions: [
            {
              storageClass: s3.StorageClass.INFREQUENT_ACCESS,
              transitionAfter: cdk.Duration.days(90),
            },
          ],
        },
      ],
    });

    // AWS Lambda function for invoice retrieval and Amazon Bedrock analysis
    const invoiceFn = new lambda.Function(this, 'InvoiceFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      timeout: cdk.Duration.minutes(5),
      memorySize: 512,
      environment: {
        BUCKET_NAME: invoiceBucket.bucketName,
        MODEL_ID: this.node.tryGetContext('modelId') || 'us.anthropic.claude-sonnet-4-6',
      },
    });

    // Grant Amazon S3 write access
    invoiceBucket.grantWrite(invoiceFn);

    // Grant Invoicing API access
    invoiceFn.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'invoicing:ListInvoiceSummaries',
        'invoicing:GetInvoicePDF',
      ],
      resources: ['*'],
    }));

    // Grant Amazon Bedrock model invocation
    invoiceFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-6`,
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
      ],
    }));

    // Amazon EventBridge rule - runs on the 2nd of each month (invoices available after month-end)
    const rule = new events.Rule(this, 'MonthlyInvoiceRule', {
      schedule: events.Schedule.cron({ minute: '0', hour: '8', day: '2', month: '*' }),
    });
    rule.addTarget(new targets.LambdaFunction(invoiceFn));

    // Outputs
    new cdk.CfnOutput(this, 'InvoiceBucketName', {
      value: invoiceBucket.bucketName,
      description: 'Amazon S3 bucket storing invoice PDFs and Amazon Bedrock analysis summaries',
    });

    new cdk.CfnOutput(this, 'FunctionName', {
      value: invoiceFn.functionName,
      description: 'AWS Lambda function name for manual invocation',
    });
  }
}
