import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as s3 from 'aws-cdk-lib/aws-s3';

export class LambdaBedrockPromptOptimizationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, 'PromptOptBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    const fn = new lambda.Function(this, 'PromptOptFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/lambda', {
        bundling: {
          image: lambda.Runtime.PYTHON_3_12.bundlingImage,
          command: [
            'bash', '-c',
            'pip install -r requirements.txt -t /asset-output && cp -au . /asset-output',
          ],
        },
      }),
      timeout: cdk.Duration.minutes(15),
      memorySize: 256,
      environment: {
        BUCKET_NAME: bucket.bucketName,
      },
    });

    bucket.grantReadWrite(fn);

    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'bedrock:CreateAdvancedPromptOptimizationJob',
        'bedrock:GetAdvancedPromptOptimizationJob',
        'bedrock:ListAdvancedPromptOptimizationJobs',
      ],
      resources: [
        `arn:aws:bedrock:${this.region}:${this.account}:advanced-prompt-optimization-job/*`,
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
        'arn:aws:bedrock:*::foundation-model/*',
      ],
    }));

    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'bedrock:InvokeModel',
        'bedrock:InvokeModelWithResponseStream',
      ],
      resources: [
        'arn:aws:bedrock:*::foundation-model/*',
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
      ],
    }));

    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
    new cdk.CfnOutput(this, 'BucketName', { value: bucket.bucketName });
  }
}
