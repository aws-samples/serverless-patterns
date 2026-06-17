import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as path from 'path';

export class S3LambdaBedrockAnnotationsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket with EventBridge notifications enabled
    const bucket = new s3.Bucket(this, 'AnnotationsBucket', {
      eventBridgeEnabled: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // Lambda layer with latest boto3 (required for put_object_annotation)
    const boto3Layer = new lambda.LayerVersion(this, 'Boto3Layer', {
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src', 'boto3-layer')),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_12],
      description: 'boto3 >= 1.43.31 with S3 Annotations support',
    });

    // Lambda function
    const annotator = new lambda.Function(this, 'AnnotatorFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src', 'annotator')),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      layers: [boto3Layer],
      environment: {
        BUCKET_NAME: bucket.bucketName,
      },
    });

    // IAM permissions: read S3 objects, write annotations, invoke Bedrock
    bucket.grantRead(annotator);
    annotator.addToRolePolicy(new iam.PolicyStatement({
      actions: ['s3:PutObjectAnnotation'],
      resources: [bucket.arnForObjects('*')],
    }));
    annotator.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        'arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-20250514-v1:0',
        `arn:aws:bedrock:*:${this.account}:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0`,
      ],
    }));

    // EventBridge rule: trigger on S3 Object Created
    const rule = new events.Rule(this, 'S3ObjectCreatedRule', {
      eventPattern: {
        source: ['aws.s3'],
        detailType: ['Object Created'],
        detail: {
          bucket: { name: [bucket.bucketName] },
        },
      },
    });
    rule.addTarget(new targets.LambdaFunction(annotator));

    // Outputs
    new cdk.CfnOutput(this, 'BucketName', { value: bucket.bucketName });
    new cdk.CfnOutput(this, 'FunctionName', { value: annotator.functionName });
  }
}
