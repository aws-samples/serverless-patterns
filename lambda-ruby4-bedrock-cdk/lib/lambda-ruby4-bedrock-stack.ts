import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

export class LambdaRuby4BedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const fn = new lambda.Function(this, 'Ruby4BedrockFunction', {
      runtime: new lambda.Runtime('ruby4.0', lambda.RuntimeFamily.RUBY),
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      architecture: lambda.Architecture.ARM_64,
      environment: {
        MODEL_ID: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      },
      loggingFormat: lambda.LoggingFormat.JSON,
    });

    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        'arn:aws:bedrock:*::foundation-model/*',
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
      ],
    }));

    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
    new cdk.CfnOutput(this, 'FunctionArn', { value: fn.functionArn });
  }
}
