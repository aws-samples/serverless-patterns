import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { RustFunction } from 'cargo-lambda-cdk';

export class BedrockStreamerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Rust Lambda Function
    const streamingLambda = new RustFunction(this, 'BedrockStreamerURL', {
      manifestPath: 'lib/bedrock-streamer-lambda/Cargo.toml',
      bundling: {
        architecture: lambda.Architecture.ARM_64,
        cargoLambdaFlags: [
          '--compiler',
          'cross',
          '--release',
        ],
      },
      timeout: cdk.Duration.seconds(60),
    });

    // Create a Lambda Function URL
    const lambdaUrl = streamingLambda.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.AWS_IAM,
      invokeMode: lambda.InvokeMode.RESPONSE_STREAM,
    });

    // Grant Lambda permission to invoke Bedrock
    streamingLambda.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModelWithResponseStream'],
      resources: ['*'],
    }));

    // Output the Lambda Function URL
    new cdk.CfnOutput(this, 'LambdaFunctionURL', {
      value: lambdaUrl.url,
      description: 'Lambda Function URL',
    });
    
  }
}