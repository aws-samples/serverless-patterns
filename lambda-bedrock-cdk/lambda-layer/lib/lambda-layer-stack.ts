import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class LambdaLayerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const layer = new lambda.LayerVersion(this, 'HelperLayer', {
      code: lambda.Code.fromAsset('resources/layers/bedrock-layer'),
      description: 'Boto3 with bedrock support',
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    const fn = new lambda.Function(this, 'LambdaFunction', {
        runtime: lambda.Runtime.PYTHON_3_9,
        code: lambda.Code.fromAsset('resources/lambda'),
        handler: 'lambda_function.handler',
        timeout: cdk.Duration.seconds(50),
        layers: [layer]
      }
    );

    fn.role?.attachInlinePolicy(new iam.Policy(this, 'bedrock-policy', {
      statements: [new iam.PolicyStatement({
        actions: ['bedrock:InvokeModel', 'bedrock:ListFoundationModels'],
        resources: ["arn:aws:bedrock:*::foundation-model/*", "*"],
      })],
    }));
  }
}
