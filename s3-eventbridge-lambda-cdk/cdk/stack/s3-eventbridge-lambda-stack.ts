import { CfnOutput, Duration, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, 'sample-eventbridge-bucket', {
      eventBridgeEnabled: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: RemovalPolicy.DESTROY
    });

    const s3ObjectTaggingStatement = new iam.PolicyStatement({
      actions: ['s3:PutObjectTagging'],
      resources: [`${bucket.bucketArn}/*`]
    });

    const lambdaFn = new lambda.Function(this, 's3-event-processor', {
      runtime: lambda.Runtime.NODEJS_14_X,
      handler: 'lambda.handler',
      code: lambda.Code.fromAsset('src'),
      functionName: 's3-event-processor',
      memorySize: 256,
      timeout: Duration.seconds(30)
    });

    lambdaFn.addToRolePolicy(s3ObjectTaggingStatement);
    lambdaFn.role?.attachInlinePolicy(
      new iam.Policy(this, 's3-object-tagging-policy', {
        statements: [s3ObjectTaggingStatement],
      }),
    );

    const rule = new events.Rule(this, 'rule', {
      eventPattern: {
        source: ['aws.s3'],
        detailType: [
          'Object Created'
        ],
        detail: {
          bucket: {
            name: [
              bucket.bucketName
            ]
          }
        }
      },
    });

    rule.addTarget(new targets.LambdaFunction(lambdaFn, {
      maxEventAge: Duration.hours(2),
      retryAttempts: 3
    }));

    new CfnOutput(this, 'S3BucketName', { value: bucket.bucketName });
    new CfnOutput(this, 'LambdaFunctionARN', { value: lambdaFn.functionArn });
    new CfnOutput(this, 'EventBridgeRuleARN', { value: rule.ruleArn });
    
  }
}
